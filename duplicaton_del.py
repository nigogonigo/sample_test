import csv

lists = []
with open('./csv/sample_queue.csv') as f:
    for low in f:
        lists.append(low.rstrip('\n'))
s_list = set(lists)
list_del_dup = list(s_list)
print(list_del_dup) 
