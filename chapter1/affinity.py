# -*- coding: UTF-8 -*-

from collections import defaultdict

from operator import itemgetter

import numpy as np


#导入文本数据
dataset_filename = "affinity_dataset.txt"
X = np.loadtxt(dataset_filename)

#有效规则字典
valid_rules = defaultdict(int)
#无效规则字典
invalid_rules = defaultdict(int)
#发生频率数
num_occurances = defaultdict(int)

for sample in X:
    for premise in range(5):
        if sample[premise] == 0: continue
        num_occurances[premise] += 1
        for conclusion in range(5):
            if premise == conclusion: continue
            if sample[conclusion] == 1:
                valid_rules[(premise, conclusion)] += 1
            else:
                invalid_rules[(premise, conclusion)] += 1

support = valid_rules
confidence = defaultdict(float)

#按支持度倒序排列字典
sorted_support = sorted(support.items(), key=itemgetter(1), reverse=True)
print sorted_support

#排序列出支持度最高的前5条规则
for index in range(5):
    print("Rule #{0}".format(index + 1))
    premise,conclusion = sorted_support[index][0]
    num_support =  sorted_support[index][1]
    print premise,conclusion,(" - Support: {0}".format(num_support))

#置信度计算
for premise, conclusion in valid_rules.keys():
    rule = (premise, conclusion)
    confidence[rule] = float(valid_rules[rule]) / float(num_occurances[premise])
    #print("Rule: If a person buys {0} they will also buy{1}".format(premise, conclusion))
    #print(" - Support: {0}".format(support[(premise,conclusion)]))
    #print(" - Confidence: {0:.1f}%".format(confidence[(premise,conclusion)]*100))

#按置信度倒序排列字典    
sorted_confidence = sorted(confidence.items(), key=itemgetter(1), reverse=True)

print sorted_confidence

#排序列出置信度最高的前5条规则
for index in range(5):
    print("Rule #{0}".format(index + 1))
    premise,conclusion = sorted_confidence[index][0]
    pre_confidence =  sorted_confidence[index][1]
    print premise,conclusion,(" - Confidence: {0:.1f}%".format(pre_confidence*100))
