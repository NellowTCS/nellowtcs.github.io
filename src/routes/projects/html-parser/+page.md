---
title: html_parser
coverImage: /images/projects/html-parser.png
slug: html-parser
date: 2025-01-01
excerpt: A fast, zero-dependency HTML tag scanner written in ANSI C, designed for embedding in larger applications.
tags: ['C', 'Parser', 'Library', 'Projects']
repo: https://github.com/NellowTCS/html_parser
---

This code was written, buried, forgotten for months, and then rediscovered. That's the backstory. I wrote an HTML tag scanner in ANSI C, forgot about it, and then realized it was actually good enough to open-source. The README literally has a "Backstory" section about this. Life comes at you fast.

## What This Is

html_parser is a fast, streaming, zero-dependency HTML tag scanner. It does NOT build a DOM. It streams through an HTML buffer and invokes a user callback for every recognized tag it finds. That's it. It's designed for embedding in larger C and C++ applications where you need to extract tag information without pulling in a full HTML parser. It's heavily inspired by wget's html-parse, but independently written.

## How It Works

The core is a state machine that scans for `<` using `memchr`, which is basically a turbocharged version of what your brain does when skimming text. When it finds one, it classifies: `<!` means SGML or comment, `</` means end tag, anything else is a start tag. Attribute parsing handles quoted, unquoted, and minimized forms. Entity decoding covers `&lt;`, `&gt;`, `&amp;`, `&apos;`, `&quot;`, plus numeric references in both decimal and hex.

The memory model is the real engineering win. There's a `Pool` struct that works as a stack-to-heap string arena with a 256-byte stack buffer. For 95% or more of tags, zero heap allocations happen. That's not a joke, it's a design constraint that makes the whole thing fast. Comment skipping uses a "Boyer-Moore-ish" approach, advancing three characters at a time instead of scanning byte by byte.

Tag content tracking uses a doubly-linked list for open tags, with `contents_begin` and `contents_end` pointers. Optional hash-table allowlists filter tags and attributes when you need selective parsing. Error recovery handles unclosed quotes, empty unquoted values, standalone `<` characters, and other malformed markup with reasonable behavior instead of crashing. The control flow is intentionally `goto`-heavy, which is idiomatic C for performance-critical parsing.

## Current Status

Version 1.0.0, (not) published via PlatformIO with a `library.json`. It works, it's fast, and it does exactly one thing well. Sometimes the best code is the code you forgot you wrote.
