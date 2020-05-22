import pandas as pd

covid19_ts = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
covid19_ts_tw = covid19_ts[covid19_ts['Country/Region'] == 'Taiwan*']
cumulative_confirmed_tw = list(covid19_ts_tw.loc[:,'1/22/20':'5/21/20'].values.ravel())
dates = list(covid19_ts_tw.loc[:, '1/22/20':'5/21/20'])
print(dates)
print(len(dates))
print(cumulative_confirmed_tw)
print(len(cumulative_confirmed_tw))
# 在這121天中那些"日期"是零新增確診