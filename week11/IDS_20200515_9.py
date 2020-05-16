living_cost_dict = {
    '臺北市' : 17005,
    '新北市' : 15500,
    '桃園市' : 15281,
    '臺中市' : 14596,
    '臺南市' : 12388,
    '高雄市' : 13099,
    '非六都之縣市' : 12388,
    '金門縣連江縣' : 11648,
}
# 方法三
#@title Default title text
living_area = '\u975E\u516D\u90FD\u4E4B\u7E23\u5E02' #@param ['臺北市', '新北市', '桃園市', '臺中市', '臺南市', '高雄市', '非六都之縣市', '金門縣連江縣']
living_cost = living_cost_dict[living_area]
print("{}的每人每月最低生活費為{:,}".format(living_area, living_cost))