import os
import random

trainval_percent = 0.2
train_percent = 0.8
xmlfilepath = 'label'
txtsavepath = 'img'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('data_list/trainval.txt', 'w')
ftest = open('data_list/test.txt', 'w')
ftrain = open('data_list/train.txt', 'w')
fval = open('data_list/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
