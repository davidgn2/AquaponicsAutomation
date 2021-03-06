import serial
ANALOGPORTS = 6

class Deserialise:
    
    def __init__(self):
        self.processedData = [None]*ANALOGPORTS
        try:
            self.arduino = serial.Serial('/dev/ttyACM0', 9600, timeout = 1)
            print("Connected to port0")
        except serial.SerialException as e:
            try:
                self.arduino = serial.Serial('/dev/ttyACM1', 9600, timeout = 1)
                print("Connected to port1")
            except serial.SerialException as e:
                print("Error! No serial connection. Please Check connection.")
                self.arduino = None
            
    def readLine(self):
        if (self.arduino is None):
            return None
        else:
            return self.arduino.readline()
        
    def updateValue(self):
        rawdata = []
        for i in range(0,ANALOGPORTS+1):
            rawdata.append(str(self.readLine()))
            
        for line in rawdata:
            #print(line)
            indexCharPos = line.find('a')+1
            startCharPos = line.find(' ')+1
            if indexCharPos != 0 and startCharPos != 0:
                index = int(line[indexCharPos])
                num = 0
                j = startCharPos
                while line[j].isdigit():
                    num = num*10
                    num = num + int(line[j])
                    #print(int(line[j]), end="")
                    j = j + 1
                
                self.processedData[index] = num
    def printAll(self):
        self.updateValue()
        for i in self.processedData:
            print(i)
    def readPort(self, port):
        self.updateValue()
        return self.processed[port]
                    
test = Deserialise()
test.printAll()
