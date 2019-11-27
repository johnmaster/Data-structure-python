"""
小顶堆的实现思路基本跟大顶堆类似，唯一不同的是在更新堆的时候
停止条件由当前节点取值大于左右子节点，变为当前节点取值小于左
右子节点时停止更新堆。
"""


class MinHeap(object):
    def __init__(self):
        self._data = []
        self._count = 0

    def size(self):
        return self._count

    def isEmpty(self):
        return self._count == 0

    def add(self, x):
        self._data.append(x)
        self._shift_up(self._count)
        self._count += 1

    def return_heap(self):
        return self._data

    def pop(self):
        if self._count:
            ret = self._data[0]
            self._data[0] = self._data[-1]
            self._data.pop()
            self._count -= 1
            self._shift_down(0)
            return ret

    def _shift_up(self, index):
        parent = (index - 1) >> 1
        while index > 0 and self._data[index] < self._data[parent]:
            self._data[index], self._data[parent] = self._data[parent], self._data[index]
            index = parent
            parent = (index - 1) >> 1

    def _shift_down(self, index):
        min_child = (index << 1) + 1
        while min_child < self._count:
            if min_child + 1 < self._count and self._data[min_child + 1] < self._data[min_child]:
                min_child = min_child + 1
            if self._data[index] <= self._data[min_child]:
                break
            self._data[index], self._data[min_child] = self._data[min_child], self._data[index]
            index = min_child
            min_child = (index << 1) + 1

if __name__ == "__main__":
    heap = MinHeap()
    for i in range(10, -1, -1):
        heap.add(i)
    print(heap.return_heap())
    heap.pop()
    print(heap.return_heap())