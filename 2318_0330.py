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
a.replace("새해 복 많이 받으","집 가세")

#.upper/lower
a="python"
B="PYTHON"
a.upper()
B.lower()