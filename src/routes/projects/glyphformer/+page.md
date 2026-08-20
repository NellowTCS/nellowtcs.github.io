---
title: Glyphformer
coverImage: /images/projects/glyphformer.png
slug: glyphformer
date: 2025-01-01
excerpt: A 2D platformer game rendered entirely in Unicode characters in your terminal, with a real physics engine and 5 hand-crafted levels.
tags: ['Python', 'Game', 'Terminal', 'Projects']
repo: https://github.com/NellowTCS/Glyphformer
---

I've always been fascinated by what you can do with almost nothing. Give me a full game engine with sprites and shaders and I'll build something decent. But take all that away and leave me with nothing but Unicode characters? That's where things get interesting. Glyphformer is a 2D platformer rendered entirely in text, and it's more fun than it has any right to be.

## What This Is

You control `[]`, jump between `▓▓` blocks, collect `◆◆` coins, avoid `▲▲` spikes, and reach `⚑⚑` flags. That's the entire visual language. No images, no canvas, no curses library, just ANSI escape codes writing characters to specific terminal positions. And somehow it works.

## The Physics Engine

This lives in a single 790-line Python file. Gravity is 0.08, jump velocity is -1.6, move acceleration is 0.10. Air friction is 0.98, ground friction is 0.88. Collision detection uses AABB with per-axis resolution and 4 sub-steps per frame to prevent tunneling through thin platforms.

There's coyote time, an 80ms grace period after walking off an edge where you can still jump. Jump buffering gives you an 80ms window to press jump before landing and it still registers. Fast-fall doubles gravity when you hold down. It's a real physics engine with real game feel, just rendered in text.

## The Game

Five hand-crafted levels as Python string grids. A viewport of 36 by 20 characters with horizontal scrolling camera. The game runs at 30 FPS with separate screens for menu, level select with mini-preview, gameplay, pause, death, win, and game-over. You get 3 lives, coin tracking, per-level best times, and star ratings. There's even a HUD.

## How It Runs

It uses pyComputerSDK for rendering, which means it runs natively AND in the browser. You can install it through pyComputer's package manager with `pkg install glyphformer`. The whole thing bundles as a `.pycapp` file.

## What's Next

Look, the truth is, building a platformer in Unicode characters taught me more about game design than any fancy engine ever did. When you can only communicate through text characters, every design decision has to earn its place. It's constraint-based design at its most pure, and I think that's kind of beautiful.
