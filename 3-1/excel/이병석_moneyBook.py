import openpyxl
import re

# 엑셀 파일 불러와서 시트 추출
filename ="가계부_지출현황_6월.xlsx"
book = openpyxl.load_workbook(filename)

#'Sheet1 시트 추출
sheet = book['Sheet1']

#[공과금 사용여부] 컬럼에 체크된 날짜의 [카드]컬럼 데이터 추출
card_list =[]
for i in range(6,19):
    check_data =sheet[str(chr(65+5)) + str(i)].value
    if check_data == 1:
        date_data = sheet[str(chr(65)) + str(i)].value
        #날짜 중 마지막 날만 ㅜ출
        date = str(date_data[-3:-1])
        if date[0] == '0':
            date = date.replace('0', '')
        card_data = sheet[str(chr(65+4)) + str(i)].value
        #날짜, 카드 값으로 구성된 리스트 출력
        card_list.append([date,card_data])


    #print(f"카드 컬럼: {sheet[str(chr(65+4)) + str(i)].value}")
print(f"공과금 사용 카드 데이터:{card_list}")

#수정할 엑셀 자료의 [moneyBook_2022.xlsx]의 [june]시트의 [공금]컬럼에  날짜 맞게 입력
filename2 ="moneyBook_2022.xlsx"
book2 = openpyxl.load_workbook(filename2)
# 'jun2'
sheet2 = book2['june']

tot_price = 0;
for i in range(2,7):
    date = sheet2[str(chr(65)) + str(i)].value
    price = sheet2[str(chr(65 + 3)) + str(i)].value
    #None 값이면 0으로  기입
    if price == None:
        price=0
    for card in card_list:
        #날짜가 동일한지 체크
        if str(date) == str(card[0]):
            #같은 날짜이면 가격 업데이트
            price=price+int(card[1])
    #공과급 업데이트
    sheet2[str(chr(65 + 3)) + str(i)]=price
    print(f"update price: {sheet2[str(chr(65 + 3)) + str(i)].value}")
    #tot_price=tot_price+price
    #print(f"tot price:{tot_price}")
#합계 금액 저장
#print(f"tot price:{sheet2[str(chr(65 + 3)) + str(7)].value}")
#sheet2[str(chr(65 + 3)) + 7] = int(tot_price)
#sheet 이름 저장
sheet2.title='june'
book2.save('moneyBook_2022_update.xlsx')




