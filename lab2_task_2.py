salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

i = 1
money_capital = 0
while i <= 10:
    dolg = spend - salary
    money_capital += dolg
    spend *= (1 + increase)
    i += 1

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))