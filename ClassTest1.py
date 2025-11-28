class Sender():
    def __init__(self):
        print("initialized")
        printer = Printer()
        printer.printHello()
        printer.printGay()
    
    def sendHello(self):
        print("method hello called")
        self.printer.printHello
    
    def sendGay(self):
        print("method gay called")
        self.printer.printGay

class Printer():
    def printHello(self):
        print("hello")
    def printGay(self):
        print("gay")

if __name__ == "__main__":
    Sender().__init__