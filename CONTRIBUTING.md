# How to update the team website

Everyone can add and edit content. This file describes the **unified way** to keep News (and related sections) up to date.

## Adding news (R2 – News)

All new items go under **`content/news/`** as one markdown file per item.

1. Create a new file: `content/news/YYYY-MM-DD-short-slug.md`
2. Set the front matter and optional body:

**General news** (announcements, events, etc.):

```yaml
---
title: "Your headline"
date: 2025-02-16
type: news
draft: false
---
Optional short body text.
```

**Blog post** (R5 – also appears under **Blog**):

```yaml
---
title: "Post title"
date: 2025-02-16
type: blog
draft: false
---
Your long-form content here...
```

**Academic entry** (paper/presentation – also appears under **Academic**):

```yaml
---
title: "Paper Title"
date: 2025-02-16
type: academic
draft: false
authors: "A. Author, B. Coauthor"
venue: "CVPR 2025"
presentation: "Oral"    # or "Spotlight" or "Poster" (optional)
top_percent: 5          # optional, e.g. top 5%
cover:
  image: "img/paper-teaser.jpg"   # optional; used only on Academic page
---
Optional abstract or note.
```

The site will show:

- **News**: all items from `content/news/` (all types).
- **Academic**: “Greatest achievements” (edited in `content/academic/_index.md`) + entries with `type: academic` in the format *Authors. Title. Accepted at Venue (Oral/Spotlight/Poster, top X%)*, with optional image.
- **Blog**: only items with `type: blog`.

## Editing other pages

- **Research directions (R3)**: edit `content/research/_index.md`
- **Academic – greatest achievements**: edit the first part of `content/academic/_index.md`
- **Community (R6)**: edit `content/community/_index.md`
- **Team (R7)**: edit `content/team/_index.md`

## Home page image

Replace `static/img/team-hero.jpg` with your team/logo image (or update `params.profileMode.imageUrl` in `config.toml`).

## Building and deploying

- Local preview: `hugo server -D`
- Build: `hugo` (output in `public/`). For GitHub Pages, configure the repo to publish from the `public` folder or use a GitHub Action that runs `hugo` and deploys.
