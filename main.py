import matplotlib.pyplot as plt
import time

def GetPlot(data_input, title: str):
    names = list(data_input.keys())
    values = list(data_input.values())
    all_vals = sum(values)
    my_labels = []
    for i in names:
       my_labels.append(i + f"\n {int(data_input[i]/all_vals*100)}%")
    plt.pie(values, labels=my_labels)
    plt.title(title)
    plt.show()


raw_text = []
people_count = 18
types_count = 5
dict_data = dict.fromkeys(range(people_count))
types_names = ['Милтон Рокич(3 главные ценности)', 'Милтон Рокич (3 наименее значимых ценности)', 'профессионально значимые качества', 'Негативные (допустимые) ', 'Недопустимые  (критические) качества']
with open('data_significant.txt', encoding='utf-8', mode='r') as data:
    for i in dict_data.keys():
        t = dict.fromkeys(types_names)
        for j in t.keys():
            s = data.readline()
            s =''.join([i for i in s if not i.isdigit()]).lower()
            t[j] = (s).rstrip(',\n').lstrip(' ')
        dict_data[i] = t
#     Work with main values
    print(types_names[0])
    main_val_1 = []
    main_val_2 = []
    main_val_3 = []
    for i in dict_data.keys():
        raw_text.append(dict_data[i][types_names[0]])
    for i in raw_text:
        stripped = i.split(',')
        if '-' not in stripped:
            main_val_1.append(stripped[0].strip(' '))
            main_val_2.append(stripped[1].strip(' '))
            main_val_3.append(stripped[2].strip(' '))
    uniq_1 = dict.fromkeys({*main_val_1})
    uniq_2 = dict.fromkeys({*main_val_2})
    uniq_3 = dict.fromkeys({*main_val_3})
    uniq_all = dict.fromkeys({*main_val_1, *main_val_2, *main_val_3})
    for i in uniq_1.keys():
        uniq_1[i] = 0
    for i in uniq_2.keys():
        uniq_2[i] = 0
    for i in uniq_3.keys():
        uniq_3[i] = 0
    for i in uniq_all.keys():
        uniq_all[i] = 0
    #  Считаем, что на первом месте
    for i in uniq_1.keys():
        for j in main_val_1:
            if i == j:
                uniq_1[i] += 1
    # Считаем, что на втором месте
    for i in uniq_2.keys():
        for j in main_val_2:
            if i == j:
                uniq_2[i] += 1
    # Считаем, что на третьем месте
    for i in uniq_3.keys():
        for j in main_val_3:
            if i == j:
                uniq_3[i] += 1
    # Считаем, что на больше всего встречается
    for i in uniq_all.keys():
        for j in [*main_val_1, *main_val_2, *main_val_3]:
            if i == j:
                uniq_all[i] += 1
    GetPlot(uniq_1, "Главная ценность по Рокичу на 1 месте")
    time.sleep(1)
    GetPlot(uniq_2, "Главная ценность по Рокичу на 2 месте")
    time.sleep(1)
    GetPlot(uniq_3, "Главная ценность по Рокичу на 3 месте")
    time.sleep(1)
    GetPlot(uniq_all, "Главная ценность по Рокичу, абсолютное распределение")
    time.sleep(1)

print('The end')

