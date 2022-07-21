import json

price = {"date":"2017-05-10",
         "price":{
             "Apple":80,
             "Orange":55,
             "Banana":40,
             "Pear":90,
             "Pineapple":110
         }
}
data = json.dumps(price, indent=4)
print(data)