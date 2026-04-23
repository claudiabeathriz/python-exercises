#N = int(input())

#if N < 1:
 #   print("Inválido")
#elif N == 1:
 #   print("[0]")
#else:
 #   fib = [0, 1]
  #  for i in range(2, N):
   #     fib.append(fib[i-1] + fib[i-2])
#print(fib)

N = int(input("Digite um número inteiro N: "))

a = 0
b = 1

for i in range(N):
    print(a, end=" ")
    a, b = b, a + b

for i in range(N):
    fibo_sum = 0
    fibo_sum += b

print(fibo_sum)