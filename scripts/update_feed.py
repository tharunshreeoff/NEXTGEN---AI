import json, re, urllib.request, xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
feeds = json.loads((ROOT/"data/feeds.json").read_text(encoding="utf-8"))["sources"]
items, errors = [], []
def clean(value):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", value or "")).strip()
for feed in feeds:
    try:
        req=urllib.request.Request(feed["url"],headers={"User-Agent":"NEXTGEN-AI-Learning-Hub/1.0"})
        with urllib.request.urlopen(req,timeout=25) as response:
            raw=response.read()
        root=ET.fromstring(raw)
        entries=root.findall(".//item")
        if not entries:
            entries=root.findall(".//{http://www.w3.org/2005/Atom}entry")
        for entry in entries[:15]:
            def get(*paths):
                for path in paths:
                    node=entry.find(path)
                    if node is not None:
                        val=node.text or node.attrib.get("href","")
                        if val: return clean(val)
                return ""
            title=get("title","{http://www.w3.org/2005/Atom}title")
            link=get("link","{http://www.w3.org/2005/Atom}link")
            if not link:
                node=entry.find("{http://www.w3.org/2005/Atom}link")
                if node is not None: link=node.attrib.get("href","")
            summary=get("description","summary","content","{http://www.w3.org/2005/Atom}summary","{http://www.w3.org/2005/Atom}content")
            published=get("pubDate","published","updated","{http://www.w3.org/2005/Atom}published","{http://www.w3.org/2005/Atom}updated")
            date=""
            if published:
                try:
                    dt=parsedate_to_datetime(published)
                except Exception:
                    try: dt=datetime.fromisoformat(published.replace("Z","+00:00"))
                    except Exception: dt=None
                if dt: date=dt.date().isoformat()
            if title and link:
                items.append({"title":title,"summary":summary[:420],"url":link,"source":feed["name"],"date":date})
    except Exception as exc:
        errors.append({"source":feed["name"],"error":str(exc)[:180]})
seen=set(); unique=[]
for item in items:
    if item["url"] not in seen:
        seen.add(item["url"]); unique.append(item)
unique.sort(key=lambda x:x.get("date") or "",reverse=True)
payload={"generated_at":datetime.now(timezone.utc).isoformat(),"items":unique[:80],"source_errors":errors}
(ROOT/"data/daily-feed.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding="utf-8")
print(f"Saved {len(unique[:80])} feed items; {len(errors)} source errors.")
