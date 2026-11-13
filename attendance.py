"""Attendance calculations and status classification."""


def attendance_percentage(total_days: int, present_days: int) -> float:
    if total_days <= 0:
        raise ValueError("Total working days must be greater than zero.")
    if present_days < 0 or present_days > total_days:
        raise ValueError("Present days must be between zero and total days.")
    return round(present_days / total_days * 100, 2)


def attendance_status(percentage: float) -> str:
    if percentage >= 75:
        return "Eligible"
    if percentage >= 60:
        return "Warning"
    return "Shortage"


def attendance_summary(records: list[dict]) -> dict:
    if not records:
        return {"total_people": 0, "average_percentage": 0.0, "eligible": 0, "warning": 0, "shortage": 0}
    percentages = [record["percentage"] for record in records]
    return {
        "total_people": len(records),
        "average_percentage": round(sum(percentages) / len(percentages), 2),
        "eligible": sum(record["status"] == "Eligible" for record in records),
        "warning": sum(record["status"] == "Warning" for record in records),
        "shortage": sum(record["status"] == "Shortage" for record in records),
    }


def add_attendance(records: list[dict], roll_no: str, name: str, total_days: int, present_days: int) -> dict:
    percentage = attendance_percentage(total_days, present_days)
    record = {
        "roll_no": roll_no.strip().upper(),
        "name": name.strip(),
        "total_days": total_days,
        "present_days": present_days,
        "percentage": percentage,
        "status": attendance_status(percentage),
    }
    records.append(record)
    return record


def get_attendance(records: list[dict], roll_no: str) -> dict | None:
    normalized_roll_no = roll_no.strip().upper()
    return next((record for record in records if record["roll_no"] == normalized_roll_no), None)
