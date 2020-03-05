
#get three value
"""
print("請輸入您的本金（萬元）、期數（年）與年利率（%），且格式為[本金,期數,年利率]")
a = input().split(",")
money = a[0]
year = a[1]
interest_rate = a[2]
"""

#test data
money = 1000000
year = 10
interest_rate = 11

#declare
import math
left_money = money #剩餘本金
money_permonth_list = list() #每月攤還本金列表
interest_permonth_list = list()#平均每月攤還利息列表
total = list() #本金利息累計(元)

money_permonth = math.ceil(money / (year * 12)) #平均每月攤還本金 #ceil

count_list = list() #first column in the dataframe below
for i in range(1 , (year*12) + 1):
  x = "第%s期" %(i)
  count_list.append(x)


#calculate
for i in range(year*12):
  interest_permonth = round(left_money * interest_rate / (12 * 100)) #round

  #due to the outcome of ceil, there will be little difference in the last element of money_permonth
  if left_money > money_permonth: 
    left_money = left_money - money_permonth
  else:
    money_permonth = left_money
    left_money = 0

  interest_permonth_list.append(str(interest_permonth)) 
  money_permonth_list.append(money_permonth)
  if i == 0:
    total.append(+ interest_permonth + money_permonth)
  else:
    total.append(total[i - 1] + interest_permonth + money_permonth)

#calculate sum of interests
sum_interest = total[year*12-1] - money

#output
import pandas as pd

name_list = ['本金', '期數(年)', '年利率', '平均每月攤還本金', '平均每月攤還利息', '全部利息'] #left of the dataframe above
value_list = [str(money) + '元' , str(year), str(interest_rate) + '%', str(money_permonth) + '元', "請參考下表", str(sum_interest) + '元']

df1 = pd.DataFrame(data = {'名稱' : name_list, '數值' : value_list})
print(df1)

df2 = pd.DataFrame(data = {'' : count_list, '本金（元）' : money_permonth_list, '利息（元）' : interest_permonth_list,
'本金利息累計(元)' : total})
print(df2)



