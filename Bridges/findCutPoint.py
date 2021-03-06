"""
@author: Alex
@contact: 1272296763@qq.com or jakinmili@gmail.com
@file: findCutPoint.py
@time: 2019/10/20 19:12
"""
class findCutPoint:

    def __init__(self, filename):
        self.V = 0  # 顶点数
        self.E = 0  # 边数
        self.adj = None



        with open(filename) as f:
            line_num = 0  # 第一行是顶点数和边数
            for line in f:
                if line_num == 0:
                    v, e = line.strip().split()
                    self.V = int(v)
                    self.E = int(e)
                    self.adj = [[] for i in range(self.V)] # 创建二维数组即邻接表
                else:
                    # 读取边 写入邻接表
                    v1, v2 = line.strip().split()
                    # 转化为整数
                    v1 = int(v1)
                    v2 = int(v2)
                    self.adj[v1].append(v2)
                    self.adj[v2].append(v1)
                line_num += 1

        self.__visited = [False for i in range(self.V)]
        self.__ord = [0 for i in range(self.V)]
        self.__low = [0 for i in range(self.V)]
        self.__cnt = 0
        self.res = set()


        # 各个联通分量寻找桥
        for v in range(self.V):
            if self.__visited[v] == False:
                self.graphDFS(v, v)

    def get_graph_information(self):
        """
        打印图的邻接表
        :return:
        """
        print("V={}, E={}".format(self.V, self.E))
        for i, v in enumerate(self.adj):
            print("{} : {}".format(i, v))

    def validateVertex(self, v):
        """
        验证顶点取值
        :param v:
        :return:
        """
        if v<0 or v>=self.V:
            raise ValueError("v值超出范围")

    def hasEdge(self, v, w):
        """
        判断两个顶点是否存在
        :param v: 第一个顶点
        :param w: 第二个顶点
        :return: true or false
        """
        self.validateVertex(v)
        self.validateVertex(w)
        return w in self.adj[v]

    def degree(self, v):
        """
        求某个顶点的度
        :param v:
        :return:
        """
        self.validateVertex(v)
        return len(self.adj[v])


    def graphDFS(self, v, parent):

        # 标记v顶点已经遍历过了
        self.__visited[v] = True
        self.__ord[v] = self.__cnt
        self.__low[v] = self.__ord[v]
        self.__cnt+=1

        child = 0
        # 添加
        for w in self.adj[v]:
            if self.__visited[w] == False:
                self.graphDFS(w, v)
                self.__low[v] = min(self.__low[v], self.__low[w])

                # 割点检测
                if v != parent and self.__low[w] >= self.__ord[v]:
                    self.res.add(v)

                child += 1

                if v == parent and child>1: # 如果是根节点
                    self.res.add(v)

            elif w != parent:
                self.__low[v] = min(self.__low[v], self.__low[w])

    def findCutPoint(self):
        print("该联通分量有存在割点的有：", self.res)

if __name__ == '__main__':
    fb = findCutPoint("../g_bridges2.txt")
    fb.get_graph_information()
    fb.findCutPoint()

    fb1 = findCutPoint("../tree.txt")
    fb1.get_graph_information()
    fb1.findCutPoint()
