import csv
import re
from datetime import datetime
#配列宣言

ENCODING = 'cp932'
#csvファイルを指定
MyPath = './data.csv'

#csvファイルを読み込み
def read_csv():
    with open(MyPath,'r', encoding=ENCODING) as f:
        reader = csv.reader(f)
        data = []
        for row in reader:
            # 'http://' と 'https://' を空文字列に置換した url を生成
            url = row[1].replace("http://", "").replace("https://", "")
            text = re.sub('<h1.*?>|</h1>|<b>|<a.*?>|</a>|<span.*?>|</span>|【|】|！|～', '', row[4])
            # data リストに [url, text] の形式で追加
            title = re.sub('【|】|　', ' ', text)
            title = convert_date(title) 
            data.append([url, title])
    return data


def convert_date(text):
    # (8/14～8/16)のような形式をマッチさせる正規表現パターン
    pattern = r'\((\d+)\/(\d+)～(\d+)\/(\d+)\)'
    match = re.search(pattern, text)
    if match:
        start_month, start_day, end_month, end_day = match.groups()
        start_date = datetime.strptime(f'{start_month}/{start_day}', '%m/%d')
        end_date = datetime.strptime(f'{end_month}/{end_day}', '%m/%d')
        # 変換後のテキストを生成
        new_text = f'{start_date.month}月{start_date.day}日～{end_date.month}月{end_date.day}日'
        text = text.replace(match.group(0), new_text)
    return text