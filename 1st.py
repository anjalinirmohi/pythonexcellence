# import threading
# class dixit:
#     def sunitaa(self):
#         for i in range(15):
#             print("this is a dangerious thing to every person")
            
#     def ganga(self):
#         for i in range(15):
#             print("hahahahahah naaaannnnaaaaa")
             
             
# obj =  dixit()
# thread1 = threading.Thread(target=obj.sunitaa) 
# thread2 = threading.Thread(target=obj.ganga)

# print("how is it possible")

# print("could u have some coffee")

# thread1.start()
# thread2.start()

# print("what is this")


# thread1.join()
# thread2.join()



# print("i am anjali not sunitaa")
# print("she is my mother,insperation")
# print("ganga is my granee")





import threading
import time

class mythread(threading.Thread):
    def __init__(self,threasID,name.counter):
        threading.Thread.__init__(self)
        self.threadID
