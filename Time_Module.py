import time
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

localtime = time.asctime(time.localtime(time.time()))
print(localtime)