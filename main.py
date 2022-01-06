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
print('🎱',  brr[2:4])

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

# ------------------------------------------------------------------
# 튜플
# 1. 한 번 선언되면 변경 X
# 2. 소괄호 선언 ()
a = (1,2,3,4)
print(a)

# dict
data = dict()
data["사과"] = 'Apple'
data["바나나"] = 'Banana'
print(data["사과"])
# 1) 메서드
# keys(), values()

# Iterable 자료형
# 순차적인 정보를 담는 자료형
# in 문법 사용 가능

# SET **
# 1. 중복 허용 X
# 2. 순서없음
# 3. |, &, - : 합, 교, 차집합
# 4. add(4), update([5,6]), remove(3)
data2 = set([11,11,11,12,13,13])
print(data2)

# ------------------------------------------------------------------
# 1. 조건
# list, dict, tuple, set과 같은 interable자료형에는 in, not in 자주 쓴다
# if score>=10 : ~~~ else if score >= 20 : ~~~~~
# result = "Success" if score >= 80 else "fail" **

# 2. 반복문(while, for~in)

# 3. 함수
# def func(param) :
# 1) global 키워드 : 함수 안에서 함수 밖의 변수를 쓰고자할 때, 'global a' 선언 후, 로직에 쓴다.
# 2) 람다식 : print((lambda a,b : a+b)(3,7))

# 4. 입출력
# 1) input() : 한 줄의 문자열 입력
# 2) list(map(int, input().split())) **
# n, m, k = map(int, input().split())
# print(n, m, k)
# 3) sys.stdin.readline().rstrip() : 한 줄씩 입력, import sys 수반
# 4) 출력 : print(f"정답은 {answer}입니다.")

# ------------------------------------------------------------------

# 내장함수 / itertools / heapq / bisect / collections / math

# 1. 내장함수(sum, min, max, eval, sorted)
result_sum = sum([1, 2, 3])
print(result_sum)

result_min = min(1, 2, 3, 4, 5, 6)
print(result_min)

# eval : 문자열 형식의 수식을 계산
result_eval = eval('3+7-2')
print(result_eval)

# 2. intertools : 반복되는 데이터 처리

# 1) permutations : iterable 자료형에서 n개 뽑았을 나오는 경우의 수 모두 뽑아줌
from itertools import permutations
data = ['a', 'b', 'c']
result_permu = list(permutations(data, 3))
print('🐤', result_permu)

# 2) combinations : iterable 자료형에서 n개를 뽑았을 때 '순서를 고려하지 않은' 경우의 수
# 2-1) combinations_with_replacement : combintions에서 중복만 허용
from itertools import combinations
result_comb =list(combinations(data, 2))
print(result_comb)

# 3) product : iterable 자료형에서 n개를 뽑았을 때 '중복하여' 경우의 수!
from itertools import product
result_prod = list(product(data, repeat=2))
print(result_prod)


# 3. heapq : 힙 기능 위해 사용
import heapq
def heapsort(iterable):
    h = []
    result_heap = []
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result_heap.append(heapq.heappop(h))
    return result_heap

result = heapsort([1, 55, 2, 3, 4, 22, 12 ,5,])
print(result)

# 4. bisect : 이진탐색, 정렬된 배열에서 특정한 원소를 찾아야 할 때 효과적
from bisect import bisect_left, bisect_right
arr_bis = [1, 2, 3, 4, 5, 9]
x = 4
print(bisect_left(a, x))
print(bisect_right(a, x))

# * 특정한 범위 내의 원소 개수 구하는데 효과적 : count_by_range
def count_by_range(arr, leftValue, rightValue):
    left = bisect_left(arr,leftValue)
    right = bisect_right(arr, rightValue)
    return right-left

print("🐯",count_by_range(arr_bis, 2, 5))


# collections : deque(큐), counter
# 리스트는 가장 앞쪽에 원소를 추가, 삭제할 때 O(N)이지만, 큐는 O(1) **
# popleft, pop, appendleft(x), append(x)
from collections import deque
data_deque = deque([2, 3, 4]);
data_deque.appendleft(11)
data_deque.append(44)
print('🏀🏀🏀🏀', list(data_deque))

# Counter : iterable 자료형에서 원소가 총 몇 번 나왔는지 확인
from collections import Counter
data_Counter = Counter(['red', 'orange', 'yellow', 'green', 'blue', 'red'])
print(data_Counter['red'])
print(dict(data_Counter))


# math : 팩토리얼, 제곱근, 최대공약수

# factorial(x)
import math
print(math.factorial(5))

# sqrt(x) : 제곱근 반환
# gcd(x,y) : 최대 공약수
# pi, e : 파이나 자연상수






