"""
计数排序
原理：
当输入的元素是n个0到k之间的整数时，它的运行时间是O(n + k)。计数
排序不是比较排序，排序的速度快于任何比较排序算法。
由于用于计数的数组C的长度取决于待排序数组中数据的范围(等于待排序
数组的最大值和最小值的差加上1)，这使得计数排序对于数据范围很大的
数组，需要大量的时间和内存。例如：计数排序是用来排序0到100之间的
数字的最好的算法，但是它不适合按字母顺序排序人名。但是，计数排序
可以用在基数排序算法中，能够更有效的排序数据范围很大的数组。
步骤：
1.找出待排序的数组中最大和最小的元素。
2.统计数组中每个值为i的元素出现的次数，存入数组C的第i项。
3.对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）。
4.反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元
素就将C(i)减去1
"""


def count_sort(nums):
    max_num = max(nums)
    min_num = min(nums)
    count = [0] * (max_num - min_num + 1)
    for i in nums:
        count[i - min_num] += 1
    index = 0
    for i in range(max_num - min_num + 1):
        for j in range(count[i]):
            nums[index] = min_num + i
            index += 1
    return nums

if __name__ == "__main__":
    nums = [8, 7, 5, 1, 3, 71]
    print(count_sort(nums))




