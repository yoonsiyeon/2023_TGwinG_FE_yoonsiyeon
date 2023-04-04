# 1번
def grade(score):
    #your code
    if (score>=90):
        return("A")
    elif (score>=80):
        return("B")
    elif (score>=70):
        return("C")
    elif (score>=60):
        return("D")
    else:
        return("F")
    
print(grade())



# 2번
def quadrant(x, y):
    #your code
    if (x>0 and y>0):
        return("제 1사분면")
    elif (x<0 and y>0):
        return("제 2사분면")
    elif (x<0 and y<0):
        return("제 3사분면")
    elif (x>0 and y<0):
        return("제 4사분면")
    
print(quadrant())



# 3번
def leapYear(year):
    # your code
    if (year%4==0):
        if (year%400==0):
            return("윤년입니다.")
        elif ( year%100==0):
            return("윤년이 아닙니다.")
        else:
            return("윤년입니다.")
    else:
        return("윤년이 아닙니다.")

print(leapYear())

        

# 4번
def dice(a, b, c):
    # your code
    if (a==b==c):
        return (10000 + a*1000)
    elif (a!=b and c==a):
        return (1000 + c*100)
    elif (a!=b and c==b):
        return (1000 + c*100)
    elif (b!=c and a==b):
        return (1000 + a*100)
    elif (a!=b!=c):
        if (a>b and a>c):
            return (a*100)
        elif (b>a and b>c):
            return (b*100)
        elif (c>a and c>b):
            return (c*100)
        
print(dice())

    

    
    

# 5번
def alarm(time):
    #your code
    if (145<=time<1045):
        if (int(str(time)[1:])>45):
            return("{}시 {}분".format(str(time-45)[0:1], str(time-45)[1:]))
        else:
            return("{}시 {}분".format(str(time-45-40)[0:1], str(time-45-40)[1:]))
    elif (time>=1045):
        if (int(str(time)[2:])>45):
            return("{}시 {}분".format(str(time-45)[0:2], str(time-45)[2:]))
        else:
            return("{}시 {}분".format(str(time-45-40)[0:2], str(time-45-40)[2:]))
    elif (100<=time<145):
        return("0시 {}분".format(str(time-45-40)))
    elif (45<=time<100):
        return("0시 {}분".format(str(time-45)))
    elif (time<45):
        return("23시 {}분".format(str(time-45+60)))

print(alarm())


