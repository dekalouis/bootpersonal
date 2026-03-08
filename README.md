# DSA-CLI-Helper

A command-line tool for practicing Data Structures & Algorithms problem-solving strategies. Instead of jumping straight to code, DSA-CLI-Helper walks you through a problem step by step — reinforcing the thought process behind each solution.

## Features

- **Autocomplete search** — quickly find problems by name using an interactive prompt
- **Step-by-step walkthrough** — each problem reveals its solution steps one at a time, letting you think before moving on
- **Complexity summary** — every problem ends with its time and space complexity
- **Lightweight** — no database, no server; questions are stored in a plain JSON file

## Project Structure

```
dsa-cli-helper/
├── src/
│   └── dsa_cli/
│       ├── main.py       # Entry point and CLI loop
│       ├── loader.py     # Loads questions from JSON into dataclasses
│       └── display.py    # Renders question steps to the terminal
├── questions/
│   └── questions.json    # DSA problem definitions
└── pyproject.toml
```

## Getting Started

### Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

### Installation

```bash
# Clone the repo
git clone <repo-url>
cd dsa-cli-helper

# Install dependencies with uv
uv sync

# Or with pip
pip install .
```

### Running the App

```bash
cd src/dsa_cli
python main.py
```

You'll be dropped into an interactive prompt where you can search for a problem by name.

## Usage

1. **Search** — type a problem name (autocomplete is supported) and press Enter
2. **Step through** — press Enter after each step to reveal the next one
3. **Review** — after all steps, see the time and space complexity summary
4. **Continue or exit** — choose to go back and search again, or exit the program

Type `exit` at the search prompt to quit at any time.

## Adding Questions

Questions live in `questions/questions.json`. Each entry follows this schema:

```json
{
  "id": "3",
  "title": "Problem Title",
  "category": "Category Name",
  "difficulty": "easy | medium | hard",
  "steps": [
    "Step one description",
    "Step two description"
  ],
  "time_complexity": "O(...)",
  "space_complexity": "O(...)"
}
```

## Current Questions

| # | Title | Category | Difficulty |
|---|-------|----------|------------|
| 0 | Contains Duplicates | Arrays & Hashing | Easy |
| 1 | Valid Anagram | Arrays & Hashing | Easy |
| 2 | Two Sum | Arrays & Hashing | Easy |

## Dependencies

- [questionary](https://github.com/tmbo/questionary) — interactive CLI prompts with autocomplete and select menus
