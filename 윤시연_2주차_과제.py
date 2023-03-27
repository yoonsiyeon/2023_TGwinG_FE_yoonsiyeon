# 1번
def sum(a, b):
    # your code 
    return a+b
print(sum())

# 2번
def sub(a, b):
    # your code
    return a-b
print(sub())

# 3번
def mul(a, b):
    # your code
    return a*b
print(mul())

# 4번
def div(a, b):
    # your code
    return a/b
print(div())

# 5번
def distance(x1, y1, x2, y2):
    # your code
    result = (x1-x2)**2+(y1-y2)**2
    return result**(1/2)
print(distance())


# 6번
def title(word):
    lylics = "Switch sides and I'm beside you."
    # your code
    return word[21:31]
lyrics= "Switch sides and I'm beside you."
print(title(lyrics))


# 7번
def reverseStr(string):
    # your code
    return string[::-1]
print(reverseStr(""))


# 8번
    # your code
var1=input("이름을 입력하세요:")
var2=input("취미를 입력하세요:")
var3=input("재학 중인 학교를 입력하세요:")
var4=input("생일을 입력하세요:")
print("이름은 {}입니다. 취미는 {}입니다. 저는 {}를 다니고 있습니다.제 생일은 {}월 {}일입니다.".format(var1, var2, var3, var4[3:4], var4[5:6]))
   
# 9번
def calc(a,b):
    # your code
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)
calc()