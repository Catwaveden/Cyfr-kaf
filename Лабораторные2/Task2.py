salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = salary - spend
for i in range(months-1):
    spend = (spend * (1 + increase))
    money_capital += salary - spend
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(-money_capital,2))
