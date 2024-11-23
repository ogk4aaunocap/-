money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

months = 0
budget = money_capital + salary
while budget - spend > 0:
    if spend > budget:
        break
    budget -= spend
    spend *= 1.05
    budget += salary
    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)
