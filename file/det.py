# 本程序可用于计算行列式（手搓）

import numpy as np
import math
# 定义需要计算行列式的矩阵
D = np.array(
    [[1,2,1,1],
     [0,2,1,11],
     [-2,-1,4,4],
     [-2,-1,1,100.123909384324]]
)


def inv_num(invNum_arr):
    '''计算逆序数：输入为一维数组，对该数组计算逆序数'''
    invNum = 0 #定义逆序数变量
    arr_len = invNum_arr.size
    for i in range(arr_len):
        # 第一个元素逆序数一定为0
        if i == 0:
            pass
        else:
            for j in range(i):
                # 如果第i个元素之前有n个比它大的元素，则逆序数为n
                if invNum_arr[j]>invNum_arr[i]:
                    invNum = invNum + 1
    # 返回该数组总的逆序数
    return invNum

def permute(nums):
    """ 获取1-n的全排列组合(递归求解)\n
        输入：[1,2,3,...,n]的一维列表   type nums: List[int]\n
        返回：一个二维列表，里面包含了n!种排列方式   returntype: List[List[int]]
    """
    # 递归终止条件：当列表只剩下一个元素时，其本身即为一个排列
    if len(nums) == 1:
        return [nums]

    # 结果列表，用于存储所有排列
    result = []

    # 遍历列表中的每个元素
    for i in range(len(nums)):
        # 选择当前元素作为排列的第一个元素
        current_num = nums[i]

        # 从剩余元素中创建新列表，用于下一层递归
        remaining_nums = nums[:i] + nums[i+1:]

        # 对剩余元素递归调用permute函数，获取它们的所有排列
        for p in permute(remaining_nums):
            # 将当前元素添加到每一种剩余元素的排列之前，生成新的排列
            result.append([current_num] + p)
    return result
    
def Det(matrix_arr):
    '''计算矩阵（方阵）的行列式：输入为一个二维数组'''
    m_shape = matrix_arr.shape #获取矩阵形状
    # 判断是否为方阵
    if m_shape[0] != m_shape[1]:
        print("矩阵不是方阵，不存在行列式")
        return
    n = m_shape[0] # 矩阵为n*n方阵
    n_list = []
    for i in range(n):
        n_list.append(i)
    all_permutions = permute(n_list)# 获取全排列
    all_permutions = np.array(all_permutions) # 将列表转换为np.array数组

    result = 0
    for permution in all_permutions:
        invNum = inv_num(permution)# 计算该排列的逆序数
        # 计算各个排列的乘积
        product = 1
        for i in range(n):
            j = permution[i]
            a_ij = matrix_arr[i][j]
            product = product * a_ij
        product = (-1)**invNum * product
        #将全排列的乘积进行加和
        result = result + product
    return result

det = Det(D)
print("我的程序计算结果为：",det)
det1 = np.linalg.det(D)
print("python标准库函数计算结果为：",det1)


    
