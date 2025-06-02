# Mental Health Tracker

A command-line application for tracking your mental health, moods, and self-care activities.

## Features

- Add users with name and email
- Log daily moods with optional journal entries
- Track self-care activities and their duration
- View history of moods and activities

## Installation

1. Make sure you have Python 3.12 installed
2. Install pipenv if you haven't already:
   ```bash
   pip install pipenv
   ```
3. Install dependencies:
   ```bash
   pipenv install
   ```

## Getting Started

1. Initialize the database:
   ```bash
   pipenv run python run.py init
   ```

2. Add a new user:
   ```bash
   pipenv run python run.py add-user
   ```

3. Log a mood:
   ```bash
   pipenv run python run.py log-mood
   ```

4. Log an activity:
   ```bash
   pipenv run python run.py log-activity
   ```

5. View your history:
   ```bash
   pipenv run python run.py view-history
   ```

## Commands

- `init`: Initialize the database
- `add-user`: Add a new user with name and email
- `log-mood`: Log a mood entry with optional journal
- `log-activity`: Log a self-care activity with duration
- `view-history`: View mood and activity history for a user

Each command will prompt you for the necessary information, or you can provide it directly using command-line options. For help with any command, use:
```bash
pipenv run python run.py COMMAND --help
``` 