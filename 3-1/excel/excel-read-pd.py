import pandas as pd

#1. 엑셀 파일 열기
filename = "stat_104102.xlsx"
sheet_name ="Sheet0"
book = pd.read_excel(filename,sheet_name=sheet_name,header=2,engine='openpyxl')

#2. 2018 인구로 정렬
book = book.sort_values(by='2018',ascending=False)
print(book.head(10))