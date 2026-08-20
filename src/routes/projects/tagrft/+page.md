---
title: TAGRFT
slug: tagrft
date: 2026-03-15
excerpt: A search engine for finding that one weirdly specific GitHub repository you need but can never seem to locate.
tags: ['Web', 'Svelte', 'Search', 'Projects']
coverImage: /images/posts/tagrft.png
link: https://nellowtcs.me/TAGRFT
repo: https://github.com/NellowTCS/TAGRFT
---

You know that feeling where you need a library that does something incredibly niche, like "parses CPF numbers from Brazilian tax forms" or "converts markdown to braille art", and you spend 45 minutes on Google just to find out it already exists on GitHub with 3 stars? Yeah, that was me every other day. So I built TAGRFT to fix that.

The name is a deliberate "There's An App For That" parody, because apparently naming things is the hardest part of software engineering.

## What This Is

TAGRFT is a search engine for GitHub repos. You type what you're looking for in plain English, it searches GitHub, and gives you results. Simple enough. But the real hook is the "I'm Feeling Lucky" button, which picks a random result from the first 10 pages of search results and takes you straight there. Is it useful? Eh, sometimes. Is it fun? Absolutely.

## How It Works Under the Hood

The whole thing is a frontend-only SPA built with Svelte 5, plain Vite, no SvelteKit. Three components total: App, RepoList, and RepoCard. It calls the GitHub Search REST API directly from the browser. There's no server, no backend, just your browser talking to GitHub.

If you give it a GitHub token, it stores it in localStorage and bumps your rate limit from 60 to 5000 requests per hour, which is way more than you'll ever need. When you do hit the limit, it parses the `X-RateLimit-Reset` header and tells you exactly when you can search again. Search history lives in localStorage too, so you can see what you looked for last Tuesday.

The CSS is glassmorphism with custom properties for theming, dark mode respects `prefers-color-scheme`, and the whole thing is fully accessible with ARIA labels. Lucide Svelte icons keep things clean.

## Current Status

Look, the test script is literally `echo "Error: no test specified" && exit 1` with zero dev dependencies. It works, it's deployed at [nellowtcs.me/TAGRFT](https://nellowtcs.me/TAGRFT), and it finds repos. That's about all I can promise.
