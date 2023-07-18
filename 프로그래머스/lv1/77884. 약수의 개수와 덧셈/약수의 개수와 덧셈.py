# 약수를 구하는 방법
    # 정수 n 을 1 ~ n 에 해당하는 숫자로 나누었을 때 나머지가 0이 된다면 정수 n 의 약수이다.
    # 예를 들어,  28을 1 부터 28 까지 숫자로 나누었을 때 나머지가 0이면 28의 약수이다.

def count(n):    # 약수의 합을 구하는 함수 solution이 받는 매개변수는 정수 n 이다.
    answer = 0      # 약수의 합을 넣을 변수를 정의했다.
    for i in range(1, n + 1):        # 정수 n을 1부터 n에 해당하는 숫자(range(1, n+1))로 나누는 반복 작업(for)을 통해 약수(i)를 찾을 것이다.
        if n % i == 0:               # 정수 n을 i로 나누었을 때 나머지가 0 이라면, (i는 n의 약수에 해당하므로)
            answer += 1     # 약수의 갯수 추가 
    return answer                    # if 절이 끝나면 for문이 약수의 갯수를 반환

def solution(left, right):
    answer = 0
    num = [i for i in range(left, right+1)]
    for i in range(len(num)):
        if count(num[i]) % 2 == 0:
            answer += num[i]
        else:
            answer -= num[i]
    return answer