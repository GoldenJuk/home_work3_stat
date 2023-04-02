# Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean) среднее арифметическое,
# среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.

import pandas as pd
import numpy as np

salary = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
print(f'Исходная выборка: {salary}\n')

# среднее арифметическое
average = sum(salary) / len(salary)

print(f'Среднее значение зарплат из выборки: {average}')
print(f'Проверка результата с помощью numpy: {np.mean(salary)}\n')

# среднее квадратичное отклонение
temp = 0
for i in range(len(salary)):
    temp += (salary[i] - average) ** 2
standard_deviation_non_shifted = (temp / (len(salary) - 1)) ** (1 / 2)
standard_deviation_shifted = (temp / (len(salary))) ** (1 / 2)

print(f'Среднее квадратичное отклонение несмещенное: {round(standard_deviation_non_shifted, 2)}')
print(f'Проверка результата с помощью numpy: {round(np.std(salary, ddof=1), 2)}\n')

print(f'Среднее квадратичное отклонение смещенное: {round(standard_deviation_shifted, 2)}')
print(f'Проверка результата с помощью numpy: {round(np.std(salary), 2)}\n')

# смещенную и несмещенную оценки дисперсий
print(f'Несмещенная дисперсия: {round(standard_deviation_non_shifted ** 2, 2)}')
print(f'Проверка результата с помощью numpy: {round(np.var(salary, ddof=1), 2)}\n')
print(f'Cмещенная дисперсия: {round(standard_deviation_shifted ** 2, 2)}')
print(f'Проверка результата с помощью numpy: {round(np.var(salary), 2)}\n')
