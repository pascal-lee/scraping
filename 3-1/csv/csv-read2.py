import csv, codecs

# csv 파일 열기
filename= "csv-kr.csv"
fp = codecs.open(filename,"r","utf-8")
#delimiter(구분자),  quotechar(데이터를 감싸는 기호)
reader = csv.reader(fp,delimiter=",",quotechar='"')
#print(f"csv reader: {reader}")
# 한줄씩 일기
for cells in reader:
    #print(cells)
    print(cells[0],cells[1])