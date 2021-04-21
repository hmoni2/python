'''
mylist = [30,10,20]
mylist.append(40)

a = mylist.pop()
mylist.sort()
mylist.insert(2,222)
mylist.remove(222)
#만약 리스트 안의 없는 요소를 지우고자 하면 에러 출력
mylist.extend([77,78,79])
'''
'''
list1 = []
list2 = []

value = 0
for i in range(0,4) :
    for k in range(0,5) :
        list1.append(value)
        value += 3
    list2.append(list1)
    list1 = []

for i in range(0,3):
    for k in range(0,4) :
        print("%3d" % list2[i][k], end = " ")
    print(" ")

#%%
aa = [[1,2,3,4],[5,6],[7,8,9]]
print(aa)
# %%
tt1 = [10,20,30,40]
print(tt1[1:3])
print(tt1[1:4])
# %%
myTuple = [10,20,30]
myList = list(myTuple)
myList.append(40)
myTuple = tuple(myList)
print(myTuple)
'''
#%%
'''
student1 = {'학번': 1000,'이름':'홍길등','학과':'컴퓨터학과'}
student1['연락처'] = '010-1111-2222'
student1

student1['학과'] = '파이썬학과'
del student1['학과']
student1

print('이름' in student1)
#student1 = {'학번': 2000,'이름':'홍길등','학과:':'컴퓨터학과'}
'''
#print(student1['학번']) #키 값에 접근할 때 많이 사용
#print(student1.get('학번'))
#print(student1.keys())
#print(student1.values())
# %%
'''
singer = {}
singer['이름'] = '트와이스'
singer['구성원수'] = 9
singer['데뷔'] = '서바이벌 식스틴'
singer['대표곡'] = 'SIGNAL'

for k in singer.keys() :
    print('%s -> %s' %(k,singer[k]))
'''
foods = {"떡볶이":"오뎅","짜장면":"단무지","라면":"김치","피자":"피클"};

while True:
    myFood = input("좋아하는 음식은?")
    if myFood in foods:
        print('%s => %s' % (myFood,foods.get(myFood)))
    elif myFood == 'end':
        break
    else :
        print("그런 음식없음")

        
mySet1 = {1,2,3,4,5}
mySet2 = {1,'삼각김밥','바나나'}
print(mySet1.intersection(mySet2))
print(mySet1.union(mySet2))
print(mySet1.difference(mySet2))
print(mySet1.symmetric_difference(mySet2))

numlist = []
for num in range(1,10):
    numlist.append(num)

numlist

numlist = [num for num in range(1,21) if (num % 3) == 0]

foods = ['떡볶이','짜장면','라면','피자','맥주','치킨','삼겹살']
sides = ['오뎅','단무지','김치']