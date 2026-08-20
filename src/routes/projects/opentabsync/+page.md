---
title: OpenTabSync
slug: opentabsync
date: 2025-01-01
hidden: true
excerpt: An open-source, cross-browser tab group sync extension that keeps your tabs consistent everywhere.
tags: ['Browser Extension', 'Sync', 'Tabs', 'Open Source', 'Projects']
repo: https://github.com/NellowTCS/OpenTabSync
---

I use different browsers on different machines, and every time I switch, I lose track of which tab groups I had open where. Bookmarks don't solve this because tab groups are a different thing entirely. I wanted my tab groups to follow me across browsers, so I built OpenTabSync.

OpenTabSync is a browser extension that syncs your tab groups across different browsers and devices. You set up your groups in Chrome, and they show up in Firefox, and vice versa. It's cross-browser tab group synchronization that actually works.

## How it works

The extension captures your tab group state (which tabs are in which groups, their names, colors, and positions) and stores it in a sync backend. When you open a different browser with the extension installed, it pulls the latest state and reconstructs your tab groups.

Tab group data is serialized into a portable format that isn't tied to any single browser's internal representation. The sync layer handles conflict resolution when groups change on multiple browsers between syncs. It uses browser storage APIs for local caching and a lightweight remote backend for cross-device sync.

The extension listens for tab group changes in real time, so modifications propagate quickly rather than waiting for a manual sync trigger.

## Features

- Cross-browser tab group synchronization
- Real time sync when groups change
- Portable tab group format across browsers
- Conflict resolution for simultaneous edits
- Works with Chrome, Firefox, and other Chromium browsers
- Open source, no telemetry, no accounts required
- Local caching for fast startup

## Where it's going

I want to add support for syncing tab groups to mobile browsers too, and maybe add a CLI tool for managing your tab groups outside the browser. The core idea is that your browsing context should be yours, wherever you are.
