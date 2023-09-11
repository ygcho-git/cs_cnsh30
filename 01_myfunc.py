def SUM(a, b):    # a ~ b의 정수합 리턴
    return (a + b) * (b - a + 1) // 2


def SUM(a, b): # a ~ b의 정수합 리턴
    s = 0
    for i in range(a, b + 1):
        s = s + i
    return s


def isprime(n):   # n이 소수이면 True, 아니면 False리턴
    if n <= 1: return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def isprime(n): 
    if n <= 1: return False  # 1 이하는 소수일리 없음

    cnt = 0
    for i in range(1, n + 1):  # 1부터 n까지 약수가 몇개 존재하는지 확인
        if n % i == 0:
            cnt = cnt + 1

    if cnt == 2:
        return True  # 소수면, 1 ~ n까지 약수가 2개 존재함(1과 자기자신)
    else:
        return False

def listprint(L):    # 1차원 리스트 출력
    for i in range(len(L)):
        print(L[i], end=' ')


def listprint(L):    # 2차원 리스트 출력
    for i in range(len(L)):
        for j in range(len(L[0])):
            print(L[i][j], end=' ')
        print()


def listsum(L):    # 2차원 리스트의 합 리턴
    s = 0
    for i in range(len(L)):
        s = s + sum(len(L[0]))

    return s


def matrixsum(A, B) : # 두 행렬의 합 리턴
    C = [[0 for _ in range(len(A[0]))] for __ in range(len(A))]

    for i in range(len(A)) :
        for j in range(len(A[0])) :
            C[i][j] = A[i][j] + B[i][j]
    return C
