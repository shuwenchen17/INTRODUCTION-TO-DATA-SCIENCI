user_int = int(input("請輸入一個正整數"))
if user_int % 15 == 0:
    print("Fizz Buzz")
elif user_int % 5 == 0:
    print("Buzz")
elif user_int % 3 == 0:
    print("Fizz")
else:
    print(user_int)