# mutable(변경 가능한 객체) : list, set, dict
# immutable(변경 불가능한 객체) : int, float, str, tuple


#####################################################
# 예제1 - immutable 객체
a = 10
b = a

print(a, id(a))
print(b, id(b))

b = 30
print(a, id(a))
print(b, id(b))


#####################################################
# 예제2 - mutable 객체
A = [1, 2, 3]
B = A

print(A, id(A))
print(B, id(B))

B[0] = 10
print(A, id(A))
print(B, id(B))


#####################################################
# 예제3 - call by value
def immutable_data(aa) :
    aa = aa + 10
    return

a = 20
immutable_data(a)  # call by value
print(a)


#####################################################
# 예제4 - call by reference
def mutable_data(LL) :
    LL[0] = LL[0] + 1
    return

L = [10, 20, 30]
mutable_data(L)    # call by reference
print(L)
