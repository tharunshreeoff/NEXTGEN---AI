# NEXTGEN AI — Explore the World, Every Day

NEXTGEN AI is a gamified daily discovery website for exploring global news, AI and technology, science, business, fashion, watches, gaming, sports, culture and more.

## Explore the news worlds
- World affairs, India, Asia, Russia & Ukraine, South Korea and politics
- Technology, Artificial Intelligence, science, space and research
- Business and markets
- Fashion and style
- Watches and horology
- Gaming, sports and entertainment
- Health and climate

## Reader tools
- Search headlines, summaries, countries, regions and sources.
- Filter by topic, region and source type.
- Sort by newest or oldest.
- Open the original publisher or community discussion.
- Expand the "Understand this story" prompts to think about evidence, context and impact.
- Save stories for later.
- Mark stories as read and earn knowledge XP.
- Track daily reading missions, explored topics, level and streak. Progress is stored locally in the user's browser.

## Sources
The feed combines publisher RSS/Atom feeds, research and official blogs, Google News discovery feeds, and selected Reddit communities. Sources include BBC, The Guardian, Al Jazeera, NPR, Times of India, TechCrunch, The Verge, Wired, Hugging Face, Google AI, arXiv, Vogue, Hypebeast, HODINKEE, Worn & Wound, Fratello, IGN, GameSpot and NASA.

Sources can be unavailable, rate-limited or change their feed formats. The website displays a source health count and the refresh workflow records failures. The feed is curated and does not represent every event happening worldwide.

Reddit posts are community discussions, not verified reporting. Google News feeds are for discovering publisher coverage; open the publisher's article for the original reporting. Always compare reliable sources before sharing important claims.

## Automatic refresh
GitHub Actions refreshes the RSS/Atom collection every three hours. The actual update frequency depends on publisher and platform availability.

## Learning features
- Animated 3D-inspired AI hero
- Agentic AI workflow teaching simulation
- Searchable AI glossary
- Six AI learning paths
- Seven-day AI learning sprint

## Run locally
Serve the repository root with a static web server. The news reader loads `data/daily-feed.json`.

## Deployment
GitHub Pages publishes the `main` branch from the repository root.

## Limitations
The website aggregates headlines, short feed excerpts and links. It does not reproduce full articles, independently fact-check every report, or generate article-specific verified analysis. The "Understand this story" panel provides general critical-reading prompts, not factual conclusions about the individual story. Gamification progress is local to each browser and is not synchronized across devices.
