def cases():
    confirm_cases=int(input("How many person affected by COVID-19: "))
    death_cases=int(input("How many persons died by COVID-19: "))
    death_rate=(((death_cases)/confirm_cases)*100)
    death=int(death_rate)
    print(f"DEATH RATE : {death_rate} %")
    if 30<death>=50:
        print(f"{death_rate} % of people are dying so te condition is bad")
    elif death<=30:
        print("The condition is not bad")
    else:
        print("The condition is too bad")
        
def vaccine():
    total_people=int(input("Total number of people in that place: "))
    vaccinate_people=int(input("How many people vaccinated: "))
    vaccinate_rate=(((vaccinate_people)/total_people)*100)
    vaccinate=int(vaccinate_rate)
    print(f"The vaccination rate is {vaccinate_rate} %")
    if 30<vaccinate>=50:
        print(f"Congrats You have made {vaccinate_rate}")        
    elif vaccinate<=30:
        print("Make people aware of vaccination")
    else:
         print(f"Congrats You did a great job that you made {vaccinate_rate}")
         
def start():
    print("-----COVID-19 DATA MANAGEMENT-----")
    user=input("1.OFFICER\n2.PEOPLE\nWho you are: ").upper()   
    if user=="OFFICER":
        user_name="OFFICER"
        pass_word="COVID"
        username=input("Enter your username: ").upper()
        password=input("Enter your password: ").upper()
        login()
    elif user=="PEOPLE":
        print("-----Welcome To COVID DATABASE-----")
        data()
    else:
        print("Sorry Invalid Option")
         
def login():
    if user_name==username and pass_word==password:
        print("-----Log-In Successfully-----")
        print("-----WELCOME TO OUR COVID-19 DATA MANAGEMENT-----")
        print("What information you wants to upload\n1.COVID CASES\n2.COVID VACCINATION\n3.BOTH")
        user_1=int(input("Enter the number to upload the information: "))
        if user_1==1:
            print("-----Here upload information for COVID CASES-----")
            cases()
        elif user_1==2:
            print("-----Here upload information for COVID VACCINE")
            vaccine()
        elif user_1==3:
            print("-----Here upload information for COVID CASES & VACCINE")
            cases()
            vaccine()
        else:
            print("Invalid Option")
            ask=input("Do you want to continue: ").lower()
            if ask=="yes":
                start()
            else:
                print("Thanks for visiting")
            
    elif user_name==username and pass_word!=password:
        print("Invalid password")
    elif user_name!=username and pass_word==password:
        print("Invalid username")
    else:
        print("Invalid username and password")
    
def data():
    print("1.Tirunelveli\n2.Kanniyakumari\n3.Trichy\n4.Madurai\n5.Chennai\n6.Coimbatore")
    tirunelveli=100
    kanniyakumari=210
    trichy=300
    madurai=500
    chennai=1200
    covai=1110
    place=int(input("Enter the number :"))
    if place==1:
        print(f"No of covid cases: {tirunelveli} ")
        if 0<tirunelveli<=100:
            print("No Strict Rules are there")
        elif 100<tirunelveli<=200:
            print("Avoid Unnecessary traveling")
        elif 200<tirunelveli<=500:
            print("Avoid Unnecessary Traveling\nIf you want to travel you must need vaccination certificate")
        elif 500<tirunelveli>1000:
            print("Strictly not allowed for traveling")
        else:
            print("Strictly following Lock down")
    elif place==2:
        print(f"No of covid cases:{kanniyakumari}")
        if 0<kanniyakumari<=100:
            print("No Strict Rules are there")
        elif 100<kanniyakumari<=200:
            print("Avoid Unnecessary traveling")
        elif 200<kanniyakumari<=500:
            print("Avoid Unnecessary Traveling\nIf you want to travel you must need vaccination certificate")
        elif 500<kanniyakumari>1000:
            print("Strictly not allowed for traveling")
        else:
            print("Strictly following Lock down")
    elif place==3:
        print(f"No of covid cases:{trichy} ")
        if 0<trichy<=100:
            print("No Strict Rules are there")
        elif 100<trichy<=200:
            print("Avoid Unnecessary traveling")
        elif 200<trichy<=500:
            print("Avoid Unnecessary Traveling\nIf you want to travel you must need vaccination certificate")
        elif 500<trichy>1000:
            print("Strictly not allowed for traveling")
        else:
            print("Strictly following Lock down")
    elif place==4:
        print(f"No of covid cases:{madurai}")
        if 0<madurai<=100:
            print("No Strict Rules are there")
        elif 100<madurai<=200:
            print("Avoid Unnecessary traveling")
        elif 200<madurai<=500:
            print("Avoid Unnecessary Traveling\nIf you want to travel you must need vaccination certificate")
        elif 500<madurai>1000:
            print("Strictly not allowed for traveling")
        else:
            print("Strictly following Lock down")
    elif place==5:
        print(f"No of covid cases:{chennai}")
        if 0<chennai<=100:
            print("No Strict Rules are there")
        elif 100<chennai<=200:
            print("Avoid Unnecessary traveling")
        elif 200<chennai<=500:
            print("Avoid Unnecessary Traveling\nIf you want to travel you must need vaccination certificate")
        elif 500<chennai>1000:
            print("Strictly not allowed for traveling")
        else:
            print("Strictly following Lock down")
    elif place==6:
        print(f"No of covid cases:{covai}")
        if 0<covai<=100:
            print("No Strict Rules are there")
        elif 100<covai<=200:
            print("Avoid Unnecessary traveling")
        elif 200<covai<=500:
            print("Avoid Unnecessary Traveling\nIf you want to travel you must need vaccination certificate")
        elif 500<covai>1000:
            print("Strictly not allowed for traveling")
        else:
            print("Strictly following Lock down")
    else:
        print("Invalid option")
        tell=input("Do you want to continue: ").lower()
        if tell=="yes":
            start()
        else:
            print("Thanks for visiting")
        
print("-----COVID-19 DATA MANAGEMENT-----")
user=input("1.OFFICER\n2.PEOPLE\nWho you are: ").upper()   
if user=="OFFICER":
    user_name="OFFICER"
    pass_word="COVID"
    username=input("Enter your username: ").upper()
    password=input("Enter your password: ").upper()
    login()
elif user=="PEOPLE":
    print("-----Welcome To COVID DATABASE-----")
    data()
else:
    print("Sorry Invalid Option")    


