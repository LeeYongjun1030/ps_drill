from functools import cmp_to_key

def ccw(p, p1, p2):
    x1, y1 = [p1[0] - p[0], p1[1] - p[1]]
    x2, y2 = [p2[0] - p[0], p2[1] - p[1]]
    return x1*y2 - x2*y1

def compare_dist(p1, p2):
    d1 = p1[0]**2 + p1[1]**2
    d2 = p2[0]**2 + p2[1]**2
    return d1 > d2

def comp(p1, p2):
    direction = ccw([0, 0], p1, p2)
    if direction > 0:
        return -1
    if direction == 0:
        if compare_dist(p1, p2):
            return 1
        else:
            return -1
    if direction < 0:
        return 1

n = int(input())

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append([x, y])

# 시작점 찾기
points = sorted(points, key=lambda x: (x[1], x[0]))
start = points[0]

# 시작점에 대한 상대좌표를 구해 정렬
shifted_points = [[x-start[0], y-start[1]] for x, y in points[1:]]
sorted_shifted_points = sorted(shifted_points, key= cmp_to_key(comp))
points = [[x+start[0], y+start[1]] for x, y in sorted_shifted_points]

# 볼록 껍질의 정점을 담아둘 스택
# 스택에 2개의 점을 넣어준다.
stack = [start, points[0]]

# 외적 결과의 z좌표의 음양 부호를 통해 ccw 여부를 판단
# 0인 경우는 선분 위의 점이라는 뜻이므로 배제해주어야 함
for p in points[1:]:
    while len(stack) > 1 and ccw(stack[-2], stack[-1], p) <=0:
        stack.pop()
    stack.append(p)
print(len(stack))