"""Invoice calculation using the specification's discount slabs and tax."""

from itertools import count


DISCOUNT_SLABS = ((10000, 0.15), (5000, 0.10), (1000, 0.05), (0, 0.0))
TAX_RATE = 0.18
_BILL_NUMBERS = count(1)


def next_bill_number() -> str:
    return f"INV-{next(_BILL_NUMBERS):04d}"


def discount_rate(subtotal: float) -> float:
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative.")
    for threshold, rate in DISCOUNT_SLABS:
        if subtotal >= threshold:
            return rate
    return 0.0


def calculate_invoice(items: list[dict], customer_name: str) -> dict:
    if not items:
        raise ValueError("At least one invoice item is required.")
    if not customer_name.strip():
        raise ValueError("Customer name cannot be empty.")
    subtotal = round(sum(item["unit_price"] * item["quantity"] for item in items), 2)
    rate = discount_rate(subtotal)
    discount = round(subtotal * rate, 2)
    taxable_amount = round(subtotal - discount, 2)
    tax = round(taxable_amount * TAX_RATE, 2)
    grand_total = round(taxable_amount + tax, 2)
    return {
        "bill_no": next_bill_number(),
        "customer_name": customer_name.strip(),
        "items": items,
        "subtotal": subtotal,
        "discount_rate": rate,
        "discount": discount,
        "tax_rate": TAX_RATE,
        "tax": tax,
        "grand_total": grand_total,
    }

