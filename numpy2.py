import numpy as np

array = np.random.randint(1, 10, size=4).reshape(2,2)
print(array)

result_array = array * 10;
print(result_array)

# 브로드캐스트 : 형태가 다른 배열을 연산할 수 있또록 배열의 형태를 동적으로 변환
array1 = np.arange(4).reshape(2, 2)
array2 = np.arange(2)
array3 = array1 + array2
print(array3)

array1 = np.arange(0, 8).reshape(2, 4)
array2 = np.arange(0, 8).reshape(2, 4)
array3 = np.concatenate([array1, array2], axis=0)
array4 = np.arange(0, 4).reshape(4, 1)
print(array3)
print(array3 + array4)

# numpy 마스킹 연산
array1 = np.arange(16).reshape(4, 4)
print(array1)

array2 = array1 < 10
print(array2)

array1[array2] = 100
print(array1)

# 집계함수
array = np.arange(16).reshape(4, 4)
print("최대값 : ", np.max(array))
print("최소값 : ", np.min(array))
print("합계 : ", np.sum(array))
print("평균값 : ", np.mean(array))

print(np.sum(array, axis=0))
print(np.sum(array, axis=1))
