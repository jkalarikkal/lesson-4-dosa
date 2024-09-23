listy = [1,2,3,4,5,6,7,8,9,10]

ques = int(input("What number are you looking for?"))

start = 0
end = (len(listy))-1
flag = False

while start <= end:
    midpoint = (start + end) // 2 
    if ques == listy[midpoint]:
        print("Key is found")
        flag = True
        break
    elif ques < listy[midpoint]:
        end  = midpoint - 1
    elif ques > listy[midpoint]:
        start =  midpoint + 1


if flag == False:
    print("Key dont exist")

