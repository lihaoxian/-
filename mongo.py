
#修改主分支



"""
pymongo模块操作实例
用于数据曾删改差方法的参考

"""

from pymongo import MongoClient

#　创建数据库连接
conn = MongoClient('localhost',27017)

#　创建数据库对象和集合对象
db = conn.stu
myset = db.class4

#　数据操作

#*******************insert*************************************************************
#myset.insert_one({'name':'张铁林','King':'乾隆'})
#myset.insert_many([{'name':'陈道明','King':'康熙'},{'name':'张国立','King':'康熙'}])
# myset.insert({'name':'唐国强','King':'雍正'})
# myset.insert({'name':'陈建斌','King':'雍正'})
# myset.insert({'name':'聂远','King':'乾隆'})

# myset.save({'_id':1,'name':'吴奇隆','king':'四爷'})
#myset.save({'_id':1,'name':'郑少秋','King':'乾隆'})

#***********************find**********************************************************

#所有的操作符加引号，作为字符串表达
#cursor = myset.find({},{'_id':0})
# for i in cursor:
#     print(i['name'],'---',i['King'])
#*****************************************

#print(cursor.next())  #获取游标的下一个结果
#*****************************************

#ｃｕｒｓｏｒ调用ｌｉｍｉｔ，ｓｋｉｐ，ｓｏｒｔ后得到的仍然是结果游标对象
# for i in cursor.skip(1).limit(3):
#     print(i)
#***************************

#按照ｋｉｎｇ排序
# for i in cursor.sort([('King',1)]):
#     print(i)
#*****************************************

# r = myset.find_one({'King':'康熙'},{'_id':0})
#
# print(r)

#***********************************8*****update**************************************

#myset.update_one({'King':'康熙'},{'$set':{'king_name':'玄烨'}})

#myset.update_many({'King':'雍正'},{'$set':{'king_name':'胤真'}})


#myset.update({'King':'乾隆'},{'$set':{'king_name':'弘历'}},multi = True)


#myset.update_one({'King':'光绪'},{'$set':{'name':'邓超'}},upsert = True)

#**********************************************delete***********************************8
#myset.delete_one({'King':'乾隆'})
#myset.delete_many({'king_name':None})
#myset.remove({'King':'雍正'},multi = False)

# r = myset.find_one_and_delete({'King':'乾隆'})
# print(r)

#**********************************************index*************************************8

# index1 = myset.create_index('name')
#
# index2 = myset.create_index([('name',-1)],name = "NAME")
#
# print("index1 = ",index1)
# print("index2 = ",index2)
#
# #查看索引
# for i in myset.list_indexes():
#     print(i)

#删除索引
# myset.drop_index('NAME')
# myset.drop_index([('name',1)])
# myset.drop_indexes()

#查看索引
# for i in myset.list_indexes():
#     print(i)

#*************************************aggregation**************************************


myset = db.class0  #  更换操作集合

pipe = [{'$match':{'sex':{'$exists':True}}},{'$sort':{'age':1}},{'$project':{'_id':0}}]

cursor = myset.aggregate(pipe)


for i in cursor:
    print(i)








# 关闭连接
conn.close()



































