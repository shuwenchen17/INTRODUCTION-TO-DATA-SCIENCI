# 方法一
odds_squared = []
for i in range(10):
  if i % 2 == 1:
      odds_squared.append(i**2)
print(odds_squared)    
print("")
# 方法二
odds_squared = [i**2 for i in range(10) if i % 2 == 1]
print(odds_squared)