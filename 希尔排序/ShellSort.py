"""
希尔排序
原理：
希尔排序（Shell Sort）也称递减增量排序算法，是插入排序的一种更高效
的改进版本。希尔排序是非稳定排序算法。
希尔排序是基于插入排序的以下两点性质而提出改进方法的：
插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序
的效率，但插入排序一般来说是低效的，因为插入排序每次只能将数据移动
一位。
步骤：
每次以一定步长进行排序，直至步长为1。

一个排序算法是稳定的，就是当有两个相等记录的关键字R和S，且在原本的
列表中R出现在S之前，在排序后的列表中R也将会是在S之前。
不稳定排序算法可能会在相等的键值中改变记录的相对次序，但是稳定算法
从来不会如此，不稳定排序算法可以被特别的实现为稳定。
"""


def shell_sort(nums):
    n = len(nums)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
            print(nums)
        gap = gap // 2
    return nums


if __name__ == '__main__':
    nums = [17, 12, 1, 3, 2, 4]
    shell_sort(nums)