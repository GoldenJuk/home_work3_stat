# В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых.
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?

from functions import combinations

box_one_total = 8
box_one_white = 5
box_two_total = 12
box_two_white = 5
take_from_box_one = 2
take_from_box_two = 4
white_ball_from_take = 3

# Вероятности: 0б (из 1-й корзины) + 3б (из 2-й корзины); 1б из 1-й корзины) + 2б (из 2-й корзины);
#              2б из 1-й корзины) + 1б (из 2-й корзины)
res = 0
for i in range(white_ball_from_take):
    res += (combinations(i, box_one_white) * combinations(take_from_box_one - i, box_one_total - box_one_white) /
            combinations(take_from_box_one, box_one_total)) * \
           ((combinations(white_ball_from_take - i, box_two_white) * combinations(i + take_from_box_two - white_ball_from_take, box_two_total - box_two_white) /
            combinations(take_from_box_two, box_two_total)))

print(f'Вероятность того, что 3 мяча белые = {round(res * 100,2)} %')

