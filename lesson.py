import csv
import datetime
import math
import os
# print(os.getcwd())
cus_file = "WORK_分析共有_顧客情報"
dir = "/Users/sasakiryou/Desktop/演習用フォルダ/python_excel/lesson/"
cus_csv_file = open(dir + cus_file + ".csv", encoding="shift-jis")
c = csv.reader(cus_csv_file)
# 顧客情報を２次元配列で格納
header = next(c)
# print(c)
cus_list = []
for i in c:
  cus_list.append(i) 
  
# 分析共有1を作成
newCus_list = []
newHeader = []
newCus_list = cus_list
header.extend(["退会週","登録時更新者","HosID","Docomo分類","キャンペーン分類"])
newHeader = header
f = open(dir+'分析結果.csv', 'w', encoding='shift-jis')
f.write(",".join(header) + "\n")
for row in cus_list:
  f.write(",".join(row) + "\n")

# # hosId分類
# hos_file = "HOSID_対応リスト"
# hos_csv_file = open(dir + hos_file + ".csv", encoding="shift-jis")
# h = csv.reader(hos_csv_file)
# hos_header = next(h)
# hos_list = []
# for i in h:
#   hos_list.append(i)
# for i,raw in enumerate(cus_list):
#   if(hos_list[i])
# # print(hos_list)

# # キャンペーン分類
# canp_file = "キャンペーン分類"
# canp_csv_file = open(dir + canp_file + ".csv", encoding="shift-jis")
# c = csv.reader(canp_csv_file)
# canp_header = next(c)
# canp_list = []
# newCanp_list = []
# for i in c:
#   canp_list.append(i)
# for i,row in enumerate(cus_list):
#   if cus_list[i][6] == canp_list[i][0]:
#     newCanp_list.append[row]
#   # print(canp_list[i][0])