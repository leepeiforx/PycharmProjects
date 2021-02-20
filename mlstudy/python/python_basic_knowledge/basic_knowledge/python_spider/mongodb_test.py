import pymongo

client = pymongo.MongoClient('localhost',27017)             #连接数据库
mydb = client['mydb']                                       #新建mydb数据库
test = mydb['test']                                         #新建test数据集合
test_data = {
    'name':'Jan',
    'sex':'famale',
    'grade':89
}
test.insert_one(test_data)