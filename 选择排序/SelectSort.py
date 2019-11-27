"""
选择排序
原理：
选择排序（Selection Sort）是一种简单直观的排序算法，它的工作原理
大致是将后面的元素最小元素一个个去除然后按顺序放置
步骤：
1.在未排序序列中找到最小（大），存放到排序序列的起始位置
2.再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的
末尾
3.重复第二步，直到所有元素均排序完毕
"""


def selection_sort(array):
    length = len(array)
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

if __name__ == "__main__":
    nums = [64, 25, 12, 22, 11]
    print(selection_sort(nums))
