"""Reusable input validation helpers for the management system."""

import math
import re
from typing import Iterable, Optional, TypeVar

T = TypeVar("T")


def get_int(prompt: str, minimum: Optional[int] = None, maximum: Optional[int] = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Invalid whole number. Please try again.")
            continue
        if minimum is not None and value < minimum:
            print(f"Value must be at least {minimum}.")
            continue
        if maximum is not None and value > maximum:
            print(f"Value must be at most {maximum}.")
            continue
        return value


def get_float(
    prompt: str,
    minimum: Optional[float] = None,
    maximum: Optional[float] = None,
) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("Invalid number. Please try again.")
            continue
        if not math.isfinite(value):
            print("Enter a finite number. Please try again.")
            continue
        if minimum is not None and value < minimum:
            print(f"Value must be at least {minimum}.")
            continue
        if maximum is not None and value > maximum:
            print(f"Value must be at most {maximum}.")
            continue
        return value


def get_non_empty_text(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def get_name(prompt: str) -> str:
    while True:
        value = get_non_empty_text(prompt)
        if re.fullmatch(r"[A-Za-z ]{2,40}", value):
            return value
        print("Name must contain only letters and spaces and be 2-40 characters long.")


def get_choice(prompt: str, choices: Iterable[T]) -> T:
    options = list(choices)
    while True:
        value = input(prompt).strip()
        for option in options:
            if str(option).lower() == value.lower():
                return option
        print(f"Choose one of: {', '.join(map(str, options))}.")

