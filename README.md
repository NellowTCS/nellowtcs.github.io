# nellowtcs.github.io

[![Built with SvelteKit](https://img.shields.io/badge/built%20with-SvelteKit-000000?logo=svelte)](https://kit.svelte.dev/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

My personal blog and portfolio site, built with SvelteKit as a fully static site. Zero runtime JavaScript overhead, automatic dark mode, responsive across all viewports, and image optimization baked into the build pipeline.

---

## Features

| Feature                 | Description                                                                |
| ----------------------- | -------------------------------------------------------------------------- |
| **Static output**       | Prerendered pages with no server required. Host anywhere.                  |
| **Dark mode**           | System preference detection plus manual toggle. Persisted across sessions. |
| **Responsive**          | Breakpoints for iPhone SE through 4K desktop, six distinct layouts.        |
| **Image optimization**  | Automatic WebP and AVIF conversion during build via image-transmutation.   |
| **Markdown content**    | MDsveX processes all posts and includes Svelte components inside markdown. |
| **Syntax highlighting** | Prism-based with custom theme across 20+ languages.                        |
| **Comments**            | Giscus integration using GitHub Discussions.                               |
| **No JS required**      | Core reading experience works with JavaScript disabled.                    |

## Quick Start

```shell
npm install
npm run dev
```

The dev server starts at `http://localhost:5173` and is accessible from other devices on your network for mobile testing.

```shell
npm run build
```

Output goes to the `build` directory, a fully static site ready for deployment.

## Repository Layout

```txt
src/
  lib/
    components/       # Reusable Svelte components (atoms, molecules, organisms)
    data/             # Blog post and project data utilities
    icons/            # SVG icon components
    scss/             # Global styles, themes, variables, mixins
    utils/            # Shared utilities and type definitions
  routes/
    (blog-article)/   # Blog post pages (markdown)
    (projects)/       # Project detail pages
    (waves)/          # Landing, blog list, project list, 404
    rss.xml/          # RSS feed endpoint
scripts/              # Email automation (weekly/monthly digests, new post notifications)
static/
  images/             # Site images and post cover images
```

## Writing Posts

Posts are markdown files in `src/routes/(blog-article)/` with front matter:

```yaml
---
title: 'Post Title'
slug: 'post-slug'
coverImage: '/images/posts/cover.png'
excerpt: 'Short description for cards and SEO'
date: '2026-01-01T12:00:00.000-06:00'
hidden: false
tags:
  - tag-one
  - tag-two
---
```

The [Front Matter VS Code extension](https://frontmatter.codes/) provides a CMS-like interface for managing post metadata.

## Packages

| Package                    | Purpose                                              |
| -------------------------- | ---------------------------------------------------- |
| `@sveltejs/adapter-static` | Static site generation                               |
| `mdsvex`                   | Markdown preprocessing with Svelte component support |
| `sass`                     | SCSS preprocessing                                   |
| `image-transmutation`      | Automatic WebP/AVIF conversion                       |
| `prismjs`                  | Syntax highlighting                                  |
| `svelte-sitemap`           | Automatic sitemap generation                         |
| `giscus`                   | GitHub Discussions-backed comments                   |

## Hosting

The build output is a fully static site. It can be deployed to GitHub Pages, Vercel, Netlify, or any static file server. The included GitHub Actions workflow (`static.yml`) handles deployment to GitHub Pages on push to `main`.

## License

MIT. See [LICENSE](LICENSE).
