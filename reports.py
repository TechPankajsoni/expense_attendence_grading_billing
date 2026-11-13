"""Console report formatting functions."""


def print_expense_report(expenses: list[dict], summary: dict) -> None:
    print("\n--- EXPENSE REPORT ---")
    if not expenses:
        print("No expenses recorded.")
        return
    for expense in expenses:
        print(f"{expense['category']:<15} {expense['description']:<25} {expense['amount']:>10.2f}")
    print("Category totals:")
    for category, amount in summary.items():
        print(f"  {category:<15} {amount:>10.2f}")


def print_attendance_report(records: list[dict], summary: dict) -> None:
    print("\n--- ATTENDANCE REPORT ---")
    if not records:
        print("No attendance records recorded.")
        return
    for record in records:
        print(f"{record['roll_no']:<10} {record['name']:<20} {record['percentage']:>7.2f}%  {record['status']}")
    print(f"Average attendance: {summary['average_percentage']:.2f}%")


def print_grading_report(students: list[dict], summary: dict) -> None:
    print("\n--- GRADING REPORT ---")
    if not students:
        print("No grading records recorded.")
        return
    for student in students:
        if student["result"] is None:
            continue
        result = student["result"]
        print(f"{student['roll_no']:<10} {student['name']:<20} {result['average']:>7.2f}%  {result['grade']}  {result['result']}")
    print(f"Class average: {summary['average']:.2f}% | Passed: {summary['passed']} | Failed: {summary['failed']}")


def print_student_directory(students: list[dict]) -> None:
    print("\n--- REGISTERED STUDENTS / UNIQUE ROLL NUMBERS ---")
    if not students:
        print("No students registered. Add students through Grading System.")
        return
    print(f"{'Roll No.':<15} {'Student Name'}")
    print("-" * 35)
    for student in students:
        print(f"{student['roll_no']:<15} {student['name']}")


def print_invoice(invoice: dict) -> None:
    print("\n--- INVOICE ---")
    print(f"Bill number: {invoice['bill_no']}")
    print(f"Customer:    {invoice['customer_name']}")
    for item in invoice["items"]:
        total = item["unit_price"] * item["quantity"]
        print(f"{item['name']:<20} {item['quantity']:>3} x {item['unit_price']:>8.2f} = {total:>10.2f}")
    print(f"Subtotal:       {invoice['subtotal']:>10.2f}")
    print(f"Discount:       {invoice['discount']:>10.2f}")
    print(f"Tax:            {invoice['tax']:>10.2f}")
    print(f"GRAND TOTAL:    {invoice['grand_total']:>10.2f}")
