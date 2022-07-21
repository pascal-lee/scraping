import codecs
filename= 'csv-kr.csv'
csv = codecs.open(filename,'r','utf-8').read()

#csv을 리스트로 변화
data = []
rows = csv.split("\r\n")
#print(f"by row: {rows}")
for row in rows:
    if row =="":
        continue
    cells=row.split(",")
   # print(f"cells: {cells}")
    data.append(cells)

# print data
#print(f"list data: {data}")
for c in data:
    print(c[0], c[1],c[2])