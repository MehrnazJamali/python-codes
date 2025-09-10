status = input("enter status: ")
number = status[0]
if len (status) == 3:
    if number == "1":
        print ("informational")
    elif number == "2":
        print ("success")
    elif number == "3":
        print ("redirect")
    elif number == "4":
        print ("client error")
    elif number == "5":
        print ("server error")
    else:
        print ("invalid status")
else:
    print ("your status codes is invalid!")
