import openpyxl



# 1. 엑셀 파일 열기
filename = "stat_104102.xlsx"
book = openpyxl.load_workbook(filename)
# 2. 첫번째 시트 추출하기
sheet = book.worksheets[0]
# 3. 시트의 각행을 순서대로 추출
data = []
for row in sheet.rows:
    data.append([row[0].value,
                 row[10].value
                 ])
#print(f"data: {data}")
# 4. 필요없는 줄 제거
del data[0:4]
del data[16:19]
print(len(data))
# 5. 데이터를 인구순서로 정렬
data = sorted(data, key=lambda x: x[1])
print(data)
# # 6. 순서대로 출력 하위 5개
for i, a in enumerate(data):
    if (i >= 5):
        break
    print(i+1,a[0],int(str(a[1]).replace(',','')))