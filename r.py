# 讀取檔案
# r就是讀取模式, w就是寫入模式
# 打開檔案後, 把檔案當作f, 只是一種簡稱
# 用for迴圈來一行一行的讀取檔案

# with open('food.txt', 'r') as f: 
	# for line in f:
		# print(line)

# 遇到問題: 用txt檔案會有換行的問題, print本身也會換行, 造成兩次換行
# 解決方式: 先用.append()把讀取檔案的每一行(line)裝進清單, 印出來看
# 解決方式: 再用.strip()除掉換行符號
# 筆記: .strip()的功能,就是把換行符號清掉, 前後有空格他也會除掉
# 筆記: .strip()是一個只能對字串做的功能, 就像.append()只能對清單做一樣

data = []
with open('food.txt', 'r') as f: 
	for line in f:
		data.append(line.strip())
print(data) 

# 進階說明:
# open是打開檔案的意思
# with是python設計的功能, 是一個自動close的功能
# 因為當open讀取一個檔案時, 就像檔案被夾住, 別人不能用
# 所以加了with open後, 當程式走出with的框框後(如第20行), 讀取的檔案就會自動關閉
