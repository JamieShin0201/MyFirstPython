import numpy as np

# 단일 객체 저장 및 불러오기
array = np.arange(0, 10)
np.save('../saved.npy', array)

result = np.load('../saved.npy')
print(result)

# 복수 객체 저장 및 불러오기
array1 = np.arange(0, 10)
array2 = np.arange(10, 20)
np.savez('../saved.npz', array1=array1, array2=array2)
result = np.load('../saved.npz')
print(result['array1'])
print(result['array2'])

# numpy 원소 오름차순 정렬
array = np.array([5, 9, 10, 3, 1])
print(array)
array.sort()
print(array)

# 내림차순 (indexing 기법)
print(array[::-1])

# 각 열의 기준으로 정렬
array = np.array([[5, 9, 10, 3, 1], [8, 3, 4, 2, 5]])
print(array)
array.sort(axis=0)
print(array)

# 균일한 간격으로 데이터 생성
array = np.linspace(0, 10, 5)
print(array)

print(np.random.randint(0, 10, (2, 3)))
# 난수의 재연 (실행마다 결과 동일)
np.random.seed(7)
print(np.random.randint(0, 10, (2, 3)))


array1 = np.arange(0, 10)
array2 = array1
array2[0] = 99
print(array1)

# numpy 배열 객체 복사
array1 = np.arange(0, 10)
array2 = array1.copy()
array2[0] = 99
print(array1)

# 중복된 원소 제거
array = np.array([1, 1, 2, 2, 2, 3, 3, 4])
print(np.unique(array))


