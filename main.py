import random

goal = input('Введение, пожалуйста, вашу цель. Варинаты: похудеть, набрать массу: ')
weight = input('Введите ваш изначальный вес')

num_of_ex = 2

print('Ваш изначальный вес', weight)
goal = goal.lower()
if goal == 'похудеть':
    up = ['планка', 'отжимания 12x3', 'обратные отжимания 12x3', 'кардио-тренировка на любимом тренажере 12x3',
          'жим от груди в тренажере, сидя 12x3', 'тяга верхнего блока 12x3', 'скручивания 12x3']
    down = ['приседания 12x3', 'зашагивания 12x3', 'жим ногами с верх.постановкой 12x3',
            'отведение ног, сидя в тренажере 12x3', 'выпады в тренажере Смита 12x3', 'румынская тяга 12x3',
            'подъемы на носки, сидя 12x3', 'ягодичный мостик, лежа на скамье 12x3']
    list_ex_1 = random.sample(up, num_of_ex)
    list_ex_2 = random.sample(down, num_of_ex)
    list_ex_all_1 = list_ex_1
    list_ex_all_1.extend(list_ex_2)
    first_ex__1 = list_ex_all_1[0]
    second_ex__1 = list_ex_all_1[1]
    third_ex__1 = list_ex_all_1[2]
    fourth_ex__1 = list_ex_all_1[3]
    print(str(first_ex__1))
    print(str(second_ex__1))
    print(str(third_ex__1))
    print(str(fourth_ex__1))


elif goal == 'набрать массу':
    up = ['планка', 'отжимания 6x3', 'подтягивания 6x3', 'жим гантелей, сидя 6x3',
          'сведение рук в тренажере, сидя 6x3', 'сведение рук в тренажере, сидя 6x3',
          'тяга нижнего блока 6x3', 'сгибание рук на скамье Скотта 6x3']
    down = ['скрестные выпады в Смите 6x3', 'подъемы на носки, стоя 6x3', 'разгибание ног, сидя в тренажере 6x3',
            'сведение ног, сидя в тренажере 6x3', 'книжка, сидя на ягодицах 6x3',
            'гиперэкстензия 6x3', 'подъемы на носки в тренажере жима ногами 6x3', 'махи ногой назад в кроссовере 6x3']
    list_ex_1 = random.sample(up, num_of_ex)
    list_ex_2 = random.sample(down, num_of_ex)
    list_ex_all_2 = list_ex_1
    list_ex_all_2.extend(list_ex_2)
    first_ex_2 = list_ex_all_2[0]
    second_ex_2 = list_ex_all_2[1]
    third_ex_2 = list_ex_all_2[2]
    fourth_ex_2 = list_ex_all_2[3]
    print(str(first_ex_2))
    print(str(second_ex_2))
    print(str(third_ex_2))
    print(str(fourth_ex_2))

