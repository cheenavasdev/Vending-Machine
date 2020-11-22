import webcam
import pyttsx3 
class cashregister:
    cashonhand=0
    def __init__(self,cash=1000):
        self.cashonhand=cash
    def Acceptamount(self,amount):
        self.cashonhand+=amount
    def Currentbalance(self):
        return self.cashonhand
class Dispenser:
    item=0
    cost=0
    def __init__(self,nitems=70,ncost=70):
        self.item=nitems
        self.cost=ncost
    def getitem(self):
        return self.item
    def getcost(self):
        return self.cost
    def makesale(self):
        self.item-=1
pepsi=Dispenser(100,35)
limca=Dispenser(100,40)
lays=Dispenser(50,20)
kitkat=Dispenser(50,25)
cr=cashregister(5000)
def Sellproduct(items,cr):
    if(items.getitem()==0):
        print("Out Of Stock")
        return
    else:
        ncost=items.getcost()
        print("cost of the item is:",ncost)
        amount=int(input("Enter Amount : "))
        if(amount>=ncost):
            items.makesale()
            cr.Acceptamount(ncost)
            engine = pyttsx3.init() 
            a="Thank you For Ordering"
            b=("please collect your balance amount:",amount-ncost)
            engine.say(a)
            engine.say(b) 
            engine.runAndWait()
        else:
            print("You Entered Wrong Amount")
def ShowMenu():
    print("1. Pepsi")
    print("2. Limaca")
    print("3. Lays")
    print("4. Kitkat")

    choice=int(input("Enter Choice : "))

    if(choice==1):
        Sellproduct(pepsi,cr)
    elif(choice==2):
        Sellproduct(limca,cr)
    elif(choice==3):
        Sellproduct(lays,cr)
    elif(choice==4):
        Sellproduct(kitkat,cr)
    elif(choice==98765):
        print("Available Stock")
        print("Pepsi : ", pepsi.getitem())
        print("Limca : ", limca.getitem())
        print("Fanta : ", lays.getitem())
        print("Lays : ", kitkat.getitem())
        print("Available Cash : ", cr.Currentbalance())
    else:
        print("Invalid Input")
ShowMenu()





