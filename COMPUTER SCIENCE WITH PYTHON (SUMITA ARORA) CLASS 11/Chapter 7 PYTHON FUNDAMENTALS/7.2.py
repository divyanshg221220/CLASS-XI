#7.2
import datetime 
d=int(input("Enter today's date (only del part):"))
m=datetime.date.today().month
n={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
print("Days left:",n[m]-d)