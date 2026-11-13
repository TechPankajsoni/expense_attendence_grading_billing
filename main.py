"""Entry point and numbered console menu."""

from attendance import add_attendance, attendance_summary, get_attendance
from billing import calculate_invoice
from expenses import add_expense, expense_summary, highest_lowest_expense
from grading import add_student, class_summary, get_student
from reports import (
    print_attendance_report,
    print_expense_report,
    print_grading_report,
    print_invoice,
    print_student_directory,
)
from validators import get_choice, get_float, get_int, get_name, get_non_empty_text


PROJECT_OWNER_NAME = "PANKAJ SONI"
PROJECT_OWNER_ROLL_NO = "2601940058"


def display_project_owner() -> None:
    print("=" * 56)
    print("EXPENSE, ATTENDANCE, GRADING & BILLING MANAGEMENT SYSTEM")
    print(f"MY NAME    : {PROJECT_OWNER_NAME}")
    print(f"MY ROLL NO.: {PROJECT_OWNER_ROLL_NO}")
    print("LOGIN      : NOT REQUIRED")
    print("=" * 56)


def expense_menu(expenses: list[dict]) -> None:
    description = get_non_empty_text("Description: ")
    category = get_choice(
        "Category (Food/Travel/Utilities/Stationery/Other): ",
        ("Food", "Travel", "Utilities", "Stationery", "Other"),
    )
    amount = get_float("Amount: ", 0.01)
    add_expense(expenses, description, category, amount)
    print("Expense added successfully.")


def attendance_menu(records: list[dict], students: list[dict]) -> None:
    while True:
        roll_no = get_non_empty_text("Student roll number: ").upper()
        student = get_student(students, roll_no)
        if student is not None:
            break
        print("Roll number not registered. Enter the student's name to register it.")
        name = get_name("Student name: ")
        student = {"roll_no": roll_no, "name": name, "result": None}
        students.append(student)
        break
    name = student["name"]
    total_days = get_int("Total working days: ", 1)
    present_days = get_int("Days present: ", 0, total_days)
    add_attendance(records, roll_no, name, total_days, present_days)
    print("Attendance recorded successfully.")


def grading_menu(students: list[dict]) -> None:
    while True:
        roll_no = get_non_empty_text("Student roll number: ").upper()
        existing = get_student(students, roll_no)
        if existing is None or existing["result"] is None:
            break
        print("That roll number already has marks. Enter a different roll number.")
    name = get_name("Student name: ")
    subject_count = get_int("Number of subjects: ", 1)
    marks = [get_float(f"Marks {index + 1}: ", 0, 100) for index in range(subject_count)]
    try:
        add_student(students, roll_no, name, marks)
    except ValueError as error:
        print(error)
        return
    print("Marks recorded successfully.")


def billing_menu() -> None:
    customer_name = get_name("Customer name: ")
    items = []
    item_count = get_int("Number of items: ", 1)
    for _ in range(item_count):
        name = get_non_empty_text("Item name: ")
        unit_price = get_float("Unit price: ", 0.01)
        quantity = get_int("Quantity: ", 1)
        items.append({"name": name, "unit_price": unit_price, "quantity": quantity})
    print_invoice(calculate_invoice(items, customer_name))


def display_menu() -> None:
    print("\n==============================================")
    print("EXPENSE | ATTENDANCE | GRADING | BILLING")
    print("==============================================")
    print("1. Add Expense")
    print("2. Attendance Management")
    print("3. Grading System")
    print("4. Billing System")
    print("5. View Reports")
    print("6. Exit")


def student_lookup_menu(students: list[dict], attendance: list[dict], roll_no: str) -> None:
    student = get_student(students, roll_no)
    attendance_record = get_attendance(attendance, roll_no)
    if student is None and attendance_record is None:
        print(f"No student data found for roll number {roll_no.upper()}.")
        return
    print("\n--- STUDENT DATA ---")
    if student:
        result = student["result"]
        print(f"Roll number: {student['roll_no']}")
        print(f"Name: {student['name']}")
        print(f"Average: {result['average']:.2f}%")
        print(f"Grade: {result['grade']} ({result['remark']})")
        print(f"Result: {result['result']}")
    if attendance_record:
        print(f"Attendance: {attendance_record['percentage']:.2f}% ({attendance_record['status']})")


def reports_menu(expenses: list[dict], attendance: list[dict], students: list[dict]) -> None:
    print_expense_report(expenses, expense_summary(expenses))
    print_attendance_report(attendance, attendance_summary(attendance))
    print_grading_report(students, class_summary(students))
    print_student_directory(students)
    lowest, highest = highest_lowest_expense(expenses)
    if lowest and highest:
        print(f"Lowest expense: {lowest['description']} ({lowest['amount']:.2f})")
        print(f"Highest expense: {highest['description']} ({highest['amount']:.2f})")
    roll_no = input("\nEnter a roll number for an individual student report, or press Enter to return: ").strip()
    if roll_no:
        student_lookup_menu(students, attendance, roll_no)


def main() -> None:
    display_project_owner()
    expenses, attendance, students = [], [], []
    while True:
        display_menu()
        choice = get_int("Enter your choice (1-6): ", 1, 6)
        if choice == 1:
            expense_menu(expenses)
        elif choice == 2:
            attendance_menu(attendance, students)
        elif choice == 3:
            grading_menu(students)
        elif choice == 4:
            billing_menu()
        elif choice == 5:
            reports_menu(expenses, attendance, students)
        else:
            print("Thank you for using the system. Goodbye!")
            return


if __name__ == "__main__":
    main()
