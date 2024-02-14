import sys

n = int(sys.stdin.readline())
points = []
for i in range(0, n):
    point = list(map(int, input().split()))  # 좌표를 point 리스트로 생성
    points.append(point)  # point 리스트를 points 리스트에 추가
points = sorted(points)  # 좌표의 x 좌표 기준 정렬
for j in range(0, n):
    print(*points[j])