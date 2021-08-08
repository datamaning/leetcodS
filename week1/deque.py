
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.mycdq=[0]*k
        self.k=k
        self.count=0
        self.start=0
        self.end=0


    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.count==self.k:
            return False
        self.start=(self.start-1)%self.k
        self.mycdq[self.start]=value
        self.count=self.count+1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.count==self.k:
            return False
        self.mycdq[self.end]=value
        self.end=(self.end+1)%self.k
        self.count=self.count+1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.count==0:
            return False
        self.start==(self.start+1)%self.k
        self.count=self.count-1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.count==0:
            return False
        self.end==(self.end-1)%self.k
        self.count=self.count-1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if  self.count==0:
            return -1
        return self.mycdq[self.start]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if  self.count==0:
            return -1
        k1=(self.end-1)%self.k
        return self.mycdq[(self.end-1)]
    

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.count==0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.k==self.count

