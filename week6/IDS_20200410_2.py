city = input("請輸入您所在的城市：")
weather = input("請輸入現在的天氣：")
tempc = input("請輸入現在的攝氏氣溫：")
tempc = int(tempc)
tempf = tempc*9/5 + 32

print("我在{}，天氣{}，攝氏{}度，華氏{}度".format(city, weather, tempc, tempf))