---
title: TactileBrowser
slug: tactilebrowser
date: 2025-01-01
excerpt: A web browser that runs on ESP32 microcontrollers, rendering HTML and CSS on a tiny touchscreen display.
tags: ['C++', 'Embedded', 'WASM', 'ESP32', 'Projects']
coverImage: /images/projects/tactilebrowser.png
repo: https://github.com/NellowTCS/TactileBrowser
link: http://nellowtcs.me/TactileBrowser/
---

I got obsessed with the idea of running a web browser on hardware that has 520KB of RAM. Not a browser wrapper, not an API client, an actual browser that parses HTML, applies CSS, does layout, and renders pixels. On a chip the size of your thumbnail. That became TactileBrowser.

There's a code comment somewhere in the renderer that says "Render document using THE POWER ENGINE". I don't remember writing that, but it feels right.

## What This Actually Does

TactileBrowser is a full web browser engine written in C/C++. It parses HTML using Lexbor, runs its own CSS parser (also Lexbor-based) that handles tag, class, and ID selectors plus CSS colors in hex, rgb, and named formats. The layout engine is 843 lines implementing CSS box model with margin, padding, border, width, height, backgrounds including linear-gradient with angle parsing, font-size, line-height, text-align, and scrolling.

The DOM renderer orchestrates the whole pipeline: download HTML, parse DOM, collect stylesheets including external ones, build a layout tree, calculate dimensions, position nodes, and render. It supports basic JavaScript via Elk on desktop or Duktape on ESP32.

## Three Targets

The library compiles for three platforms. Desktop uses SDL2 plus LVGL for rendering. WASM builds run in a browser, which means you can literally run a browser inside a browser, and yes, I find that hilarious. ESP32 is the main target, running on actual microcontroller hardware through the Tactility framework.

The platform abstraction uses a RenderInterface with callbacks, so swapping display drivers is straightforward. Each target just implements the interface and TactileBrowser does its thing.

## Current Status

The layout engine comment has a TODO that says "better layout engine", which is pretty funny given it already handles gradient angle parsing. Gopher and Gemini protocol support are on the roadmap. It renders static HTML and basic CSS fine. Don't expect your React SPA to work. Check it out at [nellowtcs.me/TactileBrowser](http://nellowtcs.me/TactileBrowser/).
