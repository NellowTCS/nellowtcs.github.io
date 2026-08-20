---
title: Ethashi
coverImage: /images/projects/ethashi.png
slug: ethashi
date: 2025-01-01
hidden: true
excerpt: An Ethernet to WiFi adapter with USB host capability for printers, USB SSDs, and more.
tags: ['Embedded', 'Hardware', 'Networking', 'USB', 'Projects']
repo: https://github.com/NellowTCS/Ethashi
---

I kept running into the same annoying problem. I had devices with Ethernet ports but no WiFi, and devices with USB ports but no network access. I wanted a single, small adapter that could bridge Ethernet to WiFi and also act as a USB host for things like printers and external drives. So I built one.

Ethashi is essentially a compact network bridge and USB host rolled into one device. It takes an Ethernet connection and bridges it to WiFi, while also exposing a USB host port for peripherals. Plug in a printer, a USB SSD, or anything else, and it shows up on the network.

## How it works

At its core, Ethashi runs on a microcontroller that handles both Ethernet and WiFi networking stacks simultaneously. The Ethernet interface connects to your wired network, while the WiFi radio bridges traffic to a wireless access point or client connection. NAT and routing logic handles traffic between the two interfaces.

The USB host capability comes from the microcontroller's USB OTG support. A software stack on the device enumerates connected USB devices and exposes them over the network, whether that's a printer via standard network printing protocols or a storage device via SMB or similar file sharing.

## Features

- Ethernet to WiFi bridging in a compact form factor
- USB host port for printers, USB SSDs, and other peripherals
- Network printing support for connected printers
- File sharing for connected storage devices
- Low power consumption
- Small enough to tuck behind a monitor

## What's next

I want to expand the USB device support and add a proper web interface for configuration. Right now setup requires some manual work, but the goal is a truly plug-and-play experience where you just connect everything and it works.
