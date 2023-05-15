# your code 를 지우고 코드를 작성하세요.
# 7주차 과제에는 출력이나 입력을 요구하는 문제가 없습니다. print(), input() 사용하지 마세요.
# 코드 실행 시 컴파일 에러, 런타임 에러가 발생하면 해당 문제 0점 처리하겠습니다.
# 함수 이름 변경하지 마세요. 변경 시 해당 문제 0점 처리 하겠습니다.
# 제출 기한: 2023년 5월 15일 23시 59분
# 지각 제출 기한: 2023년 5월 16일 23시 59분
# 3번 문제는 table을 사용해 풀이해주세요. (dictionary 활용) 다른 방법으로 구현하면 감점 또는 0점 처리하겠습니다.

# 1번
def relativeComp(a, b):
    if sorted(a-b) == []:
        return 0
    else:
        return sorted(a-b)
        
    
    
# 2번
def alphabetFreq(word):
    table = {}
    Word = list(word.upper())
    for i in Word:
        if i in table:
            table[i] +=1
        else:
            table[i] = 1
    K = [k for k, v in table.items() if max(table.values()) ==v]
    if len(K) != 1:
        return '?'
    else:
        return ', '.join(K)
   
