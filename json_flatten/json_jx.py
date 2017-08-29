# -*- coding: UTF-8 -*-
import pandas as pd
from flatten_json import flatten
import codecs
import json
import re

path = 'xhf_20170821.json'

with codecs.open(path, 'r', 'utf-8') as json_data:
    json_dicts = json.load(json_data) # 读取json数据为list[dict]结构

row_1 = json_dicts[:2000]

key_list = set()

for i in row_1:
    for k,v in  flatten(json.loads(i['result'])).items():
        #print re.sub(r'_\d+_','-',k)
        key_list.add(re.sub(r'_\d+_','-',k))

num = 0
for i in key_list:
    print num,i
    num+=1
print len(key_list)




dic = {"a": 1,
       "b": 2,
       "c": [{"d": [2, 3, 4], "e": [{"f": 1, "g": 2}]}]
      }

#print dic
#print flatten(dic)

#for i in json_dicts:
    #print flatten(i)

    #dic_flattened = (flatten(d) for d in dict(i))
    #df = pd.DataFrame(dic_flattened)
    #print df.index()
    #json_df = pd.io.json.json_normalize(json_dicts)  # 处理嵌套json
    #df = pd.DataFrame(json_df)

#dic_flattened = (flatten(d) for d in dic)

