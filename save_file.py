from pymongo import MongoClient
import bson.binary

conn = MongoClient('localhost',27017)
db = conn.images
myset = db.girl


#存储图片
# with open('p.jpeg','rb') as f:
#     data = f.read()
#
#
# #将ｄａｔａ转换为ｂｓｏｎ格式
# content = bson.binary.Binary(data)
#
# #插入到集合
# dic = {'filename':'girl.jpeg','data':content}
# myset.insert_one(dic)
#

#提取文件
s = myset.find_one({'filename':'girl.jpeg'})

#print(s)

with open('mm.jpeg','wb') as f:
    f.write(s['data'])


conn.close()