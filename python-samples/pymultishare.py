from multiprocessing import Process, Value, Array

def f(n, a, start, end, name):
  print('In process ',name)
  n.value = 1.1
  for i in range(start, end):
    a[i] = -a[i]

if __name__ == '__main__':
  num = Value('d', 0.0)
  a = Array('i', range(10))

  p = Process(target=f, args=(num, a, 0, len(a)//2,'p'))
  q = Process(target=f, args=(num, a, len(a)//2, len(a),'q'))
  p.start()
  q.start()
  p.join()
  q.join()

  print(num.value)
  print(a[:])
