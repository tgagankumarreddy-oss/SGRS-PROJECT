from student import get_student
from grievance import add_grievance, view_grievances, track_grievance
from admin import resolve_grievance
from analytics import show_report

def main():
    while True:
        print("\n1. Submit Grievance")
        print("2. View Grievances")
        print("3. Track Grievance")
        print("4. Resolve Grievance")
        print("5. Analytics")
        print("6. Exit")

        ch = input("Enter choice: ")

        if ch=='1':
            data = get_student()
            add_grievance(data)
        elif ch=='2':
            view_grievances()
        elif ch=='3':
            track_grievance()
        elif ch=='4':
            resolve_grievance()
        elif ch=='5':
            show_report()
        elif ch=='6':
            break
        else:
            print("Invalid choice")

main()
