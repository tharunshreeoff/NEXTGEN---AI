# NEXTGEN AI — World Discovery & Learning Academy

A multi-page public website for discovering daily world news and learning practical AI skills.

## Separate pages
- `index.html` — Home and destination directory
- `world-news.html` — World affairs, India, geopolitics and regional news
- `ai-technology.html` — AI and technology news
- `science.html` — Science, space, health, climate and research
- `business.html` — Business and economy
- `style-watches.html` — Fashion, watches and design
- `gaming-sports.html` — Gaming, sports and entertainment
- `learn.html` — Practical AI learning roadmap, seven-day sprint and glossary

Each major section opens a separate page within the same NEXTGEN AI website. Navigation uses page links rather than scrolling to anchors on a long single page.

## News experience
- Search and sort stories.
- Each page filters the shared daily feed to its own topics.
- Headlines link to original publishers.
- Readers can mark stories as read and save stories in local browser storage.
- News feeds can be incomplete or delayed; source health is displayed where the feed is shown.
- Reddit items are community discussions, not verified reporting.

## Learning Academy
The Learning Academy contains 12 practical modules:
1. Python for AI
2. SQL, data handling and APIs
3. Machine learning fundamentals
4. Deep learning
5. LLMs and tokens
6. Prompt design and structured output
7. Embeddings, vector search and RAG
8. AI agents and tool calling
9. MCP and agent interoperability
10. Evaluation, testing and safety
11. Deployment, monitoring and cloud basics
12. Portfolio and communication

It also includes a seven-day starter sprint and a practical glossary. Sprint completion is stored locally in the browser.

## Shared assets
- `assets/site.css` — responsive layout and visual design
- `assets/site.js` — news rendering, saving, reading progress and sprint state
- `data/daily-feed.json` — latest collected news entries
- `data/feeds.json` — configured RSS/Atom sources
- `scripts/update_feed.py` — scheduled feed collector

## Limitations
This is a curated discovery feed, not a complete record of every event worldwide. Headlines and excerpts link to original sources; the site does not independently fact-check every article or generate article-specific verified analysis. Local browser progress is not synchronised between devices.


## Additional sections
- `marketing.html` — brand strategy, digital growth, campaign news and marketing analytics.
- `trading.html` — stocks, US and Indian markets, gold, crude oil, commodities and forex news. Educational content only; not live quotes or investment advice.

The homepage uses an animated sage-glass sphere with orbital rings as the visual identity. Broad general-news feeds are topic-classified where possible; specialist feeds retain their publisher-defined categories.
