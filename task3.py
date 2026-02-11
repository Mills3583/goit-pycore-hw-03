import re


def normalize_phone(phone_number: str) -> str:
    # Видаляємо всі символи, крім цифр та '+'
    # [^0-9+] означає "все, що не є цифрою або плюсом"
    clean_number: str = re.sub(r'[^0-9+]', '', phone_number.strip())
    
    # Якщо номер починається з '+', перевіряємо чи він повний
    if clean_number.startswith('+'):
        return clean_number
    # Якщо номер починається з '380', додаємо тільки '+'
    elif clean_number.startswith('380'):
        return '+' + clean_number
    # В усіх інших випадках додаємо '+38'
    else:
        return '+38' + clean_number


if __name__ == "__main__":
    # Тестові дані
    raw_numbers: list[str] = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers: list[str] = [normalize_phone(num) for num in raw_numbers]
    print(f"Нормалізовані номери телефонів для SMS-розсилки: {sanitized_numbers}")