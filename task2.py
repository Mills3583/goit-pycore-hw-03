import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка коректності вхідних даних
    if not (1 <= min <= quantity <= max <= 1000):
        return []
    
    # Створення списку чисел у заданому діапазоні
    numbers_range = range(min, max + 1)
    
    # Генерація унікальних випадкових чисел
    # random.sample гарантує унікальність
    selected_numbers = random.sample(numbers_range, quantity)
    
    # Повертаємо відсортований список
    return sorted(selected_numbers)

# Приклад використання:
lottery_numbers = get_numbers_ticket(1, 49, 6)

print("Ваші лотерейні числа:", lottery_numbers)