# ask user the limit and then find prime nos 

x=int(input("enter range to chk prime nos"))

for i in range(2,x):
    prime=1
    for j in range(2,i):
        if i%j == 0:
            prime=0
            break
    if prime==1:
            print(i,end=" ")
            
        
    
            
