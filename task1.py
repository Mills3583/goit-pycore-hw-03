from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворюємо рядок у об'єкт datetime
        target_date = datetime.strptime(date, '%Y-%m-%d').date()

        # Отримуємо поточну дату (без часу)
        today = datetime.today().date('2021-05-05')
        
        # Розраховуємо різницю
        delta = target_date - today
        
        # Повертаємо кількість днів як ціле число
        return delta.days
    
    except ValueError as e:
        # print(f"Неправильний формат дати. Використовуйте РРРР-ММ-ДД. {e}")
        return f"Неправильний формат дати. Використовуйте РРРР-ММ-ДД. {e}"
    
    
print(get_days_from_today('2021-10-09'))