import urllib.request as req
import gzip
import os, os.path

#저장 경로 및 다운로드  사이트 URL 지정, 다운 팡리 지정

savepath = "./mnist"
baseurl ="http://yann.lecun.com/exdb/mnist/"
files =[
'train-images-idx3-ubyte.gz',#:  #training set images (9912422 bytes)
'train-labels-idx1-ubyte.gz',#:  #training set labels (28881 bytes)
't10k-images-idx3-ubyte.gz',#:   #test set images (1648877 bytes)
't10k-labels-idx1-ubyte.gz'#:   #test set labels (4542 bytes)
]

#다운로드
if not os.path.exists(savepath):
    os.mkdir(savepath)

for file in files:
    url =baseurl + "/" + file # http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
    loc=savepath + "/" + file #./minist/train-images-idx3-ubyte.gz
    print(f"download: {url}")

    if not os.path.exists(loc):
        req.urlretrieve(url,loc)

#Gzip 압축해제
for file in files:
    #Download file
    gz_file = savepath +"/" +file                   #./minist/train-images-idx3-ubyte
    #가져온 데이터 저장할 파일
    raw_file = savepath +"/"+file.replace(".gz","") #./minist/train-images-idx3-ubyte

    with gzip.open(gz_file,"rb") as fp:
        body = fp.read()
        with open(raw_file, "wb") as w:
            w.write(body)