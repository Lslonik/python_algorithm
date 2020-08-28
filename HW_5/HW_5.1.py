# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import deque, defaultdict
while True:
    try:
        number_of_enterprise = int(input('Введите количество предприятий: '))
        enterprises_name = deque()
        enterprise_profit = defaultdict(list)
        enterprises_sum_profit = {}
        sum_of_profits = 0
        higher_average_profit = []
        lower_average_profit = []

        for i in range(number_of_enterprise):
            enterprises_name.append(input(f'Введите название предприятия №{i + 1}: '))
            enterprise_profit[enterprises_name[i]].append(
                [int(profit) for profit in input(f'Введите прибыль предприятия за '
                                                 f'каждый квартал через пробел: '
                                                 f'').split()])

        for el, num_profit in enumerate(enterprise_profit):
            sum_of_profits += sum(enterprise_profit[num_profit][0])
            enterprises_sum_profit[num_profit] = sum(enterprise_profit[num_profit][0])
            # print(enterprises_sum_profit)

        print(f'Средняя годовая прибыль предприятий: {round(sum_of_profits / number_of_enterprise, 1)}')

        for i in range(number_of_enterprise):
            if enterprises_sum_profit[enterprises_name[i]] <= (sum_of_profits / number_of_enterprise):
                lower_average_profit.append(enterprises_name[i])
            else:
                higher_average_profit.append(enterprises_name[i])

        print(f'Предприятия, с прибылью ниже среднего: {lower_average_profit}')
        print(f'Предприятия, с прибылью выше среднего: {higher_average_profit}')
        break
    except:
        print('Введите числовое значение')
