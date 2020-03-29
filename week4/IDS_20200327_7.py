player_name = input("球員名字")
player_height = input("球員身高")
player_weight = input("球員體重")
# 透過 input() 函數獲得的資料類別是文字，轉換函數 1. int()：轉換為整數類別 2. float()：轉換為浮點數類別 3. str()：轉換為文字類別 4. bool()：轉換為布林類別
player_height = float(player_height)
player_weight = float(player_weight)
player_bmi = player_weight/((player_height/100)**2)
print("{}的身體質量指數為：{:.2f}".format(player_name, player_bmi))
print("{}是否過重：{}".format(player_name, player_bmi > 30))