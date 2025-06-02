import click
from datetime import datetime
from .database import get_session, init_db
from .models import User, Mood, Activity

@click.group()
def cli():
    """Mental Health Tracker CLI"""
    pass

@cli.command()
@click.option('--name', prompt='Enter name', help='The name of the user')
@click.option('--email', prompt='Enter email', help='The email of the user')
def add_user(name, email):
    """Add a new user to the system."""
    session = get_session()
    user = User(name=name, email=email)
    session.add(user)
    try:
        session.commit()
        click.echo(f"Successfully added user: {name}")
    except Exception as e:
        session.rollback()
        click.echo(f"Error adding user: {str(e)}")
    finally:
        session.close()

@cli.command()
@click.option('--email', prompt='Enter user email', help='The email of the user')
@click.option('--mood', prompt='Enter mood', help='The mood to log (e.g., Happy, Sad)')
@click.option('--journal', prompt='Enter journal entry (optional)', default='', help='Optional journal entry')
def log_mood(email, mood, journal):
    """Log a mood entry for a user."""
    session = get_session()
    user = session.query(User).filter_by(email=email).first()
    if not user:
        click.echo("User not found!")
        return
    
    mood_entry = Mood(user_id=user.id, mood_type=mood, journal_entry=journal)
    session.add(mood_entry)
    try:
        session.commit()
        click.echo(f"Successfully logged mood for {user.name}")
    except Exception as e:
        session.rollback()
        click.echo(f"Error logging mood: {str(e)}")
    finally:
        session.close()

@cli.command()
@click.option('--email', prompt='Enter user email', help='The email of the user')
@click.option('--activity', prompt='Enter activity', help='The activity type (e.g., Meditation, Exercise)')
@click.option('--duration', prompt='Enter duration (minutes)', type=int, help='Duration in minutes')
def log_activity(email, activity, duration):
    """Log a self-care activity for a user."""
    session = get_session()
    user = session.query(User).filter_by(email=email).first()
    if not user:
        click.echo("User not found!")
        return
    
    activity_entry = Activity(user_id=user.id, activity_type=activity, duration_minutes=duration)
    session.add(activity_entry)
    try:
        session.commit()
        click.echo(f"Successfully logged activity for {user.name}")
    except Exception as e:
        session.rollback()
        click.echo(f"Error logging activity: {str(e)}")
    finally:
        session.close()

@cli.command()
@click.option('--email', prompt='Enter user email', help='The email of the user')
def view_history(email):
    """View mood and activity history for a user."""
    session = get_session()
    user = session.query(User).filter_by(email=email).first()
    if not user:
        click.echo("User not found!")
        return

    click.echo(f"\nHistory for {user.name}:")
    
    click.echo("\nMood History:")
    moods = session.query(Mood).filter_by(user_id=user.id).order_by(Mood.timestamp.desc()).all()
    for mood in moods:
        click.echo(f"[{mood.timestamp}] {mood.mood_type}")
        if mood.journal_entry:
            click.echo(f"Journal: {mood.journal_entry}")
    
    click.echo("\nActivity History:")
    activities = session.query(Activity).filter_by(user_id=user.id).order_by(Activity.timestamp.desc()).all()
    for activity in activities:
        click.echo(f"[{activity.timestamp}] {activity.activity_type} ({activity.duration_minutes} minutes)")
    
    session.close()

@cli.command()
def init():
    """Initialize the database."""
    init_db()
    click.echo("Database initialized successfully!")
