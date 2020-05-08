# variable vs. values: 1-on-multiple ( 1 對 多 )
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(len(weekdays)) #觀察長度

lucky_numbers = [7, 24, 5566]
print(lucky_numbers)
lucky_numbers.append(87) #新增資料至末端
print(lucky_numbers)
lucky_numbers.pop() #將最末端資料拋出
print(lucky_numbers)
my_fav_group = lucky_numbers.pop()
print(lucky_numbers)
print(my_fav_group) #讀出拋出的最末端資料