# Abdul Mueed — Website & Documentation

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Jekyll](https://img.shields.io/badge/Jekyll-4.4.1-CC0000.svg)](https://jekyllrb.com/)
[![Hosted on GitHub Pages](https://img.shields.io/badge/hosted-GitHub%20Pages-181717.svg)](https://pages.github.com/)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#contributing)

The official website and documentation for **PluginStream** — a free, open-source Android streaming app built on a plugin and extension architecture.

This repository is a **static Jekyll site**. It contains no application code, no database and no server: every page is plain HTML/CSS plus a small amount of vanilla JavaScript that reads public data straight from the GitHub API in the visitor's browser.

- **Live site:** [am-abdulmueed.github.io](https://am-abdulmueed.github.io)
- **Repository:** [am-abdulmueed/am-abdulmueed.github.io](https://github.com/am-abdulmueed/am-abdulmueed.github.io)
- **App source:** [am-abdulmueed/pluginstream](https://github.com/am-abdulmueed/pluginstream)
- **App docs:** [pluginstream.pages.dev](https://pluginstream.pages.dev)

---

## Table of contents

- [What's in here](#whats-in-here)
- [Pages](#pages)
- [Tech stack](#tech-stack)
- [Repository layout](#repository-layout)
- [Requirements](#requirements)
- [Local development](#local-development)
- [Build and production preview](#build-and-production-preview)
- [Writing content](#writing-content)
- [Configuration reference](#configuration-reference)
- [APIs and integrations](#apis-and-integrations)
- [SEO and metadata](#seo-and-metadata)
- [Design system](#design-system)
- [GitHub Actions](#github-actions)
- [Hosting and deployment](#hosting-and-deployment)
- [Admin (CMS) setup](#admin-cms-setup)
- [Privacy and legal](#privacy-and-legal)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)
- [License and credits](#license-and-credits)

---

## What's in here

| | |
| --- | --- |
| **Purpose** | Marketing, download and documentation site for PluginStream |
| **Type** | Static site (Jekyll 4.4.1), pre-built at deploy time |
| **Runtime** | None — pure HTML, CSS and vanilla JS |
| **Backend** | None. All live data comes from public APIs called by the browser |
| **Build output** | `_site/` (generated, never committed) |
| **Deployment** | GitHub Pages (classic server-side build) with a custom domain |
| **Licence** | Apache License 2.0 |

Design goals, in order: fast on a cheap phone, readable without JavaScript, privacy-first (no cookies, no trackers, no accounts).

---

## Pages

| Route | Source | What it does |
| --- | --- | --- |
| `/` | [`index.html`](index.html) | Landing page, hero counters fed by `_data/stats.yml`, CTA into the contact page |
| `/features/` | [`features/index.html`](features/index.html) | Feature breakdown and the wider open-source project list |
| `/extensions/` | [`extensions/index.html`](extensions/index.html) | Extension/repository explainer; fetches the live repo list, live search filter, `cloudstreamrepo://` deep links |
| `/download/` | [`download/index.html`](download/index.html) | Android install guide, direct APK pulled live from GitHub releases, version-by-version history with release notes |
| `/project/` | [`project/index.html`](project/index.html) | Generic per-repository detail view (`?repo=<name>`) with README, stats and links fetched live from the GitHub API |
| `/blog/` | [`blog/index.md`](blog/index.md) | Post index for the `news` collection, plus newsletter signup |
| `/blog/<slug>/` | [`_news/`](_news) | Markdown posts (layout `news_post`) |
| `/blog/feed.xml` | [`blog/feed.xml`](blog/feed.xml) | RSS 2.0 feed of the latest 30 posts |
| `/contact/` | [`contact/index.html`](contact/index.html) | Web3Forms contact form, availability panel, contact links |
| `/privacy-policy/` | [`privacy-policy/index.html`](privacy-policy/index.html) | Privacy-first policy plus the PluginStream DMCA notice |
| `/admin/` | [`admin/index.html`](admin/index.html) | Decap CMS (noindex, `Disallow`ed in robots.txt) |
| `/app/`, `/admin/dashboard.html` | [`app/index.html`](app/index.html), [`admin/dashboard.html`](admin/dashboard.html) | Auxiliary `noindex` pages that reference assets in the app repository |
| `/robots.txt`, `/sitemap.xml`, `/llms.txt` | root | Crawler directives, generated sitemap, LLM-readable summary |

---

## Tech stack

| Layer | Choice | Notes |
| --- | --- | --- |
| Static site generator | Jekyll 4.4.1 | `kramdown` with GFM input, `rouge` for syntax highlighting |
| Markup | Hand-written HTML + Liquid | No component framework, no build step for CSS/JS |
| Styling | One hand-written stylesheet | [`assets/css/site.css`](assets/css/site.css) + [`assets/css/privacy.css`](assets/css/privacy.css) |
| Interactivity | Vanilla ES2015+ | Inline per-page `<script>` blocks, no bundler, no npm runtime deps |
| Markdown rendering | `marked.js` from a CDN | Only on the project page (README rendering) |
| CMS | Decap CMS | Git-backed, local or GitHub OAuth |
| CI | GitHub Actions | Stats refresh and IndexNow submission |

**No npm install is required to build the site.** Node.js is only needed for the optional Decap CMS local backend.

---

## Repository layout

```
.
├── _config.yml              # Site config: metadata, collections, plugins, excludes
├── _data/stats.yml          # Auto-refreshed counters (stars, updates, platforms, languages)
├── _includes/               # head.html (all SEO/meta), nav, footer, scripts, newsletter, announce bar
├── _layouts/                # default.html, news_post.html
├── _news/                   # Blog posts (folder name kept for Decap CMS compatibility)
├── assets/
│   ├── css/site.css         # Design tokens + every component
│   ├── css/privacy.css      # Privacy page additions only
│   └── images/hero/         # Responsive hero images (jpg + webp, 320/640/960w)
├── admin/                   # Decap CMS + auxiliary admin pages (noindex)
├── workers/                 # Cloudflare Worker for GitHub App OAuth (excluded from the build)
├── .github/workflows/       # refresh-stats.yml, indexnow.yml
├── .well-known/             # assetlinks.json (Android App Links), keybase.txt
├── blog/                    # Blog index + RSS template
├── contact/ download/ extensions/ features/ privacy-policy/ project/  # One folder per page
├── robots.txt llms.txt site.webmanifest
├── favicon.* android-chrome-*.png apple-touch-icon.png og-default.jpg
├── Gemfile / Gemfile.lock   # Local toolchain only — GitHub Pages ignores these
└── run.bat / server.bat     # Local convenience scripts — excluded from the published site
```

---

## Requirements

| Tool | Version | Needed for |
| --- | --- | --- |
| Ruby | 3.x (with DevKit / UCRT toolchain on Windows) | Jekyll |
| Bundler | any recent version | Dependency install |
| Git | any recent version | Cloning and deploying |
| Node.js | 18+ *(optional)* | `npx decap-server` for the CMS local backend |

The Gemfile targets **Jekyll 4.3+** (locked at 4.4.1). GitHub Pages performs its own server-side build, so the Gemfile only affects local development — that is intentional and documented in [`Gemfile`](Gemfile).

---

## Local development

### 1. Clone

```bash
git clone https://github.com/am-abdulmueed/am-abdulmueed.github.io.git
cd am-abdulmueed.github.io
```

### 2. Install dependencies

```bash
gem install bundler
bundle install
```

On Windows, `bundle install` also pulls in `wdm`, which switches Jekyll from polling to real filesystem events:

- faster saves, no 1–2 second rebuild delay
- noticeably lower CPU while the server is running

It is installed only on Windows (`install_if -> { Gem.win_platform? }`).

### 3. Run the dev server

```bash
bundle exec jekyll serve
```

Or double-click your local `run.bat`, which runs exactly that command (`run.bat` is gitignored — recreate it if a fresh clone does not have one).

The site is then available at **http://127.0.0.1:4000** with live reload. Add `--host 0.0.0.0` if you want to open it from a phone on the same Wi-Fi.

Useful flags:

```bash
bundle exec jekyll serve --drafts            # include posts with draft: true
bundle exec jekyll serve --livereload        # explicit live reload
bundle exec jekyll serve --incremental       # faster rebuilds on large edits
```

### 4. Local admin (optional)

Two terminals:

```bash
# Terminal 1 — the site
bundle exec jekyll serve

# Terminal 2 — the Decap local backend
npx decap-server          # or double-click server.bat
```

Then open **http://127.0.0.1:4000/admin/**. No login is required, and edits are written straight to your working copy (`_news/*.md`). This works because [`admin/config.yml`](admin/config.yml) sets `local_backend: true`, which only activates on localhost.

Ports used: **4000** (Jekyll), **8081** (decap-server). If 8081 is taken, stop the other process or point Decap at a different port.

### Windows notes

- Install Ruby with the **DevKit/UCRT** build so native gems (`wdm`, `ffi`) compile.
- If `bundle install` fails on `wdm`, the build is still fine — it is a developer-experience gem only.
- `run.bat` and `server.bat` are convenience wrappers and are excluded from the published site.

---

## Build and production preview

```bash
bundle exec jekyll build                    # writes _site/
bundle exec jekyll build --destination out  # custom output folder
bundle exec jekyll serve --production       # preview with production settings
```

`_site/` is gitignored and never committed — the published site is built by the host from source.

---

## Writing content

### Adding a blog post

Create `_news/YYYY-MM-DD-slug.md`:

```markdown
---
title: "Post title"
description: One-sentence lede shown under the title and in feeds.
date: 2026-11-19
tags:
  - pluginstream
  - android
redirect_from:
  - /news/old-url/
draft: false
---

Body in Markdown (GFM).
```

| Field | Required | Notes |
| --- | --- | --- |
| `title` | yes | Page title; the layout appends “— Abdul Mueed” unless `title_full` is used |
| `description` | recommended | Used for the meta description, cards and RSS |
| `date` | yes | `YYYY-MM-DD` |
| `tags` | no | Listed on the post and index |
| `redirect_from` | no | Old URLs to 301 to this post (`jekyll-redirect-from`) |
| `draft` | no | `true` hides the post from builds unless `--drafts` is passed |

Posts are published at `/blog/<slug>/`. The collection is configured in [`_config.yml`](_config.yml); the folder keeps the historical name `_news` for Decap CMS compatibility.

### Editing through the CMS

Local: `/admin/` with `decap-server` running (see above).
Live: `/admin/` on the deployed site, after completing [Admin (CMS) setup](#admin-cms-setup).

### Front-matter knobs understood by the head partial

| Key | Effect |
| --- | --- |
| `title` / `title_full` | `<title>` (suffix appended / verbatim) |
| `description` | meta description; falls back to `site.description` |
| `keywords` | meta keywords |
| `image`, `image_alt` | OG/Twitter image override |
| `homepage: true` | emits `Person` + `WebSite` JSON-LD and preloads the hero image |
| `noindex: true` | emits `noindex,nofollow` |
| `body_class`, `no_nav`, `lang` | Body class, hide navigation, language override |

---

## Configuration reference

Everything global lives in [`_config.yml`](_config.yml):

| Key | Purpose |
| --- | --- |
| `title`, `description`, `url`, `locale` | Site identity; `url` is used for canonical URLs and JSON-LD |
| `author.*`, `social.twitter` | Author entity and Twitter handle |
| `buttondown_username` | Enables the newsletter form (`githubstore`); empty disables it everywhere |
| `google_site_verification` | Google Search Console meta tag (currently verified via an HTML file instead) |
| `bing_site_verification` | Bing Webmaster meta tag (active) |
| `logo` | JSON-LD/social logo path |
| `include: [.well-known, admin]` | Folders that must not be ignored by the build |
| `collections.news` | Blog collection: `output: true`, `permalink: /blog/:slug/` |
| `defaults` | Assigns `layout: news_post` to every post |
| `markdown`, `kramdown`, `plugins` | `kramdown` + GFM, `rouge`, `jekyll-sitemap`, `jekyll-redirect-from` |
| `permalink: pretty` | Directory-style URLs |
| `exclude` | Keeps README, LICENSE, Gemfile, `workers/`, `sample/`, `run.bat` out of the published site |

---

## APIs and integrations

Everything is client-side and key-free apart from two intentionally public keys. Nothing is proxied through a server we operate.

| Integration | Used on | Endpoint | Key |
| --- | --- | --- | --- |
| GitHub REST API — repo metadata | `/project/` | `GET api.github.com/repos/:owner/:repo` | none |
| GitHub REST API — README | `/project/` | `GET api.github.com/repos/:owner/:repo/readme` | none |
| GitHub REST API — releases | `/download/` | `GET api.github.com/repos/am-abdulmueed/pluginstream/releases?per_page=100` | none |
| Extension repository list | `/extensions/` | `raw.githubusercontent.com/am-abdulmueed/pluginstream/.../pluginstream.json` | none |
| Contact form | `/contact/` | `POST api.web3forms.com/submit` | public Web3Forms access key |
| Newsletter | `/blog/` | `POST buttondown.com/api/emails/embed-subscribe/githubstore` | none (public username) |
| Social card images for posts | All blog posts | `github-store-cms-oauth.rainxchzed.workers.dev/og?title=…&description=…` | none |
| IndexNow submission | CI only | `POST api.indexnow.org/IndexNow` | public key file `1789c2770b754474b4a41db7655f202e.txt` |
| Download counter badge | CI only | `api.github-store.org/v1/badge/...` | none |

Details worth knowing:

- **GitHub API rate limit.** Unauthenticated requests are capped at 60 per hour per IP. A visitor browsing `/project/` and `/download/` a few times will not hit it, but heavy scripting or shared NAT can. The pages degrade gracefully with an error state when the API returns 403/404.
- **README images.** Relative image paths in a rendered README are rewritten to `raw.githubusercontent.com/<owner>/<repo>/<branch>/…` so they resolve outside GitHub.
- **APK asset selection.** The download page prefers a release asset literally named `pluginstream.apk` and falls back to the first `.apk` it finds.
- **Extension deep links.** Repository entries link out with the `cloudstreamrepo://` scheme so PluginStream can install them directly.
- **Web3Forms key** (`contact/index.html`) is a public, client-side key by design — it can only deliver mail to the address it was issued for. Rotate it from the Web3Forms dashboard if it is ever abused.
- **`workers/gh-store-app-oauth`** is a Cloudflare Worker used for **app** login (GitHub App OAuth state + token exchange). It is unrelated to the CMS OAuth worker and is excluded from the site build. See its own [README](workers/gh-store-app-oauth/README.md).
- **No analytics, no cookies, no consent banner** — there is nothing to consent to.

---

## SEO and metadata

[`_includes/head.html`](_includes/head.html) is the single source of truth for everything in `<head>`:

- title/description/keywords, canonical URL, `robots` control
- Open Graph and Twitter `summary_large_image` tags with a 1200×630 default card (`og-default.jpg`)
- JSON-LD: `Person` site-wide, `WebSite` on the homepage, `BlogPosting` on posts, `BreadcrumbList` on inner pages, `SoftwareApplication` on `/download/`
- verification meta tags for Google and Bing
- favicons, web manifest, RSS `<link rel="alternate">`
- render-blocking CSS with a build-based cache-bust query, fonts loaded asynchronously

Also maintained:

| File | Role |
| --- | --- |
| `sitemap.xml` | Generated by `jekyll-sitemap` |
| `robots.txt` | Allows everything except `/admin/`, `/app/`, `/preview/`, `/draft/` |
| `llms.txt` | Plain-language summary of pages and projects for LLM crawlers |
| `blog/feed.xml` | RSS 2.0, latest 30 posts |
| `1789c277…txt` | IndexNow key file (must stay at the site root) |
| `.well-known/assetlinks.json` | Android App Links verification |
| `google…html` | Google Search Console HTML verification |

`.github/workflows/indexnow.yml` re-submits every URL in the sitemap to IndexNow after each successful Pages deployment.

---

## Design system

The visual language is a manga/inked comic style: hard offset shadows, skewed “stamp” labels, zero border radius, high contrast, editorial typography.

- All tokens (`--ink`, `--page`, `--accent`, `--bw-panel`, `--sh-panel`, `--font-display`, …) live at the top of [`assets/css/site.css`](assets/css/site.css).
- Components consume those tokens only. **Do not introduce a second palette or a new shadow scale** — reuse the existing variables.
- [`assets/css/privacy.css`](assets/css/privacy.css) contains page-specific additions for the privacy policy, nothing global.
- Theme: a light/dark toggle sets `data-theme` on `<html>`; colours are defined per theme.
- Accessibility: skip link, visible focus rings, `prefers-reduced-motion` support, meaningful `alt` text, semantic headings.
- Motion and heavy visuals are opt-in per device — pointer-only parallax and animations pause when the tab is hidden or the element scrolls out of view.

A fuller reference lives in [`.claude/manga-design-system.md`](.claude/manga-design-system.md).

---

## GitHub Actions

| Workflow | Trigger | What it does |
| --- | --- | --- |
| [`refresh-stats.yml`](.github/workflows/refresh-stats.yml) | Weekly (Mondays 03:17 UTC) + manual | Fetches the star count from `api.github.com` and the download count from the backend badge, rewrites `_data/stats.yml`, commits if changed. Refuses to publish a `0` badge value. |
| [`indexnow.yml`](.github/workflows/indexnow.yml) | After a successful `pages-build-deployment`, or manual | Reads `sitemap.xml`, caps at 10,000 URLs, submits them to IndexNow. Fails loudly on anything other than HTTP 200/202. |

Both are intentionally dependency-free: `curl`, `python3` and shell only. `refresh-stats.yml` needs `contents: write`, which is scoped to the job.

---

## Hosting and deployment

The site is hosted on **GitHub Pages** as a user site, served at [am-abdulmueed.github.io](https://am-abdulmueed.github.io):

1. Content is pushed to the `main` branch of `am-abdulmueed/am-abdulmueed.github.io`.
2. GitHub builds the site with Jekyll and publishes it automatically — no `gh-pages` branch, no committed build output.
3. Because the repository is named `<user>.github.io`, the site is published at the `https://am-abdulmueed.github.io` root with HTTPS enabled by default.
4. Because Pages performs the build itself, `Gemfile`/`Gemfile.lock` are ignored in production; keep plugins limited to what Pages supports (currently `jekyll-sitemap` and `jekyll-redirect-from`).

Set `url:` in `_config.yml` to the published domain — it drives canonical URLs, the sitemap, the RSS feed and JSON-LD. It must match the domain the site is actually served from.

### Deploying changes

```bash
git add <files>
git commit -m "Describe the change"
git push origin main
```

Watch the **Actions** tab and the Pages deployment; a typical build takes a minute or two. Verify the live page afterwards (hard-refresh: the CSS URL carries a build-based cache-bust query).

### Rolling back

Revert the offending commit and push — every push to `main` redeploys:

```bash
git revert <commit-sha>
git push origin main
```

### DNS and domain

The site uses the default GitHub Pages domain, so no DNS records or `CNAME` file are needed. If a custom domain is added later:

- Create the `CNAME` file (or set it in **Settings → Pages**) and point the domain's `A`/`AAAA` (apex) or `CNAME` (subdomain) records at GitHub Pages.
- Update `url:` in `_config.yml` and the `sitemap:` line in `robots.txt` to the new domain, and re-check `llms.txt` and the IndexNow workflow host.

### Deploying elsewhere

Any static host works, because the output is plain files:

```bash
bundle exec jekyll build          # → _site/
```

Then serve `_site/` from Netlify, Cloudflare Pages, Vercel, S3/CloudFront, Nginx, or a plain container. For non-GitHub hosts, build with `bundle exec jekyll build` in CI instead of relying on the Pages builder, and set `url:` in `_config.yml` to the new domain.

---

## Admin (CMS) setup

The CMS is **Decap CMS** at `/admin/`, configured by [`admin/config.yml`](admin/config.yml).

### Local (already works)

See [Local admin](#4-local-admin-optional). No OAuth, no keys, no GitHub access required.

### Live (publishing straight to GitHub)

Live editing needs three things, because a static site cannot complete a GitHub OAuth handshake by itself:

1. **A repository you control** — set `backend.repo` in [`admin/config.yml`](admin/config.yml) to your `owner/repo` and `branch` to your default branch.
2. **A GitHub OAuth App** — Settings → Developer settings → OAuth Apps → New. Note the **Client ID** and **Client Secret**, and set the authorization callback URL to `https://<your-worker>.workers.dev/callback`.
3. **An OAuth proxy worker** (a small Cloudflare Worker is the usual choice) — deploy it, add the client ID/secret as encrypted secrets (`wrangler secret put …`; some proxies expect `OAUTH_CLIENT_ID`/`OAUTH_CLIENT_SECRET`, others `GITHUB_CLIENT_ID`/`GITHUB_CLIENT_SECRET` — check the worker's own docs), and allow your site's origin.

Then point the CMS at your worker and update the display URLs:

```yaml
backend:
  name: github
  repo: <owner>/<repo>
  branch: main
  base_url: https://<your-worker>.workers.dev

site_url: https://your-domain.example
display_url: https://your-domain.example
```

Commit and push, open `/admin/` on the deployed site, sign in with GitHub, and saves become commits to `backend.branch`.

> **Note:** the repository currently ships with the original owner's `repo` and `base_url` values, so a fork must change both before live editing works. [`workers/gh-store-app-oauth`](workers/gh-store-app-oauth) is an **app-login** worker and must not be used as the CMS OAuth proxy.

Media uploaded through the CMS is written to `assets/uploads` and served from `/assets/uploads`. The CMS route is `noindex` and disallowed in `robots.txt`.

---

## Privacy and legal

- [Privacy policy](privacy-policy/index.html): no accounts, no cookies, no analytics, no personal data collection; PluginStream hosts no content and extensions come from the open-source community; includes the full **DMCA notice** and a rights-holder contact path.
- The site itself loads no third-party scripts beyond Google Fonts (CSS only) and `marked.js` on the project page.
- **PluginStream distributes no media.** The app is a client; content is fetched from third-party sites at the user's request and remains the user's responsibility under local law.
- The project is not affiliated with GitHub, Inc., Google, or any streaming platform.

---

## Contributing

Contributions to copy, accessibility, performance and documentation are welcome.

1. Fork the repository and create a branch: `git checkout -b fix/readme-typo`.
2. Make the change. Keep the conventions: hand-written HTML/Liquid, existing CSS tokens only, no new dependencies, no frameworks.
3. Test locally: `bundle exec jekyll build` must finish without warnings, and the affected pages should be checked in both light and dark themes, plus a narrow mobile viewport.
4. Keep JavaScript progressive — the page must remain usable with JS disabled.
5. Open a pull request describing **what changed and why**, with before/after screenshots for visual changes.

For app bugs rather than website issues, open an issue on [am-abdulmueed/pluginstream](https://github.com/am-abdulmueed/pluginstream/issues) instead.

---

## Troubleshooting

| Symptom | Cause and fix |
| --- | --- |
| `bundle install` fails on `wdm` | Native build issue on Windows. Install the DevKit/UCRT Ruby build, or remove the `wdm` group — it only affects watch performance. |
| Saves take 1–2 seconds to trigger a rebuild | `wdm` is not installed, so Jekyll is polling. See above. |
| `Address already in use` on 4000 or 8081 | Another Jekyll/decap-server instance is running. Stop it, or pass `--port 4001` to Jekyll. |
| `/admin/` asks for a login locally | `decap-server` is not running, or `local_backend: true` was removed from `admin/config.yml`. |
| `/project/` or `/download/` shows an error state | GitHub API rate limit (60/hour/IP) or a renamed/deleted repository. Check the browser console and the API response. |
| Changes do not appear on the live site | The push has not finished deploying, or the browser cached the CSS. Check the Actions tab, then hard-refresh. |
| Styles look wrong after editing CSS | A token or a closing brace is missing in `site.css`. Reuse existing variables rather than hard-coding colours. |
| Sitemap missing a page | The file lacks front matter, or matches a pattern in `exclude` in `_config.yml`. |

---

## License and credits

- Licensed under the **Apache License 2.0** — see [LICENSE](LICENSE).
- Design, code and maintenance by **Abdul Mueed**.
- PluginStream and every referenced project remain the property of their respective authors.

Questions, bug reports or sponsorship: use the [contact page](https://am-abdulmueed.github.io/contact/).
