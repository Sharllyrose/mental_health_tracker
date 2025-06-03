from mental_health_tracker.cli import cli

def print_menu():
    print("\n📋 Main Menu")
    print("1. Manage Users")
    print("2. Track Moods")
    print("3. Track Activities")
    print("4. View Complete History")
    print("0. Exit")

def main():
    print("\n" + "="*50)
    print("🌟 Welcome to Mental Health Tracker! 🌟")
    print("Your companion for mental wellness and self-care")
    print("="*50)
    
    # Initialize database
    try:
        cli.main(["init"])
    except Exception as e:
        pass

    while True:
        print_menu()
        try:
            choice = input("Enter your choice: ")
            
            if choice == "1":
                print("\n🧑 User Management")
                name = input("Enter name: ")
                email = input("Enter email: ")
                cli.main(["add-user", "--name", name, "--email", email])
            
            elif choice == "2":
                print("\n😊 Mood Management")
                email = input("Enter user email: ")
                mood = input("Enter mood (e.g., Happy, Sad, Anxious): ")
                journal = input("Enter journal entry (optional): ")
                cli.main(["log-mood", "--email", email, "--mood", mood, "--journal", journal])
            
            elif choice == "3":
                print("\n⭐ Activity Management")
                email = input("Enter user email: ")
                activity = input("Enter activity type (e.g., Meditation, Exercise): ")
                duration = input("Enter duration (minutes): ")
                cli.main(["log-activity", "--email", email, "--activity", activity, "--duration", duration])
            
            elif choice == "4":
                email = input("Enter user email to view history: ")
                cli.main(["view-history", "--email", email])
            
            elif choice == "0":
                print("\nThank you for using Mental Health Tracker! Take care! 🌈")
                break
            
            else:
                print("Invalid choice! Please try again.")
            
            input("\nPress Enter to continue...")
            
        except KeyboardInterrupt:
            print("\nThank you for using Mental Health Tracker! Take care! 🌈")
            break
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            input("\nPress Enter to continue...")

if __name__ == '__main__':
    main()
