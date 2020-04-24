user_int = input("請輸入一個正整數：")
user_int = int(user_int)
if user_int % 2 == 0:
    ans = "偶數"
else:
    ans = "奇數"
print(ans)