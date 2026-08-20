---
title: Progressive Smithing
coverImage: /images/projects/progressivesmithing.png
slug: minecraft-progressive-smithing
date: 2025-01-01
excerpt: A Minecraft mod that overhauls the Smithing Table with a proper progression system and expanded functionality.
tags: ['Kotlin', 'Minecraft', 'Mod', 'Projects']
repo: https://github.com/NellowTCS/minecraft-ProgressiveSmithing
---

The Smithing Table in vanilla Minecraft is one of the most underwhelming blocks in the game. You unlock it, use it once or twice to upgrade to Netherite, and then it just sits there. The whole Netherite progression feels flat, like there's no real journey to it. You mine the ancient debris, you get the ingot, you upgrade, done. No drama, no challenge, no sense of earning it. I wanted to fix that.

Progressive Smithing turns the Smithing Table into a proper tiered system. Instead of instantly upgrading anything, you work through stages. Each tier requires specific materials and setups, making the process feel earned rather than automatic. It ties into the existing progression of the game instead of being a shortcut around it.

## How It Works

The mod uses the Architectury API so it works on both Forge and Fabric, which saved me from maintaining two separate codebases. Under the hood, I hooked into Minecraft's existing smithing recipe system but extended it with custom recipe types that handle the tiered upgrades. Each tier is defined in JSON, so it's easy to configure or override with data packs if you want to tweak the balance.

The tricky part was making the UI feel natural. I wanted the Smithing Table's interface to reflect the new progression without breaking the vanilla look and feel. That meant custom screen rendering and careful syncing between client and server state so upgrades don't glitch out in multiplayer. Getting that sync right took longer than I'd like to admit.

## The Engineering Bits

Custom smithing recipes are the backbone of the whole system. Each tier is a JSON definition with material requirements, output mappings, and progression gates. Other modpack makers can customize everything through data packs without touching the mod code. It's designed to be extended, not just used.

## Current Status

I'm still tinkering with balance and adding more tiers. The goal is to make the Smithing Table feel like a core part of the gameplay loop, not just a footnote you interact with once. It's a small mod with a specific focus, but it scratches an itch that vanilla Minecraft left unaddressed for years.
