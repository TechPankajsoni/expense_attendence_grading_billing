# Expense, Attendance, Grading & Billing Management System

A menu-driven Python console application for recording expenses, calculating attendance, grading students, generating invoices, and displaying reports.

## Requirements

- Python 3.8 or newer
- No third-party packages

## Run

From this directory:

```text
python main.py
```

The program displays a numbered menu. Invalid input is rejected with a clear message and the user is prompted again.
This is a login-free console application: users can directly select and complete
the expense, attendance, grading, billing, or report operation from the menu.
The startup screen displays the project owner's name and roll number for project
identification. The application starts with empty records; users enter their own
data rather than using values copied from the requirements examples.

## Modules

- `main.py` - entry point, main menu, and input flow
- `validators.py` - reusable validation helpers
- `expenses.py` - expense records and category summaries
- `attendance.py` - percentages and eligibility status
- `grading.py` - grades, pass/fail, and class summary
- `billing.py` - invoice, discount slabs, and 18% tax
- `reports.py` - aligned console report output
- `tests/test_cases.md` - manual test log based on the client test cases

## Student records

The roll number is the unique student key. Use the individual student report
prompt inside View Reports to retrieve a student's name, marks result, and
attendance by roll number. New grading and attendance records require a roll
number. View Reports also displays the complete registered-student directory
with every unique roll number.

## Business rules

- Attendance: `>=75%` Eligible, `60-74.99%` Warning, `<60%` Shortage.
- A student fails if any subject mark is below 35.
- Grade thresholds follow the client specification from A+ through F.
- Discounts are 0% below 1,000, 5% from 1,000, 10% from 5,000, and 15% from 10,000.
- Tax is 18% of the amount after discount.
- Billing asks for a customer name and generates an automatic invoice number.
