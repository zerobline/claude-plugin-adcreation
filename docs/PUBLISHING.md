# OpenAI Plugin Directory submission status

**24 October 2026**

The OpenAI submission portal has reported: **"We are not accepting more skills-only submissions at this time."** This is a **public listing eligibility restriction**, not a manifest lint error. It is not resolved by the privacy/terms links or by renaming the plugin. Check the portal for future policy changes.

## Skills-only distribution

The repository remains usable as an open-source skills package (where supported), but GitHub installation and private local use do not guarantee eligibility for the public Plugin Directory.

## Listing fields

The manifest now declares a valid supported category (`Creativity`) and four public HTTPS URLs:
- Website: https://github.com/zerobline/claude-plugin-adcreation
- Support: https://github.com/zerobline/claude-plugin-adcreation/blob/main/SUPPORT.md
- Privacy: https://github.com/zerobline/claude-plugin-adcreation/blob/main/PRIVACY.md
- Terms: https://github.com/zerobline/claude-plugin-adcreation/blob/main/TERMS.md

These linked Markdown documents are served as publicly readable GitHub pages. They should be checked while logged out and confirmed accessible to the OpenAI reviewer. If OpenAI requires an independent branded site or policy contact information, publish equivalent pages to a domain you control and update the manifest. The legal/privacy documents are drafts for publisher review, not legal advice.

## A legitimate alternate path

OpenAI documents a distinct **With MCP** submission path. To use it, the product must actually provide a stable publicly reachable HTTPS MCP endpoint with meaningful, reliable tools, e.g. ad concept validation, exportable production-ready layout generation, or campaign-spec audit. An empty or decorative MCP server designed to evade submission rules is inappropriate.

A real With MCP submission also requires domain verification, tool scans, a demo recording, exactly five positive and three negative review cases, completed privacy/terms metadata, and publisher attestations. You cannot add MCP to an existing skills-only draft as a field toggle; create an appropriate new MCP submission.

**Status:** Repository listing corrections implemented; skills-only public review blocked by stated portal restriction; no public submission/approval has been claimed.
