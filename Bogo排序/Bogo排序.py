"""
猴子排序（Bogo Sort）是个既不实用又原始的排序算法。
其原理等同将一堆卡片抛起，落在桌子上后检查卡片是否已经整齐排列好。
如果没有就再抛一次，直到排序好为止。
"""
import random


def bogo_sort(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return False
    return True


if __name__ == "__main__":
    nums = []
    for i in range(5):
        nums.append(random.randint(1, 1000))
    while not bogo_sort(nums):
        random.shuffle(nums)
    print(nums)