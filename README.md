# El País Web Scraper

BrowserStack Technical Assignment

## Overview

Selenium-based scraper that extracts 5 articles from El País Opinion section, translates titles to English, and analyzes repeated words.

## Setup

```bash
pip install -r requirements.txt
```

Create `.env` file:
```
RAPIDAPI_KEY=your_api_key
```

## Usage

**Local Execution:**
```bash
python main.py
```

**BrowserStack Execution:**
```bash
browserstack-sdk pytest tests/browserstack_test.py
```

## Output

- `output/results.json` - Article data with translations
- `images/` - Downloaded cover images
- Terminal - Titles, content, and repeated word analysis

## Features

- Scrapes 5 articles from El País Opinion
- Downloads article cover images
- Translates Spanish titles to English (RapidAPI)
- Identifies repeated words (>2 occurrences)
- BrowserStack parallel execution (5 platforms)


---

Made by FIZA 😎