---
title: WebViewBrowser
slug: webviewbrowser
date: 2025-01-01
excerpt: A web browser written entirely in AppleScript using Apple's Script Editor and WebKit.
tags: ['AppleScript', 'Browser', 'macOS', 'Projects']
repo: https://github.com/NellowTCS/WebViewBrowser
---

Can you build a web browser in AppleScript? Technically, yes. Should you? Almost certainly not. Did I do it anyway? Of course I did.

WebViewBrowser is a web browser written entirely in AppleScript, running inside Apple's Script Editor. It's not Chrome, it's not Safari, it's a bunch of Apple Events duct-taped together into something that loads web pages. And honestly, the fact that it works at all still amuses me. The whole thing started as a joke experiment, "what if I used AppleScript for something it was never designed to do," and it kind of just... worked.

## How It Works

The trick is that AppleScript can talk to other macOS applications through Scripting Bridge and Apple Events. WebViewBrowser uses this to create and control a WebKit WebView behind the scenes, loading URLs and rendering content through macOS's built-in web rendering stack. The AppleScript acts as the controller, managing navigation, handling user input, and orchestrating the browser window.

It's basically the world's most over-engineered way to open a webpage. The browser UI is minimal, the navigation is basic, but it genuinely renders real websites using the system's native WebKit engine. You can type a URL, hit enter, and watch a real page load. In Script Editor. It's beautiful in the worst way.

## The Details

Back, forward, reload, URL input. Those are your controls. That's what you get. The whole thing is intentionally minimal because the point was never to build a competitive browser. The point was to prove that AppleScript could do it, and then to be mildly horrified that it actually could.

This project taught me way more about macOS's inter-application communication system than I ever expected to know. Apple Events are weird, powerful, and deeply underrated. The way Script Editor can reach into other applications and puppet their UIs is something most people never even realize is possible.

## Current Status

It runs, it browses, and it's a fantastic conversation starter about what AppleScript can actually do when you abuse it in ways its creators never intended. Would I use it as my daily driver? Look, I have standards. But would I build it again given the same Thursday evening curiosity? Absolutely.
