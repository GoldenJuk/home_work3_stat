# Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1,
# для второй - 0.2, для третьей - 0.25. Какова вероятность того, что в первый месяц выйдут из строя:
# а). все детали
# б). только две детали
# в). хотя бы одна деталь
# г). от одной до двух деталей?


details = 3
probability_first = 0.1
probability_second = 0.2
probability_third = 0.25

# а). все детали

print(f'Вероятность того, что в первый месяц выйдут из строя все детали = '
      f'{round((probability_first * probability_second * probability_third) * 100, 2)} %')

# б). только две детали

two_breakdown = round((probability_first * probability_second * (1 - probability_third) +
                       probability_first * (1 - probability_second) * probability_third +
                       (1 - probability_first) * probability_second * probability_third) * 100, 2)

print(f'Вероятность того, что в первый месяц выйдут из строя только две детали = {two_breakdown} %')

# в). хотя бы одна деталь. Находим вероятность того, что ни одна деталь не выйдет из строя,
#                          затем полученное значение вычтем из единицы

p_negative = round((1 - probability_first) * (1 - probability_second) * (1 - probability_third), 2)

print(f'Вероятность того, что в первый месяц выйдет из строя хотя бы одна деталь  = {(1 - p_negative) * 100} %')

# г). от одной до двух деталей?

one_breakdown = round((probability_first * (1 - probability_second) * (1 - probability_third) +
                       (1 - probability_first) * (1 - probability_second) * probability_third +
                       (1 - probability_first) * probability_second * (1 - probability_third)) * 100, 2)

print(f'Вероятность того, что в первый месяц выйдут от одной до двух деталей = {one_breakdown + two_breakdown} %')
