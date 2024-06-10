import time

print("Greetings")

get_time=time.strftime("%H")
#g=str(greet_time)
def greets():
    if get_time>="4" and get_time<="12":
        print("Good Morning")
    elif get_time>="13" and get_time<="16":
        print("Good Afternoon")
    elif get_time>="17" and get_time<="24":
        print("Good Evening")
    else:
        print("Good Night")
greets()        