# やること
# ①アカ織を降順に並び替える
# ②アカ式の列の重複を取り除く
# ③定期解約日の列を時間だけ別の列に分離させる
# ④時間の列を削除
# ⑤定期解約日の列をnullと本日から３ヶ月以内だけ残してソート
# ⑥アカ式の列だけを取り出して完成ファイルとして作成
import os
import csv
import datetime

# print(os.getcwd()) 

# ①
# １データをインポートする
# ２ヘッダーとデータを分けて二次元配列に格納する
# ３データの０番目のカラム＝アカ式を降順に並び替える
master = "/Users/sasakiryou/Desktop/演習用フォルダ/python_excel/lesson/analysisLesson2/"
file = "3週間以内解約＋現ユーザー抽出元データ"
csv_file = open(master + file + ".csv", encoding="shift-jis")
c = csv.reader(csv_file)
header = next(c)
# print(header)
userList = []
for i in c:
  userList.append(i)
# print(userList)