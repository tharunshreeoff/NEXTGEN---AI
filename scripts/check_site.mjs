import { readFileSync } from "node:fs";

const html = readFileSync("index.html", "utf8");
const scripts = [...html.matchAll(/<script\b[^>]*>([\s\S]*?)<\/script>/gi)];
if (!scripts.length) throw new Error("No inline JavaScript found in index.html");
for (let i = 0; i < scripts.length; i++) {
  new Function(scripts[i][1]);
}
console.log("Checked " + scripts.length + " inline script block(s): syntax OK.");
