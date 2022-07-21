import openpyxl
import re
#population.xls 에서
#1. 출처 주석 삭제
#2. 인구수로 따졌을 때 제 3의 도시는 어디인가? 터미널  출력
 #인구순서대로 내림차순 정리
#3.제2의 대도시와 서울의 인구수 차이를 23번행에 저장 분석 결과 엑셀에 저장


# 1. filename
filename ="population.xlsx"
book = openpyxl.load_workbook(filename)

#2. 활성시트 추출
sheet = book.active
print(sheet.cell(row=5,column=6).value)
#1. 출처 주석 삭제
print(f"A22: {sheet[str(chr(65))+'22'].value}")
sheet[str(chr(65))+'22']=''
print(f"A22: {sheet[str(chr(65))+'22'].value}")
print(f"B22: {sheet[str(chr(66))+'22'].value}")
sheet[str(chr(66))+'22']=''
print(f"B22: {sheet[str(chr(66))+'22'].value}")
sheet[str(chr(65))+'23']=''
sheet[str(chr(66))+'23']=''
print(f"A23: {sheet[str(chr(65))+'23'].value}")
print(f"B23: {sheet[str(chr(66))+'23'].value}")

# 제3의 도시
pop_data=dict()
for i in range(5,22):
    #key=도시,  value=  인구수
    key=sheet[str(chr(65))+str(i)].value
    value=sheet[str(chr(75))+str(i)].value
    pop_data[key]=int(re.sub(",","",value))

print(f'city-population:{pop_data}')
ordered_dict = sorted(pop_data.items(),key = lambda item: item[1], reverse=True)
print(f" Ordered List: {ordered_dict}")
print(f" 3th: {ordered_dict[2]}")

#3. 제2의 대도시와 서울의 인구수 차이를 23번행에 저장 분석 결과 엑셀에 저장
print(f"2nd city{ordered_dict[2][0]}, 인구: {ordered_dict[2][1]} ")
print(f"seoul: {pop_data['서울']}")
city_diff = pop_data['서울']-ordered_dict[2][1]
sheet[str(chr(65))+'23']=format(city_diff , ',d')
cell = sheet[str(chr(65))+"23"]
cell.font = openpyxl.styles.Font(size=14, color="FF0000")
cell.number_format = cell.number_format

filename="population2.xlsx"
book.save(filename)
#3. 서울 인구를 제외한 인구  구해서 쓰기
# print(sheet["B4"].value)
# print(chr(66))
# print(type(chr(66)))
# for i in range(10):
#     #print(sheet[chr(66+i)+"4"].value)
#     total = sheet[chr(66+i)+"4"].value
#     seoul = sheet[chr(66+i)+"5"].value
#     output = int(re.sub(",","",total)) - int(re.sub(",","",seoul))
#     print(f"서울 제외 인구 = {output}")
#
#     #wirte values
#     sheet[str(chr(i+66))+"25"] = format(output, ',d')
#     #sheet[str(chr(i+66))+"21"] = output
#     cell = sheet[str(chr(i+66))+"25"]
#     cell.font = openpyxl.styles.Font(size=14, color="FF0000")
#     cell.number_format = cell.number_format
#     #font & size
# filename="population.xlsx"
# book.save(filename)
# print("ok")



