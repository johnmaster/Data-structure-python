"""
鸡尾酒排序是冒泡排序的升级版，属于双向冒泡排序。
基本原理：
1.找出最大值放到最后，找到最小值放到最前（同一步中进行，但有先后）。
2.找出第二大值放到倒二，找到第二小值放到第二个位置。
3.重复以上步骤
循环次数：数组长度n//2取整（偶数时正好排列完毕，奇数时中间剩余的也
正好排列）
"""


def cocktail_sort(nums):
    size = len(nums)
    for i in range(size // 2):
        flag = True
        for j in range(i, size - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        for j in range(size - 2 - i, i, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                flag = False
        if flag:
            return nums
    return nums


if __name__ == "__main__":
    nums = [5, 2, 6, 1, 7, 4, 3, 20, 10, 0, 7]
    print(cocktail_sort(nums))
