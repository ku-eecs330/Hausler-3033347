class DisjointSet:
    def __init__(self, size):
        self.vertex = [i for i in range(size)]
        self.rank = [0] * size

    def validate(self, v1):
        return 0 <= v1 < len(self.vertex)

    def size(self, v1):
        if not self.validate(v1):
            return None
        root = self.find(v1)
        return -self.vertex[root] if root >= 0 else self.rank[-root]

    def parent(self, v1):
        if not self.validate(v1):
            return None
        return self.vertex[v1]

    def find(self, v1):
        if not self.validate(v1):
            return None
        if self.vertex[v1] == v1:
            return v1
        self.vertex[v1] = self.find(self.vertex[v1])
        return self.vertex[v1]

    def unionByWeight(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        
        if root1 == root2:
            return
        
        if self.rank[root1] < self.rank[root2]:
            self.vertex[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.vertex[root2] = root1
        else:
            self.vertex[root2] = root1
            self.rank[root1] += 1

    def unionByRank(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        
        if root1 == root2:
            return
        
        if self.rank[root1] < self.rank[root2]:
            self.vertex[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.vertex[root2] = root1
        else:
            self.vertex[root2] = root1
            self.rank[root1] += 1

    def isConnected(self, v1, v2):
        if not self.validate(v1) or not self.validate(v2):
            return False
        return self.find(v1) == self.find(v2)

    def buildConnectedSets(self, connected):
        if not connected:
            return None
        
        n = len(connected)
        
        for i in range(n):
            for j in range(i + 1, n):
                if connected[i][j] == 1:
                    self.unionByWeight(i, j)

    def areBlocksConnected(self, block1, block2):
        if not self.validate(block1) or not self.validate(block2):
            return False
        return self.isConnected(block1, block2)

    def joinBlocks(self, connected):
        if not connected:
            return None
        self.buildConnectedSets(connected)

    def findBlockSets(self):
        sets = {}
        for i in range(len(self.vertex)):
            root = self.find(i)
            if root in sets:
                sets[root].append(i)
            else:
                sets[root] = [i]
        return list(sets.values())

    def findBlockCount(self, blockid):
        if not self.validate(blockid):
            return None
        root = self.find(blockid)
        return -self.vertex[root] if root >= 0 else self.rank[-root]

if __name__ == '__main__':
    # Tasks A
    uf = DisjointSet(10)
    # 0 1-2-5-6-7 3-8-9 4
    uf.unionByRank(1, 2)
    uf.unionByRank(2, 5)
    uf.unionByRank(5, 6)
    uf.unionByWeight(6, 7)
    uf.unionByRank(3, 8)
    uf.unionByWeight(8, 9)
    print(uf.isConnected(1, 5))  # true
    print(uf.isConnected(5, 7))  # true
    print(uf.isConnected(4, 9))  # false
    # 0 1-2-5-6-7 3-8-9-4
    uf.unionByWeight(9, 4)
    print(uf.isConnected(4, 9))  # true

    # Tasks B
    Connected = [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]
    uf = DisjointSet(4)
    uf.joinBlocks(Connected)
    uf.findBlockCount(1)


