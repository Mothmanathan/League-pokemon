class Champions:
    def __init__(self,name, hp, ad, ap):
        self.name = name
        self.hp = int(hp)
        self.ad = int(ad)
        self.ap = int(ap)
        
    def __str__(self):
        return "Champion: "  + self.name + "\n" + "HP: " + str(self.hp)  + "\n" \
               + "AD: " + str(self.ad)  + "\n"  + "AP: " + str(self.ap)
    
        
def getName(c):
    return c.name

def getHp(c):
    return c.hp

def SetHp(c, newHp):
    c.hp = newHp

def getAD(c):
    return c.ad

def setAd(c):
    return c.ad

def getAP(c):
    return c.ap
    
def setAP(c):
    return c.ap


