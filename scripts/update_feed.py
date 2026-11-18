import html
import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sources = json.loads((ROOT / "data/feeds.json").read_text(encoding="utf-8"))["sources"]
items, errors = [], []

def text_of(node):
    if node is None:
        return ""
    value = "".join(node.itertext())
    value = html.unescape(value)
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", value).strip()

def child_text(entry, names):
    for name in names:
        node = entry.find(name)
        if node is not None:
            value = text_of(node)
            if value:
                return value
    return ""

def parse_date(value):
    if not value:
        return ""
    try:
        dt = parsedate_to_datetime(value)
    except Exception:
        try:
            dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        except Exception:
            return ""
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc).date().isoformat()

def classify_broad_story(source, title, summary):
    # Broad catch-all publishers can mix technology, business and culture headlines.
    # Specialist feeds keep their declared category.
    broad = {"BBC Top Stories", "BBC World", "Al Jazeera English", "NPR News"}
    if source.get("name") in {"ArXiv cs.AI", "ArXiv cs.CL"}:
        return "AI Research"
    if source.get("name") not in broad:
        return source.get("category", "World")
    text = (title + " " + summary).lower()
    rules = [
        ("Artificial Intelligence", r"\b(ai|artificial intelligence|machine learning|chatgpt|openai|llm|robotics?)\b"),
        ("Technology", r"\b(technology|tech firms?|cyber|software|smartphone|semiconductor|chipmakers?|data breach)\b"),
        ("Business", r"\b(stocks?|shares|markets?|earnings|company|companies|business|economy|inflation|trade deal|startup|ipo)\b"),
        ("Science", r"\b(science|research|space|nasa|climate|environment|health|medical|study|scientists?)\b"),
        ("Sports", r"\b(sport|football|cricket|tennis|olympics|league|championship|athlete|match)\b"),
        ("Gaming", r"\b(video game|gaming|esports|playstation|xbox|nintendo)\b"),
        ("Entertainment", r"\b(film|movie|cinema|television|music|actor|actress|celebrity)\b"),
        ("Fashion", r"\b(fashion|designer|runway|collection|luxury|watchmaking)\b"),
    ]
    for category, pattern in rules:
        if re.search(pattern, text):
            return category
    return source.get("category", "World")

for source in sources:
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; NEXTGEN-AI-News/1.1; +https://github.com/tharunshreeoff/NEXTGEN---AI)",
            "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml;q=0.9, */*;q=0.8",
        }
        request = urllib.request.Request(source["url"], headers=headers)
        with urllib.request.urlopen(request, timeout=22) as response:
            root = ET.fromstring(response.read())

        entries = root.findall(".//item")
        atom = False
        if not entries:
            entries = root.findall(".//{http://www.w3.org/2005/Atom}entry")
            atom = True

        for entry in entries[:12]:
            title = child_text(entry, ["title", "{http://www.w3.org/2005/Atom}title"])
            if atom:
                link_node = entry.find("{http://www.w3.org/2005/Atom}link")
                link = link_node.attrib.get("href", "") if link_node is not None else ""
            else:
                link = child_text(entry, ["link"])
            summary = child_text(entry, [
                "description", "summary", "content",
                "{http://www.w3.org/2005/Atom}summary",
                "{http://www.w3.org/2005/Atom}content",
                "{http://purl.org/rss/1.0/modules/content/}encoded",
            ])
            published = child_text(entry, [
                "pubDate", "published", "updated",
                "{http://www.w3.org/2005/Atom}published",
                "{http://www.w3.org/2005/Atom}updated",
            ])
            if title and link:
                items.append({
                    "title": title[:300],
                    "summary": summary[:650],
                    "url": link,
                    "source": source["name"],
                    "date": parse_date(published),
                    "category": classify_broad_story(source, title, summary),
                    "subcategory": source.get("subcategory", ""),
                    "region": source.get("region", "Global"),
                    "kind": source.get("kind", "news"),
                })
    except Exception as exc:
        errors.append({"source": source["name"], "error": str(exc)[:180]})

seen, unique = set(), []
for item in items:
    url = item["url"].split("#")[0]
    if url not in seen:
        seen.add(url)
        item["url"] = url
        unique.append(item)

unique.sort(key=lambda item: item.get("date") or "", reverse=True)
payload = {
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "items": unique[:420],
    "source_count": len(sources),
    "successful_sources": len(sources) - len(errors),
    "source_errors": errors,
    "disclaimer": "This is a curated discovery feed, not every event worldwide. Reddit entries are community discussions, not verified reporting. Google News items link to publishers. Verify important claims against original reporting.",
}
(ROOT / "data/daily-feed.json").write_text(
    json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
)
print(f"Saved {len(unique[:420])} stories from {len(sources) - len(errors)}/{len(sources)} responding feeds.")
if errors:
    print("Some feeds did not respond:", json.dumps(errors, ensure_ascii=False))
