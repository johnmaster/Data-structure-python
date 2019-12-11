"""
给定一个链表，判断链表中是否有环。
利用哈希表解决这样的问题：
首先定义一个集合set，之后遍历链表的结点，每遍历一个结点，就将这个
结点的元素放入set中，如果这个链表没有环，那么最终遍历就结束了。
如果链表有环的话，那么肯定有一个元素会被访问两次，当第二次访问这个
元素的时候，set中就有记录了，这样就可以判断出链表是否有环了。

哈希表可以解决这样的问题，但是使用双指针技巧有一个更高效的解决方案。
想象一下，有两个速度不同的跑步者。如果他们在直路上行驶，快跑者将首
先到达目的地，但是，如果它们在圆形跑到上跑步，那么快跑者如果继续跑
步就会追上慢跑者。
这正是我们在链表中使用两个速度不同的指针时会遇到的情况：
1.如果没有环，快指针将停在链表的末尾。
2.如果有环，快指针最终将与慢指针相遇。
所以剩下的问题是：
这两个指针的适当速度应该是多少？
一个安全的选择是每次移动慢指针一步，而移动快指针两步。每一次迭代，
快速指针将额外移动一步。如果环的长度为M，经过M次迭代后，快指针肯定
会多绕环一周，并赶上慢指针。

执行用时 :48 ms, 在所有 python3 提交中击败了97.18%的用户
内存消耗 :16 MB, 在所有 python3 提交中击败了100.00%的用户

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        low, quick = head, head.next
        while quick and quick.next:
            if low == quick:
                return True
            low = low.next
            quick = quick.next.next
        return False