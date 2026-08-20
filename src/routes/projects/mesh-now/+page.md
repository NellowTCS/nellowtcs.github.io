---
title: Mesh-NOW
coverImage: /images/projects/mesh-now.png
slug: mesh-now
date: 2025-04-01
excerpt: A serverless mesh network built on ESP-NOW, letting ESP32 devices communicate directly without any Wi-Fi infrastructure.
tags: ['C', 'Embedded', 'ESP-NOW', 'Mesh Network', 'Projects']
repo: https://github.com/NellowTCS/Mesh-NOW
---

I had a pile of ESP32 boards and a problem. I needed them to talk to each other, but there was no router, no access point, no internet. Not "the Wi-Fi is down" kind of no, but literally no network infrastructure at all. So I made them build their own.

Mesh-NOW is a mesh networking system built on ESP-NOW, Espressif's low-power wireless protocol. ESP32 devices communicate directly with each other, forming a self-healing mesh where messages hop from node to node until they reach their destination. No central coordinator, no router, no internet. Just boards talking to boards.

## How the Mesh Works

Each ESP32 broadcasts messages to its neighbors using ESP-NOW. When a node receives a message not addressed to it, it relays that message to its own neighbors, and so on, until the message reaches its destination. The routing finds the shortest path automatically. If a node dies, messages reroute around the dead node. Self-healing means you can yank power from any board and the network adapts without you doing anything.

Peer discovery happens via UDP broadcasts. Devices find each other automatically when they come into range. Each board also creates its own Wi-Fi access point, so you can connect with a phone or laptop and access a web interface served directly from the mesh.

## The Architecture

The system is entirely C firmware. Four modules handle everything: `mesh_now` manages ESP-NOW communication and peer tracking, `wifi_manager` handles the access point and peer discovery, `web_server` serves the chat UI and HTTP message endpoints, and `message_queue` uses FreeRTOS queues for reliable message handling.

Messages flood through the mesh until every device has seen them. It's simple, it's reliable, and it works with any ESP32 variant (ESP32, S2, S3, C3, C6).

## Current Status

This is very WIP. Messages use ESP-NOW's default 128-bit encryption with no PMK or spoofing protection yet. The mesh routing and peer discovery work. You can genuinely set up a network of ESP32 boards with no router and have them pass messages between each other. It's a cool demo of what ESP-NOW can do when you string it together beyond simple point-to-point communication.
