inputs = list(input())
cnt = len(inputs) / 10
start = 0  
end = 10
time = 0
while time < cnt:
  print("".join(inputs[start:end]))
  start = start + 10
  end = end + 10
  time = time + 1
