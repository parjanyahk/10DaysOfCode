# Enter your code here. Read input from STDIN. Print output to STDOUT

num = input()

list =[]
for i in range(int(num)):
    q =input()
    op =int(q[0])
    if(op==1):
        s = q.split(' ')[-1]
        list.append(s)
    elif(op==2):
        list.pop(0)
    elif(op==3):
        print(list[0])