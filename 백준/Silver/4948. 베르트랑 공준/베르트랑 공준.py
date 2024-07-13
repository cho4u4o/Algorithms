class prime:
  def __init__(self, n):
    self.n = n
    self.check = [True] * (2 * n + 1)
    self.cnt = 0

  def prime_check(self):
    for i in range(2, self.n * 2 + 1):
      if self.check[i]:
        for j in range(i, self.n * 2 + 1, i):
          self.check[j] = False
        if i > n:
          self.cnt += 1


result = []
while True:
  n = int(input())
  if n == 0:
    break
  else:
    p = prime(n)
    p.prime_check()
    result.append(p.cnt)
print(*result, sep='\n')