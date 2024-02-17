###
# import random
# import pandas as pd
#
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()
# pd.get_dummies(data['whoAmI'])

### Через СТРОКИ
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = list()
# print('#\thuman\trobot')
# n = 0
# for i in lst:
#     if i == 'robot':
#         add_str = '0\t\t  1'
#         data.append(add_str)
#     else:
#         add_str = '1\t\t  0'
#         data.append(add_str)
#     print(f"{str(n)}\t  {data[n]}")
#     n += 1

### Через Числа
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data_human = list()
data_robot = list()
print('#\thuman\trobot')
n = 0
for i in lst:
    if i == 'robot':
        data_robot.append(1)
        data_human.append(0)
    else:
        data_robot.append(0)
        data_human.append(1)
    print(f"{str(n)}\t  {data_human[n]}\t\t  {data_robot[n]}")
    n += 1


