'''
foods = ['떡볶이','짜장면','라면','과자','맥주','치킨','삼겹살']
sides = ['오뎅','단무지','김치']
appetizes = ['콜라','커피','사이다']

for food, side, appetize in zip(foods,sides,appetizes) :
    print(food, '-->', side ,'-->', appetize)
    
dic = dict(zip(foods,sides))
'''

oldList = ['짜장면','탕수육','군만두']
newList =  list(oldList[:])
oldList[0] = '짬뽕'

