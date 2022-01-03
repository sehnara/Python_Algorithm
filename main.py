# 실수 표현 : AeN - A * 10**N
print(30e2)

# round() 등장 : 컴퓨터는 이진법을 쓰기 때문에, 실수의 사칙연산 결과를 정확히 표현할 수 없다.
print(round(123.1234, 2))

# 연산자들 : +, -, *, /, %, //(몫)

# 리스트
# 1. 초기화
n = 10
arr = [0]*10
print(arr)

# 2. slice
brr = [1,2,3,4,5,4,2,9]
print(brr[2:4])

# 3. comprehension
crr = [i for i in range(20) if i%2 == 1]
print("🐸", crr)

# 3-1. 2차원 배열 초기화
m =4
n =3
drr =[[0] * m for _ in range(n)]
drr[1][1] = 33
print('🐔', drr)

# 3-2. 포함되지 않는 값만으로 초기화
arr1 = [1,2,3,4,5,6,7]
div = {1,2,3,4,5}

result = [i for i in arr1 if i not in div]
print('🌽', result)

# 메서드
brr.sort()
print(brr)
brr.sort(reverse=True)
print(brr)
brr.insert(2, 3)
print(brr)
# 특정값 세기
print(brr.count(3))
# 특정값 삭제
brr.remove(4)
print(brr)
