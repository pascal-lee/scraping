import csv, codecs

with codecs.open("test.csv", "w", "utf-8") as fp:
    writer = csv.writer(fp, delimiter=",",quotechar='"')
    writer.writerow(["ID","이름","가격"])
    writer.writerow(["1000", "SD", "30000"])
    writer.writerow(["1001", "book", "50000"])
    writer.writerow(["1002", "mouse", "70000"])