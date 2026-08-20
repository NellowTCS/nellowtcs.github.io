---
title: updato
coverImage: /images/projects/updato.png
slug: updato
date: 2025-01-01
excerpt: An updater and CDN system for websites and single-file app builds, with hot-updates and deployment metrics.
tags: ['TypeScript', 'CDN', 'Deployment', 'Tool', 'Projects']
repo: https://github.com/NellowTCS/updato
link: http://nellowtcs.me/updato/
---

I kept hitting the same wall with my smaller projects. I'd build a single-file app, throw it on a server, and then have no clean way to push updates to people who already downloaded it. GitHub Releases works, but it's clunky for continuous delivery. I wanted something that just worked, like how browser apps update themselves, but for desktop tools and CLI utilities. So I built updato.

It's both a CDN for hosting files and an updater system that can check for and deliver new versions automatically. If you're building small desktop apps, CLI tools, or even just hosting static website assets, updato gives you a dead simple way to distribute updates without building a custom system for every project.

## How It Works

The core is a TypeScript server acting as a file host. When you push a new build, updato indexes it and makes it available through a versioned URL scheme. The updater client, which you embed in your app, hits a manifest endpoint to check if a newer version exists, then downloads and applies the update. It's basically the same flow as a browser auto-updater, but for anything.

The whole pipeline runs through GitHub Actions. Push to your repo, the action builds your project, uploads the artifact to updato, and updates the manifest. Metrics get tracked so you can see download counts and how many people are actually running the latest version. It's the kind of infrastructure that sounds boring until you realize how much time it saves.

## The Engineering Bits

The hot-update flow is the part I'm most proud of. When a new version drops, the client can pick it up and apply it without the user manually downloading anything. Hoshiza, one of my other projects, uses this exact mechanism. When I push to main, the running app hot-swaps to the new code. It's seamless enough that users don't even notice.

## Current Status

updato started as a solution to my own frustration, but it's grown into something I use across almost all my distributable projects. It's the invisible plumbing that keeps everything current. Most users never think about how updates work, and honestly that's the compliment. If the update system is invisible, it's doing its job.
