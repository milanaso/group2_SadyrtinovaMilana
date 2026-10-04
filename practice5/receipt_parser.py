import re
import json
from pathlib import Path


def parse_receipt(filename="raw.txt"):
    text = Path(filename).read_text(encoding="utf-8")

    # Product blocks start with a number and a dot.
    product_pattern = re.compile(
        r"(?m)^[ \t]*(\d+)\.[ \t]*\n"
        r"(.*?)\n"
        r"[ \t]*([\d ]+,\d+)[ \t]*x[ \t]*([\d ]+,\d{2})[ \t]*\n"
        r"[ \t]*([\d ]+,\d{2})[ \t]*\n"
        r"[ \t]*Стоимость[ \t]*\n"
        r"[ \t]*([\d ]+,\d{2})",
        re.DOTALL
    )

    products = []

    for match in product_pattern.finditer(text):
        number, name, quantity, unit_price, line_price, cost = match.groups()

        def money(value):
            return float(value.replace(" ", "").replace(",", "."))

        def qty(value):
            return float(value.replace(" ", "").replace(",", "."))

        products.append({
            "number": int(number),
            "name": " ".join(name.split()),
            "quantity": qty(quantity),
            "unit_price": money(unit_price),
            "total": money(cost)
        })
    total_match = re.search(
        r"ИТОГО:\s*\n?\s*([\d ]+,\d{2})",
        text
    )

    card_match = re.search(
        r"Банковская карта:\s*\n?\s*([\d ]+,\d{2})",
        text
    )

    datetime_match = re.search(
        r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})",
        text
    )

    payment_method = "Банковская карта" if card_match else "Не найден"

    result = {
        "store": "ТОО EUROPHARMA",
        "city": "Астана",
        "receipt_number": (
            re.search(r"Чек №(\d+)", text).group(1)
            if re.search(r"Чек №(\d+)", text) else None
        ),
        "products": products,
        "product_count": len(products),
        "payment_method": payment_method,
        "paid_by_card": (
            float(card_match.group(1).replace(" ", "").replace(",", "."))
            if card_match else None
        ),
        "total": (
            float(total_match.group(1).replace(" ", "").replace(",", "."))
            if total_match else None
        ),
        "datetime": (
            f"{datetime_match.group(1)} {datetime_match.group(2)}"
            if datetime_match else None
        )
    }

    return result

if __name__ == "__main__":
    receipt = parse_receipt()

    print("=" * 60)
    print("RECEIPT INFORMATION")
    print("=" * 60)

    print(f"Store: {receipt['store']}")
    print(f"City: {receipt['city']}")
    print(f"Receipt number: {receipt['receipt_number']}")
    print(f"Date and time: {receipt['datetime']}")
    print(f"Payment method: {receipt['payment_method']}")
    print(f"Total: {receipt['total']:.2f}")
    print(f"Number of products: {receipt['product_count']}")

    print("\nPRODUCTS")
    print("-" * 60)

    for product in receipt["products"]:
        print(
            f"{product['number']:2}. "
            f"{product['name']} | "
            f"{product['quantity']} x "
            f"{product['unit_price']:.2f} = "
            f"{product['total']:.2f}"
        )

    print("\nJSON OUTPUT")
    print(json.dumps(receipt, ensure_ascii=False, indent=4))

