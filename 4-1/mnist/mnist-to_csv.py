import struct

def to_csv(name, maxData):
    #학습테스트 데이터 파일과 학습/테스트 레이블 파일 열기
    img_f = open("./mnist/"+ name + "-images-idx3-ubyte", "rb") # open("./mnist/train-images-idx3-ubyte","rb")
    lbl_f = open("./mnist/" + name + "-labels-idx1-ubyte", "rb")  #open("./mnist/labels-images-idx1-ubyte, "rb")
    csv_f = open("./mnist/" + name + ".csv", "w", encoding="utf-8")  #open("./mnist/labels-images-idx1-ubyte, "rb")

    # 'I':부호 없는 정수(4바이트),
    # 'B':부호 없는 정수(1바이트)
    magic,img_cnt=struct.unpack(">II",img_f.read(8))
    print(f"magic number: {magic}")
    print(f"전체 이미지 개수: {img_cnt}")
    rows, cols = struct.unpack(">II", img_f.read(8))
    print(f"1개 이미지 행 개수: {rows}")
    print(f"1개 이미지 열 개수: {cols}")
    pixels = rows * cols # 개 이미지의 픽셀 개수 : 784
    magic, lbl_count = struct.unpack(">II",lbl_f.read(8))
    print(f"lbl_count:{lbl_count}")

    for idx in range(lbl_count):
        if idx >= maxData:
            break
        label = struct.unpack("B",lbl_f.read(1))[0]# 튜플 첫번째 원소

        bdata = img_f.read(pixels)
        #print(bdata)

        sdata = list(map(lambda n:str(n),bdata))

        csv_f.write(str(label)+",")
        csv_f.write(",".join(sdata)+"\r\n")

        #check
        if idx < 10:
            s = "P2 28 28 255\n"
            #print(s)
            s += " ".join(sdata)
            #print(s)
            iname = "./mnist/{0}-{1}-{2}.pgm".format(name,idx,label)
            with open(iname, "w",encoding="utf-8") as f:
                f.write(s)


    img_f.close()
    lbl_f.close()
    csv_f.close()


to_csv("train",60000)
to_csv("t10k",10000)