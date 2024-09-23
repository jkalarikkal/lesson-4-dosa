listy = [1,2,3,4,5,6,7,8,9,10]
flag = False
ques = int(input("What number are you looking for?"))

for i in range (0,len(listy)):
#len is used for finding the member amount of a list
    if ques == listy[i]:
        print('Yes your key exists')
        flag = True
        break

if flag == False:
    print("Key not found")