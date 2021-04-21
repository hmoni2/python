import operator

trainDic, trainList = {},[]

trainDic = {'Thomas':'토마스','Edward':'에드워드','Henry':'헨리','Gothon':'고든','James':'제임스'}
trainList = list(sorted(trainDic.items(),key = operator.itemgetter(1)))
print(trainList)