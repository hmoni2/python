import random

lotto = []
getnumber = 0
top = 0

def random_number() :
  
    for i in range(0,6) : 
        getnumber = random.randrange(1,46)
        if lotto.count != 0 : 
            lotto.append(getnumber)
    lotto.sort() 

        
#MAIN#
print("** 로또 추첨을 시작합니다. **")
random_number()

print("추첨된 로또 번호 == > ", lotto)