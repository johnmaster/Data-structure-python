"""
冒泡排序
原理：
冒泡排序（Bubble Sort）是一种简单的排序算法。它重复地走访过要排序的
数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来，走访数列
的工作是重复地进行知道没有再需要交换，也就是说该数列已经排序完成。
步骤：
冒泡排序算法的运作如下：
1.比较相邻的元素，如果第一个比第二个大，就交换它们两个
2.对每一对相邻元素做同样的工作，从开始第一对到结尾最后一对。这步做完
后，最后的元素会是最大的数
3.针对所有的元素重复以上的步骤，除了最后一个。
4.持续每次对越来越少的元素重复上面的步骤，知道没有任何一对数字需要比较
"""


def bubble_sort(array):
    length = len(array)
    for i in range(length):
        flag = True
        for j in range(1, length - i):
            if array[j - 1] > array[j]:
                flag = False
                array[j - 1], array[j] = array[j], array[j - 1]
        if flag:
            return array
    return array


if __name__ == '__main__':
    nums = [12, 5, 1, 89, 22]
    print(bubble_sort(nums))