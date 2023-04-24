import csv

#配列宣言

ENCODING = 'cp932'
#csvファイルを指定
MyPath = './data.csv'

#csvファイルを読み込み
def read_csv():
    with open(MyPath,'r', encoding=ENCODING) as f:
        reader = csv.reader(f)
        data = None
        #csvファイルのデータをループ
        for row in reader:
            next(reader)  # ヘッダー行をスキップ
            data = [[row[1].replace("http://", "").replace("https://", ""), row[0]] for row in reader]
    return data