#https://www.codewars.com/kata/explosive-sum/python
def exp_sum(n):
  if n < 0:
    return 0
  dp = [1]+[0]*n #генерируем таким образом список,
  for num in range(1,n+1):
    for i in range(num,n+1):
      dp[i] += dp[i-num]

  print(dp[-1])
  return dp[-1]

exp_sum(10)#, 42