# How to update the team website

Everyone can add and edit content. This file describes the **unified way** to keep News (and related sections) up to date.

## Adding news (R2 – News)

All new items go under **`content/news/`** as a **folder per item** (page bundle). This lets you keep images and other assets next to the post and reference them by filename.

1. Create a **folder**: `content/news/YYYY-MM-DD-short-slug/`
2. Create **`index.md`** inside that folder with the front matter and body.
3. (Optional) Put images or other assets in the **same folder**. Reference them in `index.md` by filename only (e.g. `![Alt text](my-image.png)` or `cover.image: "my-image.png"`). That way the image appears in the right place in the post and works everywhere (local preview and production).

**About `date`:** Use the **publication or announcement date** of the item (when the paper was accepted, when the event happens, or when the post was first published), not the date you add it to the site. This keeps ordering and displayed dates meaningful.

**General news** (announcements, events, etc.):

- Folder: `content/news/2025-02-16-workshop-announcement/`
- File: `content/news/2025-02-16-workshop-announcement/index.md`

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

- Folder: `content/news/2025-02-16-my-blog-post/`
- File: `content/news/2025-02-16-my-blog-post/index.md`

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

- Folder: `content/news/2025-02-16-paper-slug/`
- File: `content/news/2025-02-16-paper-slug/index.md`
- Optional: put a teaser image in the same folder (e.g. `paper-teaser.png`) and set `cover.image: "paper-teaser.png"`. Use the same filename in the body to show the image in the post (e.g. `![Caption](paper-teaser.png)`).

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
  image: "paper-teaser.png"   # optional; filename of image in this folder
---
Optional abstract or note.
```

**Community entry** (courses, teaching, outreach – also appears under **Community**):

- Folder: `content/news/2025-03-01-new-course-deep-learning/`
- File: `content/news/2025-03-01-new-course-deep-learning/index.md`

```yaml
---
title: "New course: Deep Learning @ FMI"
date: 2025-03-01
type: community
draft: false
---
Optional short summary. Enrollments open in March.
```

The site will show:

- **News**: all items from `content/news/` (all types).
- **Academic**: “Greatest achievements” (edited in `content/academic/_index.md`) + entries with `type: academic` in the format *Authors. Title. Accepted at Venue (Oral/Spotlight/Poster, top X%)*, with optional image.
- **Community**: static “Courses” content (in `content/community/_index.md`) + entries with `type: community` (e.g. new course announcements).
- **Blog**: only items with `type: blog`.

## Editing other pages

- **Research directions (R3)**: edit `content/research/_index.md`
- **Academic – greatest achievements**: edit the first part of `content/academic/_index.md`
- **Community (R6)**: edit `content/community/_index.md` for the static Courses section; add news items with `type: community` in `content/news/` for course announcements etc.
- **Team (R7)**: edit `content/team/_index.md`

## Home page image

Replace `static/img/team-hero.jpg` with your team/logo image (or update `params.profileMode.imageUrl` in `config.toml`).

## Building and deploying

- Local preview: `hugo server -D`
- Build: `hugo` (output in `public/`). For GitHub Pages, configure the repo to publish from the `public` folder or use a GitHub Action that runs `hugo` and deploys.
