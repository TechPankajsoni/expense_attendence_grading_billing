# Test Log

| ID | Module | Input | Expected result | Type |
|---|---|---|---|---|
| TC-01 | Menu | `1` | Opens Expense module | Valid |
| TC-02 | Menu | `abc` | Error message and re-prompt | Invalid |
| TC-03 | Expense | Amount `250.50` | Added successfully | Valid |
| TC-04 | Expense | Amount `-10` | Rejected and re-prompted | Invalid |
| TC-05 | Attendance | Total `40`, present `38` | `95.00%`, Eligible | Valid |
| TC-06 | Attendance | Total `40`, present `20` | `50.00%`, Shortage | Boundary |
| TC-07 | Grading | Marks `90, 90, 90` | A+, PASS | Valid |
| TC-08 | Grading | Mark `101` | Rejected | Invalid |
| TC-09 | Billing | Subtotal `500` | No discount, tax calculated | Valid |
| TC-10 | Billing | Subtotal `1,000` | 5% discount | Boundary |
| TC-11 | Billing | Quantity `0` | Rejected | Invalid |
| TC-12 | Reports | Empty records | Clear no-data messages | Edge case |
| TC-13 | Student lookup | Roll `ST001` | Returns Asha's grading and attendance | Valid |
| TC-14 | Student lookup | Roll `ST999` | Clear not-found message | Invalid |
| TC-15 | Student key | Duplicate roll number | Duplicate roll number rejected | Invalid |
| TC-16 | Startup | Run `python main.py` | Owner details and login-free status displayed | Valid |
| TC-17 | Any input | Invalid value | Error message and re-prompt until valid | Invalid |
| TC-18 | Attendance | Unknown roll number | Rejected and re-prompted | Invalid |
| TC-19 | Billing | Customer name and item | Invoice number and customer displayed | Valid |
| TC-20 | Reports | Registered students | Every student roll number displayed once | Valid |

## Manual verification

Run `python -m unittest discover` from the project directory after adding automated tests.
