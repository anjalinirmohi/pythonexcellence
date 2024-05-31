import threading

class distribution:
    def mma(self):
        for i in range(20):
            print("yesssss")
        
    def mom(self):
        for i in range(20):
            print("nooooooooooo")

obj = distribution()

thread1 = threading.Thread(target = obj.mma)
thread2 = threading.Thread(target = obj.mom)
print("i am women")
thread1.start()
thread2.start()
print("i am heroin")
thread1.join()
thread2.join()

print("i am  runnninggg...")

print("new process")

print("this is importnt code")


print("done.")
