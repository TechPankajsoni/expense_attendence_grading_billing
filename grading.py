"""Marks, grades, pass/fail, and class summaries."""


GRADE_SCALE = (
    (90, "A+", "Outstanding"),
    (80, "A", "Excellent"),
    (70, "B", "Very Good"),
    (60, "C", "Good"),
    (50, "D", "Satisfactory"),
    (35, "E", "Pass"),
    (0, "F", "Fail"),
)


def add_student(students: list[dict], roll_no: str, name: str, marks: list[float]) -> dict:
    """Add a student keyed by a unique roll number."""
    normalized_roll_no = roll_no.strip().upper()
    if not normalized_roll_no:
        raise ValueError("Roll number cannot be empty.")
    existing = get_student(students, normalized_roll_no)
    if existing is not None:
        if existing["result"] is not None:
            raise ValueError(f"Roll number {normalized_roll_no} already has marks.")
        existing["name"] = name.strip()
        existing["result"] = calculate_grade(marks)
        return existing
    student = {
        "roll_no": normalized_roll_no,
        "name": name.strip(),
        "result": calculate_grade(marks),
    }
    students.append(student)
    return student


def get_student(students: list[dict], roll_no: str) -> dict | None:
    normalized_roll_no = roll_no.strip().upper()
    return next((student for student in students if student["roll_no"] == normalized_roll_no), None)


def calculate_grade(marks: list[float]) -> dict:
    if not marks:
        raise ValueError("At least one subject mark is required.")
    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Marks must be between 0 and 100.")
    total = round(sum(marks), 2)
    average = round(total / len(marks), 2)
    grade, remark = next((grade, remark) for threshold, grade, remark in GRADE_SCALE if average >= threshold)
    passed = all(mark >= 35 for mark in marks) and grade != "F"
    return {"total": total, "average": average, "grade": grade, "remark": remark, "result": "PASS" if passed else "FAIL"}


def class_summary(students: list[dict]) -> dict:
    graded_students = [student for student in students if student["result"] is not None]
    if not graded_students:
        return {"count": 0, "average": 0.0, "highest": 0.0, "lowest": 0.0, "passed": 0, "failed": 0}
    averages = [student["result"]["average"] for student in graded_students]
    return {
        "count": len(graded_students),
        "average": round(sum(averages) / len(averages), 2),
        "highest": max(averages),
        "lowest": min(averages),
        "passed": sum(student["result"]["result"] == "PASS" for student in graded_students),
        "failed": sum(student["result"]["result"] == "FAIL" for student in graded_students),
    }
