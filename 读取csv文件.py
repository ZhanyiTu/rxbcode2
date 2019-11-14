def fun1()

import pandas as pd #导入pandas包
data = pd.read_csv("WomensApparelReviews(1).csv") #读取csv文件
#print(data) #打印所有文件
#print(data.head(5)) #打印前5行
print(data.columns) #返回全部列名 Index(['',''])
#print(data.shape) #返回csv文件形状  (23486, 8)
#print(data.loc[1:2]) #打印第一行到第二行
#print(data.loc[2:4, ['Age', 'Department']]) #打印特定行的特定列
#print(data.loc[0:23486, ['Review Text']]) #这个表示我们要的那一列的数据
dataText = data.loc[0:23486, ['Review Text']]
for text in dataText
    fun1()

