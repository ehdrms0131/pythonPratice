i = 0
while i<5 :
  print("한동근")
  i += 1

i = 0
while i<31 :
  print(i%4)
  i += 1

i=0
j=1
fibo = 0
while fibo<100:
  print(i)
  fibo = i+j
  i=j
  j=fibo

name = ""
while name != "q" :
  name = input("이름 입력 'q'입력시 종료")
  print(name)

n = ""
a=23
while n != a :
  n=input("숫자 입력")
  if n==a :
    print(정답)
  elif a<n :
    print("DOWN")
  else :
    print("UP")

n = ""
a=23
while n != a :
  n = int(input("숫자 입력"))
  if n==a :
    print("정답")
  elif a < n :
    print("DOWN")
  else :
    print("UP")

from random import *
p = ""
print("아무키를 누르면 주사위가 던져집니다. 종료는 q입니다")
while p != 'q':
  d = randint(1,6) 
  print(d)
  p=input("입력")

i
i = int(input("단"))
while i != 0 :
  j = 1
  while j < 10 :
    print(i,"x",j,"=",i*j)
    j += 1
  i = int(input("단"))