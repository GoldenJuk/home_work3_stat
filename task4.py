# В университет на факультеты A и B поступило равное количество студентов, а на факультет C студентов поступило столько же,
# сколько на A и B вместе. Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8.
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. Студент сдал первую сессию.
# Какова вероятность, что он учится: a). на факультете A б). на факультете B в). на факультете C?

probability_A = 0.8
probability_B = 0.7
probability_C = 0.9
p_a_a = p_a_b = 1/4
p_a_c = 1/2

p_a = p_a_a * probability_A + p_a_b * probability_B + p_a_c * probability_C

print(
    f'Вероятность того, что студент учится на факультете А = '
    f'{round((probability_A * p_a_a / p_a) * 100, 2)}%')
print(
    f'Вероятность того, что студент учится на факультете B = '
    f'{round((probability_B * p_a_b / p_a) * 100, 2)}%')
print(
    f'Вероятность того, что студент учится на факультете C = '
    f'{round((probability_C * p_a_c / p_a) * 100, 2)}%')