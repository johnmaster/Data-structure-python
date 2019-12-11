"""
执行用时 :260 ms, 在所有 python3 提交中击败了59.91%的用户
内存消耗 :12.9 MB, 在所有 python3 提交中击败了100.00%的用户

设计链表的实现。可以选择单链表或者双链表。单链表中的节点应该具有两个
属性：val和next。val是当前节点的值，next是指向下一个节点的指针/引用
如果要使用双向链表，则还需要一个属性prev以指示链表中的上一个节点。

get(index):获取链表中第index个节点。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为val的节点。插入后，
新节点将成为链表的第一个节点。
addAtTail(val):将值为val的节点追加到链表的最后一个元素。
addAtIndex(index, val):在链表的第index个节点之前添加值为val的节点。
如果index等于链表的长度，则该节点将附加到链表的末尾。如果Index大于链表
长度，则不会插入节点。如果index小于0,则在头部插入节点。
deleteAtIndex(index)：如果索引index有效，则删除链表中的第index个节点。
"""


class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = Node(0)

    def get(self, index):
        if index < 0:
            return -1
        node = self.head
        for _ in range(index + 1):
            if node.next is not None:
                node = node.next
            else:
                return -1
        return node.val

    def addAtHead(self, val):
        new = Node(val)
        new.next = self.head.next
        self.head.next = new

    def addAtTail(self, val):
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(val)

    def addAtIndex(self, index, val):
        node = self.head
        for _ in range(index):
            if node.next is not None:
                node = node.next
            else:
                return
        new = Node(val)
        new.next = node.next
        node.next = new

    def deleteAtIndex(self, index):
        if index < 0:
            return
        node = self.head
        for _ in range(index):
            if node.next is not None:
                node = node.next
            else:
                return
        if node.next is not None:
            node.next = node.next.next