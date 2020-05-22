# random 產生 1 個隨機數
import random

print(random.randint(1, 1000))
print("")

# random 產生 100 個隨機數
random_integers = []
for i in range(100):
    rand_int = random.randint(1, 1000)
    random_integers.append(rand_int)
print(random_integers)
print(len(random_integers))
print("")

# 找出第一大與第一小的數字
print(max(random_integers))
print(min(random_integers))
print("")

# 找出第二大與第二小的數字
print(len(set(random_integers))) # 先檢查有無重複
ran_int_unique = set(random_integers) # "set"不可取值
ran_int_unique_list = list(ran_int_unique) 
print(ran_int_unique_list)
ran_int_unique_list.sort()
print(ran_int_unique_list[1]) # 第二小
print(ran_int_unique_list[-2]) # 第二大