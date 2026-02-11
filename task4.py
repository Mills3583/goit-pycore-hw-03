from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    today = datetime.today().date()
    upcoming_birthdays: list[dict[str, str]] = []

    for user in users:
        # Перетворюємо рядок дати у об'єкт date
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Визначаємо дату народження у поточному році
        birthday_this_year = birthday.replace(year=today.year)
        
        # Якщо день народження вже минув у цьому році, перевіряємо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Рахуємо різницю в днях
        days_until: int = (birthday_this_year - today).days
        
        # Перевіряємо, чи день народження протягом наступних 7 днів (включно з сьогодні)
        if 0 <= days_until <= 7:
            congratulation_date = birthday_this_year
            
            # Якщо припадає на вихідний (5 - субота, 6 - неділя)
            weekday = congratulation_date.weekday()
            if weekday == 5:  # Субота
                congratulation_date += timedelta(days=2)
            elif weekday == 6:  # Неділя
                congratulation_date += timedelta(days=1)
                
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
            
    return upcoming_birthdays


if __name__ == "__main__":
    users_list: list[dict[str, str]] = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Anton Kashuba", "birthday": "1993.08.16"},
        {"name": "Birthday Boy", "birthday": "1995.02.16"} # Тестова дата
    ]

    upcoming: list = get_upcoming_birthdays(users_list)
    print(f"Список привітань на цьому тижні: {upcoming}")