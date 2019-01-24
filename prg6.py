s=input("enter emp code")


if len(s)==8 and s.isnumeric():
    s1=s[0:2]
    s2=s[2:4]
    s3=s[4:5]
    s4=s[5:]

    
    if s1=="10":
        loc="mumbai"
    elif s1=="20":
        loc="delhi"
    elif s1=="30":
        loc="chennai"
    else:
        print("wrong location no")
        
    if s2=="01":
        dep="accounts"
    elif s2=="02":
        dep="sales"
    elif s2=="03":
        dep="mfg"
    else:
        print("wrong dep")
        
    if s3=="1":
        cat="unskilled"
    elif s3=="2":
        cat="semi skilled"
    elif s3=="3":
        cat="staff"
    else:
        print("wrong categroy")
        
        
    print("\nemp location is   :",loc)
    print("\nemp department is :",dep)
    print("\nemp categroy is   :",cat)
    print("\nemp id is         :",s4)
        
   
else:
    print("code should be 8 digit and numeric")