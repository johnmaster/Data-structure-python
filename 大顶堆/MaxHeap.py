class MaxHeap(object):
    def __init__(self):
        self._data = []
        self._count = 0

    def size(self):
        return self._count

    def isEmpty(self):
        return self._count == 0

    def return_heap(self):
        return self._data

    def add(self, x):
        """
        往大顶堆中添加元素：
        1.首先把新添加的元素当作最后一个叶子结点添加到堆的后面
        2.判断当前节点和其父节点的大小：若当前节点大于父节点，那么
        交换两个节点的位置，然后继续往上比较。
        :param x: 需要加入到最大堆中的元素
        :return: 返回调整后的大顶堆
        """
        self._data.append(x)
        self._shift_up(self._count)  # _shiftUp传入的参数是新加入节点的索引
        self._count += 1

    def pop(self):
        """
        从大顶堆中弹出根节点，该元素肯定是这个堆中最大的元素；调整堆的结构
        使得新的堆仍然是一个大顶堆
        1.首先弹出根节点（索引为0的元素），然后把一个叶子节点放到根节点位置上
        2.从根节点开始，比较其两个子节点的大小，当当前节点小于其子节点时，则
        将当前节点与较大的一个子节点交换位置，然后继续向下比较，直到当前节点
        是叶子节点或者当前节点大于其子节点
        :return: 返回调整后的最大堆
        """
        if self._count:
            ret = self._data[0]
            self._count -= 1
            self._data[0] = self.data[-1]
            self._shift_down(0)
            return ret

    def _shift_up(self, index):
        parent = (index - 1) >> 1
        while index > 0 and self._data[index] > self._data[parent]:
            self._data[index], self._data[parent] = self._data[parent], self._data[index]
            index = parent
            parent = (index - 1) >> 1

    def _shift_down(self, index):
        """
        总共分为三种情况
        1.总共有两个节点，删除根节点后只剩余一个节点。这种情况不需要进行比较。
        2.总共有三个节点，删除根节点后只剩余两个节点，这种情况下不需要寻找哪
        个子节点是最大的，因为只有一个根节点。
        3.总共有大于三个节点，删除根节点后大于等于3，这种情况需要判断子节点中
        哪一个最大，然后进行更换。
        :param index: 弹出根节点的位置，也就是0
        :return:
        """
        max_child = (index << 1) + 1    #首先假设左子节点为最大的子节点
        while max_child < self._count:
            #判断是否存在右子节点
            if max_child + 1 < self._count and self._data[max_child + 1] > self._data[max_child]:
                max_child = max_child + 1
            if self._data[index] < self._data[max_child]:
                self._data[index], self._data[max_child] = self._data[max_child], self._data[index]
                index = max_child
                max_child = (index << 1) + 1
            else:
                break

if __name__ == '__main__':
    heap = MaxHeap()
    for i in range(10):
        heap.add(i)
    print(heap.return_heap())











