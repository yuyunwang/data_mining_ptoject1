class tree_node:
    def __init__(self, namev, num, parent_node):
        self.name = namev
        self.count = num
        self.node_link = None
        self.parent = parent_node
        self.children = {}

    def inc(self, num):
        self.count += num
    
    def disp(self, ind =1):
        print(' '*ind, self.name, '', self.count)
        for child in self.children.values():
            child.disp(ind+1)

    def create_tree(dataset, minsup = 1):
        header = {}
        for trans in dataset:
            for item in trans:
                header[item] = header.get(item,0) + dataset[trans]
        for k in header.keys():
            if header[k] < minsup:
                del header[k]
        freqset = set(header.keys())
        if len(freqset) == 0:
            return None,None
        for k in header:
            header[k] = [header[k], None]
        retree = tree_node('Null set',1,None)
        for transet, count in dataset.items():
            loc_id = {}
            for item in transet:
                if item in freqset:
                    loc_id[item] = header[item][0]
            if len(loc_id) > 0:
                orderitem = [v[0] for v in sorted(loc_id, items(), key = lambda p:p[1], reverse = True)]
                updatetree(orderitem, retree, header, count)
        return retree, header
    def updatetree(items, intree, header,count):
        if item[0] in intree.children:
            intree.children(item[0].ins(count))
        else:
            intree.children[item[0]] = tree_node(items[0], count, intree)
            if header[item[0][1]] == None:
                header[item[0][1]] == intree.children[item[0]]
            else:
                updateheader(header[items[0][1],intree.children[item[0]])
        if len(items) > 1:
            updatetree(item[1::], intree.children[items[0]],header,count)
    def updateheader(nodetest, target):
        while(nodetest.node_link != None):
            nodetest = nodetest.node_link
        nodetest.node_link = target
