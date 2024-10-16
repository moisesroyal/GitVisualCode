def sum_with_range(min, max):
  print(min, max)
  sum = 0
  for x in range(min, max):
    sum += x
  return sum

result = sum_with_range(1, 15)
print(result)
result_2 = sum_with_range(result, result + 7)
print(result_2)