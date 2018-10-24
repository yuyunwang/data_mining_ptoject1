count = 1
item = 10
data = []
item_dict = {}
data_list = []

for i in range(item):
    item_dict[i] = 0

with open('/home/yuyun/文件/10data.txt', 'rt') as f:
    txt_data = f.readline()
    while txt_data:
        item_dict[int(txt_data.split()[2])] = item_dict[int(txt_data.split()[2])]+1
        if txt_data.split()[1] == str(count):
            data_list.append(txt_data.split()[2])
        else:
            count += 1
            data.append(data_list)
            data_list = []
            data_list.append(txt_data.split()[2])
        
        txt_data = f.readline()
    data.append(data_list)

   
    def create_c1(dataset):
        c1 = []
        for tran in dataset:
            for item in tran:
                #print(item)
                if not item in c1:
                    c1.append(item)
        c1.sort()
        return list(map(frozenset, c1))
    def scan(d, ck, minsup):
        scnt = {}    
        for tid in d:
            for can in ck:
                if can.issubset(tid):
                    if not scnt.__contains__(can):
                        scnt[can] = 1
                    else:
                        scnt[can] += 1
        
        numitems = float(len(d))
        l1_list = []
        supdata = {}
        for key in scnt:
            sup = scnt[key]/numitems
            if sup >= minsup:
                l1_list.insert(0,key)
            supdata[key] = sup
        return l1_list, supdata
    
    c1 = create_c1(data)
    d = map(set, data)
    l1 = scan(list(d), c1, 0.5)
    print(l1)
    