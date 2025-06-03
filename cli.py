import click
from datetime import datetime
try:
    from .database import get_session, init_db
    from .models import User, Mood, Activity
except ImportError:
    from database import get_session, init_db
    from models import User, Mood, Activity

def print_menu():
    print("\n" + "="*50)
    print("🌟 Welcome to Mental Health Tracker! 🌟")
    print("Your companion for mental wellness and self-care")
    print("="*50)
    print("\n📋 Main Menu")
    print("1. Manage Users")
    print("2. Track Moods")
    print("3. Track Activities")
    print("4. View Complete History")
    print("0. Exit")

def add_user(session):
    name = input("Enter name: ")
    email = input("Enter email: ")
    user = User(name=name, email=email)
    session.add(user)
    try:
        session.commit()
        print(f"\n✅ Successfully added user: {name}")
    except Exception as e:
        session.rollback()
        print(f"\n❌ Error adding user: {str(e)}")

def log_mood(session):
    email = input("Enter user email: ")
    user = session.query(User).filter_by(email=email).first()
    if not user:
        print("\n❌ User not found!")
        return
    
    mood = input("Enter mood (e.g., Happy, Sad, Anxious): ")
    journal = input("Enter journal entry (optional): ")
    mood_entry = Mood(user_id=user.id, mood_type=mood, journal_entry=journal)
    session.add(mood_entry)
    try:
        session.commit()
        print(f"\n✅ Successfully logged mood for {user.name}")
    except Exception as e:
        session.rollback()
        print(f"\n❌ Error logging mood: {str(e)}")

def log_activity(session):
    email = input("Enter user email: ")
    user = session.query(User).filter_by(email=email).first()
    if not user:
        print("\n❌ User not found!")
        return
    
    activity = input("Enter activity type (e.g., Meditation, Exercise): ")
    duration = input("Enter duration (minutes): ")
    try:
        duration = int(duration)
        activity_entry = Activity(user_id=user.id, activity_type=activity, duration_minutes=duration)
        session.add(activity_entry)
        session.commit()
        print(f"\n✅ Successfully logged activity for {user.name}")
    except ValueError:
        print("\n❌ Duration must be a number!")
    except Exception as e:
        session.rollback()
        print(f"\n❌ Error logging activity: {str(e)}")

def view_history(session):
    email = input("Enter user email: ")
    user = session.query(User).filter_by(email=email).first()
    if not user:
        print("\n❌ User not found!")
        return

    print(f"\n📊 History for {user.name}:")
    
    print("\n😊 Mood History:")
    moods = session.query(Mood).filter_by(user_id=user.id).order_by(Mood.timestamp.desc()).all()
    if moods:
        for mood in moods:
            print(f"[{mood.timestamp}] {mood.mood_type}")
            if mood.journal_entry:
                print(f"Journal: {mood.journal_entry}")
    else:
        print("No mood entries found.")
    
    print("\n⭐ Activity History:")
    activities = session.query(Activity).filter_by(user_id=user.id).order_by(Activity.timestamp.desc()).all()
    if activities:
        for activity in activities:
            print(f"[{activity.timestamp}] {activity.activity_type} ({activity.duration_minutes} minutes)")
    else:
        print("No activity entries found.")

def main():
    # Initialize database
    init_db()
    session = get_session()

    while True:
        print_menu()
        try:
            choice = input("\nEnter your choice: ")
            
            if choice == "1":
                print("\n🧑 User Management")
                add_user(session)
            
            elif choice == "2":
                print("\n😊 Mood Management")
                log_mood(session)
            
            elif choice == "3":
                print("\n⭐ Activity Management")
                log_activity(session)
            
            elif choice == "4":
                print("\n📊 View History")
                view_history(session)
            
            elif choice == "0":
                print("\nThank you for using Mental Health Tracker! Take care! 🌈")
                break
            
            else:
                print("\n❌ Invalid choice! Please try again.")
            
            input("\nPress Enter to continue...")
            
        except KeyboardInterrupt:
            print("\nThank you for using Mental Health Tracker! Take care! 🌈")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {str(e)}")
            input("\nPress Enter to continue...")

    session.close()

if __name__ == '__main__':
    main()
