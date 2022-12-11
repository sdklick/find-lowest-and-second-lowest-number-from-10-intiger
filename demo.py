#find lowest and second lowest number from 10 intiger
my_arr=[]
for x in range(10):
    userinput=int(input('enter number : '))
    my_arr.append(userinput)
print('you enter ',my_arr)
my_arr.sort()
print('lowest number is : ',my_arr[0])    
print('second lowest number is : ',my_arr[1])    