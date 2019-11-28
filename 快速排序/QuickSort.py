"""
快速排序
原理：
快速排序使用分治法（Divide And Conquer）策略来把一个序列分成
两个子序列。
步骤：
1.从数列中挑出一个元素，称为"基准"
2.重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比
基准值大的摆放在基准的后面（相同的数可以到任一边）。在这个分区
结束之后，该基准就处于数列的中间位置。这个称为分区操作。
3.递归地把小于基准值元素的子数列和大于基准值元素子数列排序。
"""


def quick_sort(nums, left, right):
    if left > right:
        return -1
    i, j = left, right
    temp = nums[left]
    while left != right:
        while nums[right] > temp and left < right:
            right -= 1
        while nums[left] < temp and left < right:
            left += 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
    nums[left] = temp
    quick_sort(nums, i, left - 1)
    quick_sort(nums, left + 1, j)
    return nums


if __name__ == "__main__":
    nums = [5, 14, 1, 8, 3, 2]
    print(quick_sort(nums, 0, len(nums) - 1))

