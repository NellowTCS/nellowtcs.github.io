---
title: Generic-Platformer
coverImage: /images/projects/generic-platformer.png
slug: generic-platformer
date: 2025-01-01
hidden: true
excerpt: A 2D platformer with a built-in level editor where players can create and share their own stages.
tags: [JavaScript, game, platformer, 'Projects']
repo: https://github.com/NellowTCS/Generic-Platformer
link: http://nellowtcs.me/Generic-Platformer/
---

I've wanted to make a platformer since I was a kid, and I finally sat down and did it. Generic-Platformer is a 2D side-scrolling game with coins to collect, spikes to avoid, and wall jumps to master. But the real reason I built it was to have a level editor built right in.

The level editor lets you drag and drop tiles, place hazards, and set spawn points. Once you've got a level you're happy with, you can save it and share the level data with others. It's JSON under the hood, so sharing is as easy as copying a string. Other players can paste that string into their copy of the game and play your level immediately.

The game itself runs on vanilla JavaScript with canvas rendering. The physics are simple but tight, wall jumping feels responsive, and the collision detection handles the usual platformer edge cases. I spent a lot of time tweaking the movement values until the controls felt right because nothing kills a platformer faster than floaty or stiff movement.

This project taught me a ton about game loops, input handling, and why game designers obsess over "game feel." It's generic by name but I put genuine love into making it fun to actually play.
