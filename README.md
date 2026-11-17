# NEXTGEN AI

A public learning and daily discovery hub for understanding AI, technology, science, business and world developments.

## Daily news reader
- Search headlines and summaries.
- Filter by topic: World, Technology, Artificial Intelligence, Science, Business and Research.
- Filter by source type: news publishers, research/official blogs, and Reddit community discussions.
- Sort by newest or oldest.
- Open every original article or discussion.
- Use the "Read & learn" panel to ask evidence, context and impact questions.

## Sources and editorial labels
The feed combines selected publisher RSS/Atom feeds, official AI/research feeds, and Reddit subreddit feeds. Reddit is labelled as community discussion and is not verified reporting. A Reddit post is a lead for discovery, not proof of a claim. Always open original links and compare independent reporting for important topics.

Feeds are refreshed by GitHub Actions every three hours (UTC schedule). Actual update frequency depends on the publisher, Reddit availability and GitHub Actions scheduling. Some sources may occasionally fail or block automated requests; failures are recorded in `data/daily-feed.json`.

## Learning features
- Animated 3D-inspired AI hero
- Agentic AI workflow teaching simulation
- Searchable AI glossary
- Six learning paths
- Seven-day learning sprint with browser-local progress

## Run locally
Open `index.html` through a static web server from the repository root. The news reader fetches `data/daily-feed.json`.

## Deployment
GitHub Pages is configured to publish the `main` branch from the repository root.

## Important limitations
The site aggregates headlines, excerpts and original links. It does not independently fact-check reports, generate article-specific AI summaries, or represent every event happening worldwide. The learning prompts are critical-reading guidance, not factual conclusions about an individual story.
