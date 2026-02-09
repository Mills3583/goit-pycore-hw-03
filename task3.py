import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та '+'
    # [^0-9+] означає "все, що не є цифрою або плюсом"
    clean_number = re.sub(r'[^0-9+]', '', phone_number.strip())
    
    # Якщо номер починається з '+', перевіряємо чи він повний
    if clean_number.startswith('+'):
        return clean_number
    # Якщо номер починається з '380', додаємо тільки '+'
    elif clean_number.startswith('380'):
        return '+' + clean_number
    # В усіх інших випадках додаємо '+38'
    else:
        return '+38' + clean_number

# Приклад використання:
raw_numbers = [
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

sanitized_numbers = []

for num in raw_numbers:
    sanitized_numbers.append(normalize_phone(num))

print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

# робоча, але по моєму менш читабельна версія коду
# sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
# print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)