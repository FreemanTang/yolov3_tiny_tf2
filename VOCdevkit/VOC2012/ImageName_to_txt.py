import os
import random
 
trainval_percent = 0.2
train_percent = 0.8
xmlfilepath = 'Annotations'
txtsavepath = 'ImageSets\Main'
total_xml = os.listdir(xmlfilepath)
 
num = len(total_xml)
list = range(num)
# print(list)
tv = int(num * trainval_percent) # 训练验证集数量
tr = int(tv * train_percent) # 训练集数量
trainval = random.sample(list, tv)
# print(trainval,len(trainval))
train = random.sample(trainval, tr)
# print(train,len(train))
 
ftrainval = open('ImageSets/Main/trainval.txt', 'w')
ftest = open('ImageSets/Main/test.txt', 'w')
ftrain = open('ImageSets/Main/train.txt', 'w')
fval = open('ImageSets/Main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    #print(name)
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            fval.write(name)
        else:
            ftest.write(name)
    else:
        ftrain.write(name)
 
ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
