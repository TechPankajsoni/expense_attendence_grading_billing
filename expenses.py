"""Expense tracking and summaries."""

from collections import defaultdict
from typing import Dict, List


def add_expense(expenses: List[dict], description: str, category: str, amount: float) -> dict:
    expense = {"description": description, "category": category, "amount": round(amount, 2)}
    expenses.append(expense)
    return expense


def expense_summary(expenses: List[dict]) -> Dict[str, float]:
    totals = defaultdict(float)
    for expense in expenses:
        totals[expense["category"]] += expense["amount"]
    return {category: round(amount, 2) for category, amount in totals.items()}


def highest_lowest_expense(expenses: List[dict]):
    if not expenses:
        return None, None
    return min(expenses, key=lambda item: item["amount"]), max(
        expenses, key=lambda item: item["amount"]
    )

