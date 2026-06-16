#7.13
def trafficLight():
    signal=input("Enter the colour of the traffic light: ")
    if (signal not in ("RED","YELLOW","GREEN")):
        print("Please enter a valid Traffic Light colour in CAPITALS")
    else:
        value=light(signal)
        if (value==0):
            print("STOP, Your Life is Precious.")
        elif (value==1):
            print("PLEASE GO SLOW.")
        else:
            print("GO!, Thank you for being patient.")
def light(colour):
    if (colour=="RED"):
        return (0)
    elif (colour=="YELLOW"):
        return (1)
    else:
        return (2)
trafficLight()
print("SPEED THRILLS BUT KILLS")