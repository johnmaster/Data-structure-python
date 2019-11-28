"""
归并排序
原理：
归并操作，指的是将两个已经排序好的序列合并成一个序列的操作。
归并排序算法依赖归并操作。
递归法：
假设序列共有n个元素：
1.将序列每相邻两个数字进行归并操作，排序后每个序列包含两个元素。
2.将上述序列再次归并，每个序列包含四个元素。
3.重复步骤2，直到所有元素排序完毕。
"""


def merge_sort(list):
    if len(list) <= 1:
        return list
    middle = len(list) // 2
    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])
    return merge(left, right)


def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


if __name__ == "__main__":
    nums = [8, 4, 5, 7, 1, 3, 6, 2]
    print(merge_sort(nums))
