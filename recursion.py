# 재귀함수를 이용한 (프랙탈?)트리 그리기
# DFS(Depth First Search)
import turtle as t

def tree(depth, br_len) :
    if depth > 3 : return
    t.forward(br_len*0.9)
    t.left(20)                # 좌로 20도 방향
    tree(depth+1, br_len*0.9)
    t.right(40)
    tree(depth+1, br_len*0.9)
    t.left(20)
    t.backward(br_len*0.9)

t.left(90)
tree(0, 100)
t.done()
