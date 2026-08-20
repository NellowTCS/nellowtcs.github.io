---
title: Obsidian-AutoLink
coverImage: /images/projects/autolink.png
slug: obsidian-autolink
date: 2025-06-01
excerpt: An Obsidian plugin that automatically creates backlinks between notes, keeping your knowledge graph connected without manual work.
tags: ['TypeScript', 'Obsidian Plugin', 'Backlinks', 'Projects']
repo: https://github.com/NellowTCS/Obsidian-AutoLink
---

I kept writing notes in Obsidian and forgetting to link them to other notes. You know the drill. You write about "machine learning" and completely forget you already have a note called "machine learning" sitting right there. Your knowledge graph stays disconnected because you're lazy. Same. So I built AutoLink to fix my own bad habits.

## What This Does

You type a word that matches an existing note title, and AutoLink turns it into a `[[wiki-style backlink]]` automatically. Four modes to choose from. Autonomous mode inserts links the moment you finish typing a matching word. Semi-Autonomous does the same but only checks notes in the current folder. Suggestions mode gives you a popup dropdown, like VS Code's autocomplete, and lets you pick. Custom mode lets you mix approaches with folder filtering.

## How It Works

On load, the plugin scans your entire vault and builds two Maps, one for note titles and one for aliases pulled from frontmatter. Then it listens to editor-change events, debounced at 300ms, and matches what you're typing against those Maps using Unicode-aware regex.

The smart part is disambiguation. If multiple notes share a prefix like "project-alpha" and "project-beta", it doesn't just link the first match. It waits until your word is complete and unambiguous. The `getBestMatch` function iterates up to 10 times, stripping leading words to find the right note. There's also an `isInsideLink` function that counts open and close `[[` brackets so it never double-wraps an existing link.

## The Undo System

This was the tricky bit. Auto-linking is convenient until it links something you didn't want. So there's a stack of 10 undo entries. If you hit backspace or delete within 30 seconds of an auto-link, it restores the original text. After undoing, auto-linking pauses for 1 second so you can type without getting re-linked immediately.

It's on the official Obsidian Community Plugins store, has a proper test suite with Vitest, and supports aliases with display showing alias pointing to actual note. Honestly it's one of those plugins that sounds small but changes how you write notes.
