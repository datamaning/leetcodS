
from collections import deque as q

class Solution:
    def ladderLength(self, beginWord, endWord, wordList) -> int:
        # 让我康康你是不是我儿砸
        def ShiErZaMa(baba, erza):
            dif = 0
            for i in range(0, len(baba)):
                if baba[i] != erza[i]:
                    dif += 1
                if dif > 1:
                    return False
            return True

        # 特殊例子
        if endWord not in wordList:
            return 0

        # ---------  初始化
        OneLayer_b = q()  # 开始节点的队列
        OneLayer_e = q()  # 结束节点的队列

        OneLayer_b.append(beginWord)
        OneLayer_e.append(endWord)

        Visited_b = [True] * len(wordList)  # 开始节点BFS找到的数，True是可以查，查到了就转成False就不再查了。
        Visited_e = [True] * len(wordList)  # 结束节点BFS找到的数，

        CengShu_b = 0  # 开始节点BFS的层数
        CengShu_e = 0  # 结束节点BFS的层数

