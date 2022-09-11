import random

def test(classNumber):
    classMates = []
    result = 0

    for x in range(classNumber):
        birthday = random.randint(0, 365)
        classMates.append(birthday)
    for x in range(classNumber):
        for i in range(classNumber):
            if x != i and classMates[x] == classMates[i]:
                result+=1

    return result

def record(classNumber, sameBirthday= 0):
    lucky = 0
    for n in range(0, 10000):
        if test(classNumber) > sameBirthday:
            lucky += 1
    word = '人数为{0}时，生日相同的人数大于{1}的可能性是{2}%!'.format(classNumber, sameBirthday, str(lucky)[:2])
    return word

number = input('请输入想测试的人数！')
print(record(20))
