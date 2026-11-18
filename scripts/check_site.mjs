import { readFileSync, existsSync } from "node:fs";

const home = readFileSync("index.html", "utf8");
const sharedJs = readFileSync("assets/site.js", "utf8");
const sharedCss = readFileSync("assets/site.css", "utf8");
const pages = [
  "world-news.html",
  "ai-technology.html",
  "science.html",
  "business.html",
  "marketing.html",
  "trading.html",
  "style-watches.html",
  "gaming-sports.html",
  "learn.html",
];

new Function(sharedJs);
for (const page of pages) {
  if (!existsSync(page)) throw new Error("Missing page: " + page);
  if (!home.includes('href="' + page + '"')) {
    throw new Error("Homepage is missing a link to " + page);
  }
}
if (!sharedCss.includes(".orb") || !home.includes("orb-node")) {
  throw new Error("The homepage visual identity is incomplete.");
}
console.log("NEXTGEN AI checks passed: shared JavaScript syntax, " + pages.length + " destination pages, homepage navigation and orb styles.");
