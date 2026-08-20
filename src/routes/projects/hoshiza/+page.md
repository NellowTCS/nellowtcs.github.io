---
title: Hoshiza
coverImage: /images/projects/hoshiza.png
slug: hoshiza
date: 2025-01-01
excerpt: A GitHub repository triage board that lets you organize, tag, and visualize your repos as a kanban board or network graph.
tags: ['Svelte', 'GitHub', 'Tool', 'Projects']
repo: https://github.com/NellowTCS/Hoshiza
link: http://nellowtcs.me/Hoshiza/
---

I have way too many GitHub repos and no good way to make sense of them. GitHub's interface doesn't let you organize things the way your brain actually works. So I built Hoshiza, which means "constellation" in Japanese. It's a triage board for your repositories, and it uses GitHub itself as the database.

## What This Is

You connect via OAuth, and Hoshiza fetches all your repos. Then you organize them into status columns: Currently Working On, Living, Done, Dropped. You can tag repos, add notes, and switch between a kanban board view and a network graph visualization powered by vis-network. It's a Svelte 5 app with `$state` runes, and the whole thing is a PWA.

## The Engineering Bits

The backend is a single Cloudflare Worker, about 285 lines. It handles GitHub OAuth with HttpOnly cookie token storage, acts as a CORS-safe proxy, and has a tight allowlist: `/user/*`, `/repos/*` GET, `/graphql` POST, and a single write surface for `state.json`. That's it. No database, no server state. The Worker only holds the OAuth secret.

State syncs across devices via a private GitHub repo using the GitHub Contents API. Think of it as Git-backed localStorage. There's debounced autosync at 5 seconds, queued pushes during edits, and stale-SHA retry on 422 conflicts. I learned the hard way that you need the `repo` OAuth scope for this to work, and the error messages are not helpful. Smart status suggestions are based on repo activity, three months of inactivity means "Living," twelve months means "Dropped."

## Under the Hood

The frontend is about 880 lines of state management across 13 Svelte components. A `repoIndex` Map gives O(1) lookups for any repo. The test suite is 192 lines of Vitest covering the Worker. Self-updating is handled by `@nellowtcs/updato`.

It sounds like a simple tool, but the architecture is genuinely fun. No server means nothing to host or maintain beyond the Worker. GitHub becomes both the data source and the persistence layer. The hardest part was getting conflict resolution right when two devices edit state simultaneously, but the stale-SHA retry pattern handles it cleanly. Hoshiza made me realize that sometimes the best database is the one you already have.
