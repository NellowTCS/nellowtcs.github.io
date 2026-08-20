---
title: ChessMap
coverImage: /images/projects/chessmap.png
slug: chessmap
date: 2025-01-01
excerpt: An infinitely zoomable, progressively loaded map of every chess possibility, rendered as an interactive game tree.
tags: ['JavaScript', 'Chess', 'Visualization', 'Projects']
repo: https://github.com/NellowTCS/ChessMap
link: http://nellowtcs.me/ChessMap/
---

I've always been obsessed with the idea that chess has a finite but incomprehensibly vast game tree. Every position branches into legal moves, and those branch again, and again. I wanted to actually see that tree, not just read about it. So I built ChessMap, a progressively loaded, infinitely zoomable map of every chess possibility.

## What This Is

You start at the initial position and zoom in. As you do, new nodes appear, each representing a position, each branch a legal move. Keep going and you fall through layers of the chess universe forever. The board renders via chessboard2, and chess.js handles legal move generation, FEN, and PGN. But the real trick is that you can't precompute the entire chess tree. It's too big. So ChessMap loads positions lazily, on demand, as you navigate.

## How It Works

Every node is a DOM element with the FEN and move path stored in `data-*` attributes. When you click one, a new `Chess` instance is created, the move is applied, and verbose legal moves are retrieved. They get sorted by "interestingness," captures first, then checks, then mates. At root, opening moves like e4, d4, and Nf3 get priority. The entire move tree is also kept in a JavaScript `Map` called `moveNodes` for fast lookups.

Panning works through CSS transforms with mouse drag and touch support. Scroll-wheel zoom targets the mouse position, ranging from 0.5x to 3x. Keyboard shortcuts are there too: Cmd+Z for undo, Cmd+R for reset, Cmd+C to copy PGN. The "Expand All" button throttles with `setTimeout(expandNext, 10)` to avoid freezing the browser, which I learned the hard way.

## The Details

The status bar changes color based on game state, green for checkmate, yellow for draw, red for check. A pan-hint toast appears for exactly three seconds after a 500ms delay, which sounds trivial but took surprisingly long to get right. Path replay resets to the start and replays the entire move sequence, which is useful for sharing positions.

It's vanilla HTML, CSS, and JavaScript. No build step, no framework, no bundler. Just open the HTML file and go. Sometimes the simplest architecture is the one that actually works. The chess tree is infinite, but at least now you can see a tiny corner of it.
