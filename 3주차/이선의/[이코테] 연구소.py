'''
새로 세울 수 있는 벽의 개수 3개(반드시 3개)
바이러스가 퍼질 수 없는 곳 = 안전 영역
안전 영역의 크기를 구할 것
'''
import copy
from collections import deque

n, m = map(int, input().split())
v = [list(map(int, input().split())) for _ in range(n)]
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = 0

def bfs():
    global ans
    tv = copy.deepcopy(v)
    q = deque()
    for i in range(n):
        for j in range(m):
            if tv[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for d in dxy:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < n and 0 <= ny < m:
                if tv[nx][ny] == 0:
                    tv[nx][ny] = 2
                    q.append((nx, ny))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if tv[i][j] == 0:
                cnt += 1
    ans = max(cnt, ans)
def solution(cur):
    if cur == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if v[i][j] == 0:
                v[i][j] = 1
                solution(cur+1)
                v[i][j] = 0

solution(0)
print(ans)