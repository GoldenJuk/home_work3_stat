# На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень.
# Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6.
# Найти вероятность того, что выстрел произведен: a). первым спортсменом б). вторым спортсменом в). третьим спортсменом.


probability_first = 0.9
probability_second = 0.8
probability_third = 0.6
sportsmens = 3

p_a = 1 / sportsmens * probability_first + 1 / sportsmens * probability_second + 1 / sportsmens * probability_third

print(
    f'Вероятность того, что выстрел произведен первым спортсменом = '
    f'{round((probability_first * 1 / sportsmens / p_a) * 100, 2)}%')
print(
    f'Вероятность того, что выстрел произведен вторым спортсменом = '
    f'{round((probability_second * 1 / sportsmens / p_a) * 100, 2)}%')
print(
    f'Вероятность того, что выстрел произведен третьим спортсменом = '
    f'{round((probability_third * 1 / sportsmens / p_a) * 100, 2)}%')
