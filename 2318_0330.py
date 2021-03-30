a="Strings in Python"
a[4:10]
#string slice

a= "Hello Python"
a[-1:-6]
a[-6:-1]

a = "Hello Python"
a[:5]
a[6:]
a[-6:]

#. check
a = ""
while a!='q':
  a=input("")
  if a[-1] == "." :
    print("온점입니다")
    print("온점을 잡 입력하셨습니다")
  else :
    print("온점을 입력하세요")

# space check
a=""
print("입력")
while a != 'q' :
  a=input("")
  print(a[0])
  for i in range(len(a)):
    if a[i] == " ":
      print(a[i+1])

# join
a="- -"
b= ["A","B","C","D"]
a.join(b)


#기존의 문자열 변수를 리스트로 분리
a="arc bug can dream elephant"
a.split(" ")
a="arc-bug-can-dream-elephant"
b=a.split("-")
b

#.replace
a= "사장 니도 새해 복 많이 받으세요"
a.replace("새해 복 많이 받으","집 가")

#upper/lower
a="python"
B="PYTHON"
a.upper()
B.lower()

#count 
a = "간장공장공장장짱"
a.count("장")

#문자열 위치
a="Ladies and Gentlemen, Welcome to Python world"

a.find("W")
a.index("W")
a.find("Boys")
#index()에 해당 문자가 없으면 오류
#a.index("Boys")

#strip (문자/공백제거)
a="아 정말 제가 할게요"
a.strip("아")

a = "        정답은 사과"
a.strip()

a= "A is apple"


#정렬 center ljust rjust
a= "A is apple"
a.center(20)

a.ljust(20)

a.rjust(20)

a.center(20,",")

#문자 위치 찾기
print("문서 작성") 
doc = input("")
word = input("찾을 문자를 입력 : ")
seq=0
for i in range(doc.count(word)):
  if doc.count(word) > 0:
    seq = doc.find(word,seq)
    print(doc[seq],seq+1,"/",doc.count(word))
    seq = seq+1


#숫자인지 문자인지 체크
a="12345"
a.isdigit()
a.isalpha()

#대소문자인지 체크
a="hello"
a.islower()
a="HELLO"
a.isupper()

#문자열 변수 안에 해당 문자가 들어 있는지 확인하는 가장 쉬운 방법은 [in] 해당 문자를 찾아 t/f  a=apple 이라고 했을 때 "pl" in a

#어절 개수 세기
print("문장 입력")
a=""
while a != "q":
  a = input("")
  spa = 1
  for i in range(len(a)):
    if a[i] == " ":
      spa = spa+1
  if a=="q":
    break
  print("이 문장은",spa,"어절입니다")

#띄어쓰기로 자료 순서를 입력하고,자료 형식이 틀리면 재입력 요구
a=1
while a==1:
  a=input("DATA Input")
  a=a.split(" ")
  if a[0].isalpha()==1 and a[1].isdigit()==True and a[2].isalnum():
    a[0]=a[0].upper()
    a[2]=a[2].capitalize()
    print(a)
  else:
    a=1