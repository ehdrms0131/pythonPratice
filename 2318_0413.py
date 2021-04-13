#function
def hello():
  print("hello")
hello()

def sum():
  a=2
  b=2
  print(a+b)
sum();

#function + return
def hello(name,place="파이썬"):
  print("%s님 안녕하세요, %s에 오신 것을 환영합니다."%(name,place))
  return name;
user = hello("동근")

user = hello("동근","DirectX")

#function + * 
def apark(*calloff):
  print("오늘",calloff,"은(는) 운행하지 않습니다")

apark("청룡열차")
apark("청룡열차","자이로드롭")

#function + * + for
def Todaymenu(*menu):
  print("오늘의 메뉴")
  for i in range(len(menu)):print(menu[i])
  print("Service Charge, VAT 10% will be added")
Todaymenu("만두","김치","김치만두")

#function + * + for + len
def shift(*name) :
  worker = len(name)
  print("교대 근무자의 수는 %d명입니다. 순서대로"%(worker))
  for a in name:
      print(a)
shift("a","b","c")

#lambda
def Get10Mp(x):
  return x*10
Get10Mp(3)

(lambda x: x*10)(3)

#type change
a=["123","456","789"]
print(type(a[0]),type(a[1]),type(a[2]))

a=list(map(int,a))
print(type(a[0]),type(a[1]),type(a[2]))

#(lambda 매개변수:매개변수 처리식)(인자)
#(lambda x : x*10)(3,5,7,9)
a = list(map(lambda x :x*10 ,(3,5,7,9)))
a
#x의 y승

def distance(x=0,y=0):
  if x==0 and y == 0:
    x = int(input("x좌표 입력 : "))
    y = int(input("y좌표 압력 : "))
  c = (x**2 + y**2) ** 0.5 #루트 표현
  return c
#피타고라스
distance(3,4)

distance()