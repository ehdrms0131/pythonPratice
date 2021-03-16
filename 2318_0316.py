p = input("비밀번호 : ")
a = "0610"
if p == a :
  print("문이 열렸습니다")

a = 3
if a>2 :
  print("a는 2 이상")

r = float(input("원의 반지름을 입력하세요"))
rod = round(2*3.14*r,2)
area = round(3.14*(r**2),2)
print("원의 둘레",rod,"cm, 원의 넓이",area,"cm")

n = input("이름: ")
h = float(input("키: "))
w = float(input("몸무게: "))
bmi = w/(h/100)**2
a=round(bmi,2)
print(n,"님의 키는",h,"cm이고 몸무게는",w,"kg입니다 BMI 지수는 ",a,"입니다")  

n = input("이름")
a = int(input("국어"))
b = int(input("수학"))
c = int(input("사회"))
d = int(input("과학"))
e = int(input("영어"))
sum = a+b+c+d+e
average = sum/5
print(n,"님의 성적은 총합" ,sum ,"점," ,"평균 " , average,"점 입니다")

a = int(input("피제수"))
b = int(input("제수"))
print("몫",a//b)

a = int(input("첫번째:"))
b = int(input("두번째:"))
print("두 숫자의 합은",a+b,"입니다")

a = input ("당신의 나이는? ")
print("당신은",a,"년을 살았습니다")
"방과후"*10

a = input("아무 숫자나 입력하세요 : ")
a

n = input("이름: ")
h = float(input("키: "))
w = float(input("몸무게: "))
bmi = w/(h/100)**2
a=round(bmi,2)

print(n,"님의 키는",h,"cm이고 몸무게는",w,"kg입니다 BMI 지수는 ",a,"입니다")

if a > 30 : 
  print("고도비만입니다")
elif a >25 and a<29.9 :
  print("비만")
elif a >24.9 and a>23 :
  printf("과체중")
else : 
  printf("정상")


i = int(input("자연수: "))
if i <= 0 :
  print("자연수가아닙니다")
elif i%2==1 : 
  print("홀수입니다")
else :
  print("짝수입니다")

sider = 700
coke = 800
water = 1200
money = int(input("얼마 있나요 "))
c = input("선택 1-사이다 2-콜라 3-물 ")

if money < 0 :
  print("돈이 없습니다")
elif i == 1:
  if money>cider:
    print("사이다가 나왔습니다. 덜컹")
    print("잔돈",money-700,"원 반환합니다")
  else :
    print("음료수를 뽑을 수 없습니다.")
    print("잔돈",money,"원 반환합니다")
elif i == 2:
  if money>cider:
    print("콜라가 나왔습니다. 덜컹")
    print("잔돈",money-800,"원 반환합니다")
  else :
    print("음료수를 뽑을 수 없습니다.")
    print("잔돈",money,"원 반환합니다")
else :
  if money>water:
    print("물이 나왔습니다. 덜컹")
    print("잔돈",money-1200,"원 반환합니다")
  else :
    print("음료수를 뽑을 수 없습니다.")
    print("잔돈",money,"원 반환합니다")
