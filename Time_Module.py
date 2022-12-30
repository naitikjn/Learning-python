
# intial = time.time()
# k = 0
# while (k<45):
#      print("This is Trendy tech")
#      time.sleep(10)
#      k+=1
#
# print("While loop ran in", time.time() - intial,"seconds")
#
# intial2 = time.time()
# for x in range (45):
#    print("This is Trendy tech")
#    print("for loop ran in",time.time() - intial2,'seconds')

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)
import time
t = time.strftime('%H:%M:%S')
# hour = int(time.strftime('%H'))
# hour = int(input("Enter hour: "))
# print(hour)
#
# if(hour>=0 and hour<12):
#   print("Good Morning Sir!")
# elif(hour>=12 and hour<17):
#   print("Good Afternoon Sir!")
# elif(hour>=17 and hour<=24):
#   print("Good Night sir!")
print(t)