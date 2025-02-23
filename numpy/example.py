import numpy as np

list_data = [1, 2, 3]
array = np.array(list_data)

print(array)
print(array.size)
print(array.dtype)
print(array[2])

# 0부터 3까지의 배열 만들기
array1 = np.arange(4)
print(array1)

array2 = np.zeros((4, 4), dtype=float)
print(array2)

array3 = np.ones((3, 3), dtype=str)
print(array3)

# 0부터 9까지 랜덤하게 초기화 된 배열 만들기
array4 = np.random.randint(0, 10, (3, 3))
print(array4)

# 평균이 0이고, 표준편차가 1인 표준 정규를 띄는 배열
array5 = np.random.normal(0, 1, (3,3))
print(array5)

array6 = np.array([1, 2, 3])
array7 = np.array([4, 5, 6])
array8 = np.concatenate([array6, array7])
print(array8)

array9 = np.array([1, 2, 3, 4, 5, 6])
array10 = array9.reshape((2,3))
print(array10)

arr1 = np.arange(4).reshape(1, 4)
arr2 = np.arange(8).reshape(2, 4)

arr3 = np.concatenate([arr1, arr2], axis=0)
print(arr3)

left, right = np.split(arr2, [2], axis=1)
print(left.shape)
print(right.shape)
print(left)



