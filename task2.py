import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    # Перевірка коректності вхідних даних
    if not (1 <= min <= max <= 1000) or not (0 < quantity <= (max - min + 1)):
        return []
    
    numbers: list[int] = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)


if __name__ == "__main__":
    # Приклад використання:
    lottery_numbers: list[str] = get_numbers_ticket(1, 59, 7)
    print("Ваші лотерейні числа:", lottery_numbers)