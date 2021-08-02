start_time = datetime.now()
def python_func ():
  import random
  def fill (x,y):
      b = []
      d = 1
      for row in range (x):
          b.append([])
          for elem in range(y):
              b[row].append(random.randint(1,3))
      return b

  x = 100
  y = 100
  z = 100
  q = 100

  matr1 = fill(x, y)
  matr2 = fill(z, q)

  print("\nВывод матрицы 1:")
  for i in matr1:
      print(' '.join(map(str, i)))

  print("\nВывод матрицы 2:")
  for i in matr2:
      print(' '.join(map(str, i)))

  subt_matrix = []
  for row3 in range(x):
      subt_matrix.append([])
      for elem3 in range(y):
          subt_matrix[row3].append(0)

  for row2 in range(x):
      for elem2 in range(y):
          subt_matrix[row2][elem2] = matr1[row2][elem2] * matr2[row2][elem2]

  print("\nВывод матрицы 3:")
  for i in subt_matrix:
      print(' '.join(map(str, i)) )

print(python_func())


end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))