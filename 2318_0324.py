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

  n = 0
while n != 1:
  n = int(input("숫자입력"))
  i = 1
  s = 0
  while i <= n:
     s += i
     i += 1
  print(s)

  p = 100
while p > 0 :
  d = int(input("얼마의 데미지를 입히시겠습니까"))  
  p -= d
  print("주인공의 체력은",p)
  if p > 0 :
    break
print("주인공이 죽었습니다")

l = ["아","점","저","야"]
while a != 0 :
  a = int(input("며칠이 지났습니까?"))
  for i in l : 
    print(a * i)

    n = 0
j = [10,30,61,70,90]
print("2020 제2회 한국사 시험 결과")
for i in j :
  n += 1
  if i >= 70 :
    print(n,"1급")
  elif i >= 60:
    print(n,"2급")
  else :
    print(n,"불합격")