#!usr/bin/env python
# -*- coding:utf-8 -*-
dic = {
    1:{"id":1,"name":"hds"},
    2:{"id":2,"name":"dss"}
}
for item in dic.items():
    print(item)

for k,v in dic.items():
    print(k,v)

for item in dic.values():
    print(item)

