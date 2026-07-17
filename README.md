# CLI Tools Suite

Three command-line tools built with Python — an expense tracker, a student grade manager, and a weather lookup tool — built to practice file I/O, JSON persistence, API integration, and clean CLI design with `argparse`.

## Why this project exists

Real-world Python tooling rarely starts with a GUI or web framework — it starts with scripts that do one job well from the terminal. This suite was built to practice exactly that: structured CLI design, persistent local data storage, and calling external APIs safely.

## Tools

### 1. Expense Tracker
Track expenses by category and date, stored locally in JSON.
```bash
python expense_tracker.py add --amount 500 --category food --date 2026-07-17
python expense_tracker.py list
python expense_tracker.py list --category food
```

### 2. Student Grade Manager
Add students and grades, generate simple reports (average, highest, lowest).
```bash
python grade_manager.py add-student --name "Ali"
python grade_manager.py add-grade --name "Ali" --subject "Math" --score 85
python grade_manager.py report --name "Ali"
```

### 3. Weather CLI
Fetches live weather data for any city using the OpenWeatherMap API.
```bash
python weather_cli.py --city Lahore
```

## How to run locally

```bash
git clone https://github.com/daniyal-devx/cli-tools-suite.git
cd cli-tools-suite
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

Create a `.env` file for the Weather CLI:
OPENWEATHER_API_KEY=your_key_here

## Technologies used

Python 3 · argparse · JSON · python-dotenv · requests

## What I learned

- Designing clean CLI interfaces with subcommands using `argparse`
- Persisting structured data locally with JSON serialization/deserialization
- Handling real API failures gracefully (rate limits, invalid input, missing keys)
- Keeping secrets out of source control with `.env` + `.gitignore`

## Project structure
cli-tools-suite/
├── expense_tracker.py
├── grade_manager.py
├── weather_cli.py
├── data/
│   ├── expenses.json
│   └── students.json
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
