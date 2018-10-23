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

    print('items:',item_dict)
   
    def create_c1(dataset):
        c1 = []
        for tran in dataset:
            for item in tran:
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

    def lgen(lk, k):
        result = []
        lenlk = len(lk)
        for i in range(lenlk):
            for j in range(i+1, lenlk):
                l1 = list(lk[i])[:k-2]
                l2 = list(lk[j])[:k-2]
                if l1 == l2:
                    result.append(lk[i] | lk[j])
        return result

    def apr(dataset, minsup = 0.5):
        c1 = create_c1(data)
        d = list(map(set, data))
        l1, supdata = scan(d, c1, minsup)
        
        l = [l1]
        k = 2
        while (len(l[k-2]) > 0):
            ck = lgen(l[k-2], k)
            lk, supx = scan(list(d), ck, minsup)
            supdata.update(supx)
            l.append(lk)
            k += 1
        return l, supdata

    def rules(l, supdata, minconf = 0.6):
        all_list = []
        for i in range(1, len(l)):
            for freqset in l[i]:
                h1 = frozenset(item for item in freqset)
                if i >1 :
                    rule_from_con(freqset, h1, supdata, all_list, minconf)
                else:
                    calconf(freqset, h1, supdata, all_list, minconf)
        return all_list

    def calconf(freqset, h, supdata, br1, minconf = 0.6):
        prun = []
        for conseq in h:
            conf = supdata[freqset]/supdata[freqset-frozenset(conseq)]
        if conf >= minconf:
            print(freqset-conseq,'------>',conseq,'conf:',conf)
            br1.append((freqset-frozenset(conseq),conseq,conf))
            prun.append(conseq)
        return prun   

    def rule_from_con(freqset, h, supdata, br1, minconf = 0.6):
        #print(h,'.....................')
        h_list = list(h)
        m = len(h_list[0])
        if len(freqset) > m+1:
            hmp1 = lgen(h_list, m+1)
            hmp1 = calconf(freqset, hmp1, supdata, br1, minconf)
            if(len(freqset) > 1):
                rule_from_con(freqset, hmp1, supdata, br1, minconf)


    print('data:',data)
    l, supdata= apr(data)
    for c in range(len(l)):
        print('freq_itemset-'+str(c+1)+':',l[c])
    final_rule = rules(l, supdata, minconf = 0.6)
    print(final_rule)

 