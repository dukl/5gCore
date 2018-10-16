import threading
def printHello():  
    print("start")  
    timer = threading.Timer(5,printHello)
    timer.start()
  
if __name__ == "__main__":  
    timer = threading.Timer(5,printHello)
    timer.start()
