import urllib.request as req
import pandas as pd

#Download Mushroom Data Set
local = "mushroom.csv"
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"
req.urlretrieve(url, local)
print("ok")


