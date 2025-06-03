from mental_health_tracker.cli import cli
import click

def user_management():
    while True:
        print("\n🧑 User Management")
        print("1. Add New User")
        print("2. View All Users")
        print("0. Back")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            cli.main(["add-user", "--name", name, "--email", email])
        elif choice == "2":
            print("\nFeature coming soon: View All Users")
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

def mood_management():
    while True:
        print("\n😊 Mood Management")
        print("1. Log New Mood")
        print("2. View Mood History")
        print("0. Back")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            email = input("Enter user email: ")
            mood = input("Enter mood (e.g., Happy, Sad, Anxious): ")
            journal = input("Enter journal entry (optional): ")
            cli.main(["log-mood", "--email", email, "--mood", mood, "--journal", journal])
        elif choice == "2":
            email = input("Enter user email to view history: ")
            cli.main(["view-history", "--email", email])
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

def activity_management():
    while True:
        print("\n⭐ Activity Management")
        print("1. Log New Activity")
        print("2. View Activity History")
        print("0. Back")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            email = input("Enter user email: ")
            activity = input("Enter activity type (e.g., Meditation, Exercise): ")
            duration = input("Enter duration (minutes): ")
            cli.main(["log-activity", "--email", email, "--activity", activity, "--duration", duration])
        elif choice == "2":
            email = input("Enter user email to view history: ")
            cli.main(["view-history", "--email", email])
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

def main_menu():
    print("\n" + "="*50)
    print("🌟 Welcome to Mental Health Tracker! 🌟")
    print("Your companion for mental wellness and self-care")
    print("="*50)
    
    # Initialize database if not exists
    try:
        cli.main(["init"])
    except Exception as e:
        pass  # Database might already be initialized

    while True:
        print("\n📋 Main Menu")
        print("1. Manage Users")
        print("2. Track Moods")
        print("3. Track Activities")
        print("4. View Complete History")
        print("0. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            user_management()
        elif choice == "2":
            mood_management()
        elif choice == "3":
            activity_management()
        elif choice == "4":
            email = input("Enter user email to view complete history: ")
            cli.main(["view-history", "--email", email])
        elif choice == "0":
            print("\nThank you for using Mental Health Tracker! Take care! 🌈")
            break
        else:
            print("Invalid choice!")

if __name__ == '__main__':
    main_menu()
