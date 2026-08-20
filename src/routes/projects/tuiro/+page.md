---
title: tuiro
coverImage: /images/projects/tuiro.png
slug: tuiro
date: 2025-01-01
excerpt: A zero-dependency Python library for producing clean, colorful terminal output with spinners, banners, and status messages.
tags: ['Python', 'Library', 'TUI', 'CLI', 'Projects']
repo: https://github.com/NellowTCS/tuiro
---

tuiro started as an internal utility inside another project and grew into something I use in almost every Python CLI I write. It's a zero-dependency Python library for making your terminal output look good, and I mean really zero dependencies. No rich, no colorama, no click. Just raw ANSI escape codes and vibes.

## What This Is

You get banner headers, section dividers, colored status messages, animated spinners, command logging, tables, and themed palettes. All of it built on nothing but `print()` with escape sequences. The whole package is six modules: the core TUI class, raw color codes, a palette system, a spinner, a version file, and a demo CLI. It's published on PyPI at v0.1.1 and has GitHub Actions CI, so it's not just a toy.

## How It Works

The `Colors` class is the foundation. It holds every ANSI escape code as class attributes, and the `disable()` method reassigns them all to empty strings. That's the entire CI compatibility strategy. Instead of trying to detect terminals or mock anything, it just blanks all color codes. Bold move, literally. The `Spinner` uses a background `threading.Thread` with Unicode quarter-circle characters at 100ms intervals, and it auto-degrades in non-TTY environments. The `Step` context manager is my favorite part, it auto-catches exceptions and reports failure, so your scripts never silently crash.

The palette system has three built-in themes: `Palette` (default), `Mono`, and `Pastel`. Pastel uses bright magenta for errors instead of red, which is a choice I stand by. You can subclass to create your own. Banners use Unicode box-drawing characters for that polished look.

## The Philosophy

I deliberately avoided every popular terminal library. The "dependency-free" philosophy means you can drop `tuiro.py` into any project and it just works, no `pip install` needed. The step context manager pattern means you can wrap any operation and get clean success/failure output automatically. It's the kind of thing that feels trivial until you try to build it yourself and realize how many edge cases there are in making terminals look human-readable.

It started because I kept copy-pasting the same ANSI code snippets into every project. Eventually I stopped and thought, why not just make this a library? So I did. And now I use it constantly. The best tools are the ones you build because you're tired of solving the same problem twice.
