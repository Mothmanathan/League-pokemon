class Moves:
    def __init__(self,name,damage,Mtype,scaling, info):
        
        # Damage >  a moves base damage
        
        # Mtype > moves type classification EX: dark fighting poison etc (these types will be replaced with league stand ins)
        
        # Scaling >  whether the move scales with attack damage or ability power
        
        # info > additonal effects that the move does
        self.name = name
        self.damage = int(damage)
        self.Mtype = Mtype
        self.scaling = scaling
        self.info = info
    def __str__(self):
        return "Move Name: "  + self.name + "\n" + "Damage: " + str(self.damage)  + "\n" \
               + "Move Type: " + str(self.Mtype)  + "\n"  + "Scaling: " + str(self.scaling) + "\n" + "Info: " + self.info
def getName(c):
    return c.name
def getDamage(c):
    return c.damage
def getMtype(c):
    return c.Mtype
def getScaling(c):
    return c.Scaling