# Bitdefender ML Research Team – Website

Hugo-based site for the research team (GitHub Pages). Uses the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme.

## Requirements

- **Hugo extended** **v0.146.0 or newer** (required by PaperMod).  
  Install from [Hugo releases](https://github.com/gohugoio/hugo/releases) if your system version is older.

## Build & preview

```bash
hugo server -D    # preview at http://localhost:1313
hugo              # build to public/
```

## Structure

| Section | Purpose |
|--------|--------|
| **Home** | Image, short text, menu links (config + profileMode) |
| **News** | Single feed: all updates (general news, blog, academic) from `content/news/` |
| **Research** | Current research directions (text) |
| **Academic** | Greatest achievements + publication/news entries (filtered from News) |
| **Blog** | Long-form posts (filtered from News) |
| **Community** | Engagement (workshops, service, etc.) |
| **Team** | Team members and roles |

## Updating content

**All new items go in `content/news/`** with front matter `type: news`, `type: blog`, or `type: academic`. See **[CONTRIBUTING.md](CONTRIBUTING.md)** for the exact format and how to add general news, blog posts, and academic entries.

## GitHub Pages

Point the repo’s Pages source to the `public/` directory after running `hugo`, or use a workflow that runs `hugo` and deploys the output (e.g. `peaceiris/actions-hugo`).

## Home image

Place your team/hero image at **`static/img/team-hero.jpg`** or set `params.profileMode.imageUrl` in `config.toml`.
