

# Mental Health Tracker

A command-line application to help you track your mental health by logging moods, journaling feelings, and recording self-care activities.

## Features

* Add users with name and email
* Log daily moods with optional journal entries
* Track self-care activities and their duration
* View complete history of moods and activities for any user

## Installation

1. Ensure you have Python 3.12 installed.
2. Install pipenv if you don't have it:

   ```bash
   pip install pipenv
   ```
3. Install project dependencies:

   ```bash
   pipenv install
   ```

## Usage

Start the application by running the CLI:

```bash
pipenv run python cli.py
```

You will see a menu with options to:

* Manage Users
* Track Moods
* Track Activities
* View Complete History
* Exit the program

Follow the prompts to enter user emails, moods, activities, and journal entries. The program validates users and provides feedback for successful operations.

## How It Works

* Users can be created by entering a name and email.
* Mood entries include the mood type and an optional journal note.
* Activities include the type of activity and duration in minutes.
* Viewing history shows all logged moods and activities with timestamps for the selected user.

## Technical Details

* The app uses SQLAlchemy ORM to manage a SQLite database with three related tables: Users, Moods, and Activities.
* The project follows a proper package structure and uses Pipenv to manage dependencies.
* Input validation and clear prompts ensure smooth interaction with the CLI.
* Python data structures like lists and dictionaries are used to efficiently manage and display data.

## Future Improvements

* Add filtering and searching in history
* Implement data export to CSV or JSON
* Add authentication for user privacy
