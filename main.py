# import docx
import csv
# import openpyxl
# group_one = {1: 'Анхель Аксель Рейес Апарисио',
#              2: 'Ержанов Максат Куандыкович',
#              3: 'Журавлева Татьяна Вячеславовна',
#              4: 'Капча Мансилльа Марко Освальдо',
#              5: 'Леушина Екатерина Владимировна',
#              6: 'Матвеева Лариса Сергеевна',
#              7: 'Эспиноза Валлес Ангело Сальватор'
#              }
#
# group_two = {1: 'Акимченко Ульяна Владимировна',
#              2: 'Андреева Виктория Валерьевна',
#              3: 'Асбаганова Виктория Валерьевна',
#              4: 'Атлашов Павел Николаевич',
#              5: 'Бол Тон Май Нгуот',
#              6: 'Болотина Виолетта Александровна',
#              7: 'Боярский Иван Сергеевич',
#              8: 'Буенростро Гроскоп Габриэль Хосе',
#              9: 'Васильев Евгений Александрович',
#              10: 'Гаврилов Данил Олегович',
#              11: 'Гаврилов Данила Сергеевич',
#              12: 'Горячкина Вероника Евгеньевна',
#              13: 'Гуськов Данила Михайлович',
#              14: 'Данилова Екатерина Олеговна',
#              15: 'Золотухин Ярослав Анатольевич',
#              16: 'Иванов Илья Эдуардович',
#              17: 'Каллистов Мирон Ильич',
#              18: 'Колесникова Виктория Евгеньевна',
#              19: 'Лагунова Анастасия Васильевна',
#              20: 'Леаль Эрнандес Мигель Анхель',
#              21: 'Мелёхин Роман Валерьевич',
#              22: 'Орлов Иван Андреевич',
#              23: 'Пономарева Мария Андреевна',
#              24: 'Попов Илья Александрович',
#              25: 'Пресняков Кирилл Олегович',
#              26: 'Рогожин Игорь Георгиевич',
#              27: 'Филиппов Вадим Викторович',
#              28: 'Хандоко Фарах Дефрида',
#              29: 'Эспиноза Чири Хуан'
#              }
#
# with open('one.xlsx', 'w') as one:
#     one_writer = openpyxl.load_workbook('one.xlsx')
#     # one_writer.writerow(len(group_one)*[' '] + ['Всего'])
#
# # for i in range(len(group_one)):
# #     table_one.
#
# print(len(group_one))

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
            t[j] = (s).rstrip(',\n')
        dict_data[i] = t
    print('FFF')

