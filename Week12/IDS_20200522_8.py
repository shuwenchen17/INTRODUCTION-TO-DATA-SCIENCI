print(list(range(10)))
print("")
# 方法一
squared = []
for i in range(10):
  squared.append(i**2)
print(squared)  
print("")
# 方法二
squared = [i**2 for i in range(10)]
print(squared) 