class MyCircularDeque:

    def __init__(self, k: int):
        self.__k = k
        self.__list = [ ]
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        

    def insertFront(self, value: int) -> bool:
        if self.__k >0:
            self.__list.insert(0, value)
            self.__k -=1
            return True
        else:
            return False

        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        

    def insertLast(self, value: int) -> bool:
        if self.__k >0:
            self.__list.append(value)
            self.__k -=1
            return True
        else:
            return False           
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        

    def deleteFront(self) -> bool:
        if self.__list == []:
            return False

        self.__list.pop(0)
        self.__k += 1
        return True
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        

    def deleteLast(self) -> bool:
        if self.__list == []:
            return False

        self.__list.pop()
        self.__k += 1
        return True
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        

    def getFront(self) -> int:
        if self.__list == []:
            return -1
        return self.__list[0]
        """
        Get the front item from the deque.
        """
        

    def getRear(self) -> int:
        if self.__list == []:
            return -1
        return self.__list[-1]
        """
        Get the last item from the deque.
        """
        

    def isEmpty(self) -> bool:
        return self.__list == []
        """
        Checks whether the circular deque is empty or not.
        """
        

    def isFull(self) -> bool:
        return self.__k == 0
        """
        Checks whether the circular deque is full or not.
        """
        

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
