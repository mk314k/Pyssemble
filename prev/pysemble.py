
class Assembly():
    def __init__(self) -> None:
        self.memory={}
        pass
    def lui(rd, luiconstant):
        pass
    def jal(rd,label):
        pass
    def jalr(rd,offset,rs1):
        pass
    def beq(rs1,rs2,label):
        pass
    def bne(rs1,rs2,label):
        pass
    def blt(rs1,rs2,label):
        pass
    def bge(rs1,rs2,label):
        pass
    def bltu(rs1,rs2,label):
        pass
    def bgeu():
        pass

class memory():
    def __init__(self) -> None:
        self.storage=[]
    def __getitem__(self,key):
        assert(key>=0 and key%4==0,"inalid memory reference, expected address to be positive")
        key=int(key/4)
        return self.storage[key]
    def __setitem__(self,key,value):
        #assert(len(self.storage)<2048 or len(self.storage[-1])<32,"memory full")
        if (key<0 or key%4!=0):
            raise Exception("inalid memory reference, expected address to be positive")
        key=int(key/4)
        for i in range(key-len(self.storage)+1):
            self.storage.append(None)
        self.storage[key]=value
        return