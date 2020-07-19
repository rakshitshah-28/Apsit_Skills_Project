def validator(a,b,c):
    if int(a)>=9999 or int(a)<999:
        print("enter correct year")
    if int(b)>12 or int(b)<=0:
        print("enter correct month")
        exit(0)
    if int(c)>31 or int(c)<=0:
        print("enter correct date")
        exit(0)
    if int(b)==2 and (int(c)>29 or int(c)<=0):
        print("enter correct date")
        exit(0)
    if (int(b)==4 or int(b)==6 or int(b)==9 or int(b)==11 ) and (int(c)>30 or int(c)<=0):
        print("enter correct date")
        exit(0)
        
def day_calculator():       
    str1=input("To calculate number of days ->\nEnter the start day in yyyy/mm/dd format: ")
    str1=str1.strip()
    try:
        syr,smon,sday=str1.split("/")
    except:
        print("enter correct format")
        exit(0)
    validator(syr,smon,sday)
    str2=input("Enter the end day in yyyy/mm/dd format: ")
    str2=str2.strip()
    try:
        eyr,emon,eday=str2.split("/")
    except:
        print("enter correct format")
        exit(0)
    validator(eyr,emon,eday)
    from datetime import date
    start_date = date(int(syr),int(smon),int(sday))
    end_date = date(int(eyr), int(emon), int(eday))
    ans = end_date - start_date
    if int(ans.days)>0:
        print("Total number of days calculated :",str(ans.days))
    else :
        ans=-ans
        print("Total number of days calculated :",str(ans.days))
