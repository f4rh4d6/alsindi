
# Working

1- Done code or change anything before asking gor approval 
2- memories all the films when opening a new chat you should already have every thing remember 




# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

I want you to to give the plan for every steps you will be doing after I give a command and ask me to give you the go then do it 

## Running the site

The can only be opened with Google Chrome Html file 

## Architecture

This is a **no-build, no-framework** photography portfolio. There is no npm, no bundler, no transpilation step.

### Data flow

All site content lives in a single object in [`data.js`](data.js) (`DEFAULT_SITE_DATA`). Every HTML page loads `data.js` and `script.js` directly via `<script>` tags. On page load, `script.js` calls `getSiteData()` and hydrates the DOM using `data-bind` attributes for simple fields, and imperative DOM writes for structured content (gallery grid, essay sections, stats, contact channels).

When the admin panel saves changes, `server.py` receives the updated object via `POST /api/save` and rewrites `data.js` on disk — making `data.js` both the runtime data source and the persisted store. A timestamped backup is written to `backups/` on every save.

### Server API (`server.py`)

| Endpoint | Method | Purpose |
|---|---|---|
| `/api/data` | GET | Parses and returns `data.js` as JSON |
| `/api/images` | GET | Lists files in `images/` |
| `/api/inquiries` | GET | Returns `inquiries.json` |
| `/api/save` | POST | Rewrites `data.js` with new content |
| `/api/upload` | POST | Accepts base64-encoded image, writes to `images/` |
| `/api/inquiry` | POST | Appends a contact form submission to `inquiries.json` |
| `/api/save-css` | POST | Writes a CSS override file and injects its `<link>` into all HTML pages |

### Key relationships

- `data.js` → read by every HTML page and by the admin panel; written by `server.py`
- `script.js` → shared across all public pages; handles data binding, gallery filtering, and the lightbox
- `admin.html` + `admin.css` → self-contained admin UI; communicates with `server.py` exclusively via the API endpoints above
- `inquiries.json` → created on first contact form submission; not committed (runtime file)
- `backups/` → auto-created by server on save; not committed

### Photo catalog

Each entry in `data.photos` has: `id`, `num`, `title`, `year`, `category` (`architecture` | `landscape` | `commentary`), `caption`, `image` (path relative to site root), and `meta`. The gallery page filters on `category` client-side.

### CSS override injection

`POST /api/save-css` writes a `.css` file to the site root and patches a `<link>` tag into every public HTML page's `<head>`. This is how the admin's design editor persists visual changes without touching `style.css` directly.
