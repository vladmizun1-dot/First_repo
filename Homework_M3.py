from datetime import datetime

def get_days_from_today(date):
    try:
        converted_date = datetime.strptime(date, "%Y-%m-%d").date()    # перетворення рядка у об'єкт datatime.
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")    # обробка помилки, якщо формат дати неправильний.
    date_today = datetime.today().date()     # отримання поточної дати.
    delta = date_today - converted_date     # обчислення різниці між поточною датою та введеною датою.
    return delta.days     # повернення кількості днів.

print(get_days_from_today("2020-10-09"))

    
    


