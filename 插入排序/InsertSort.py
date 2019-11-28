"""
插入排序
原理：
插入排序（Insert Sort）是一种简单直观的排序算法。它的工作原理是通过
构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位
置并插入。
步骤：
1.从第一个元素开始，该元素可以认为已经被排序。
2.取出下一个元素，在已经排序的元素序列中从后向前扫描。
3.如果该元素（已排序）大于新元素，将该元素移到下一位置。
4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置。
5.将新元素插入到该位置后。
6.重复步骤2~5
"""


def insertionSort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums

if __name__ == "__main__":
    nums = [12, 11, 13, 5, 6]
    print(insertionSort(nums))

