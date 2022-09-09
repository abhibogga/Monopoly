import random
class space:
  def __init__(self,name,color,value,kind):
    self.name = ""
    self.color = ""
    self.value = 0
    self.kind = ""

board = []

go = space("","",0,"")
go.name = "Go"
go.value =200 
go.kind = "go"
board.append(go)

MeditAve = space("","",0,"")
MeditAve.name = "Mediteranean Avenue"
MeditAve.color = "brown"
MeditAve.value =60
MeditAve.kind = "property"
board.append(MeditAve)

ComChest1 = space("","",0,"")
ComChest1.name = "Community Chest"
ComChest1.kind = "community chest"
board.append(ComChest1)

BalticAve = space("","",0,"")
BalticAve.name = "Baltic Avenue"
BalticAve.color = "brown"
BalticAve.value =60 
BalticAve.kind = "property"
board.append(BalticAve)

Tax = space("","",0,"")
Tax.name = "Income Tax"
Tax.value =200
Tax.kind = "income tax"
board.append(Tax)

ReadRail = space("","",0,"")
ReadRail.name = "Reading Railroad"
ReadRail.value =200
ReadRail.kind = "property"
board.append(ReadRail)

OrienAve = space("","",0,"")
OrienAve.name = "Oriental Avenue"
OrienAve.color = "light blue"
OrienAve.value =100
OrienAve.kind = "property"
board.append(OrienAve)

Chance1 = space("","",0,"")
Chance1.name = "Chance"
Chance1.kind = "chance"
board.append(Chance1)

VerAve = space("","",0,"")
VerAve.name = "Vermont Avenue"
VerAve.color = "light blue"
VerAve.value =100
VerAve.kind = "property"
board.append(VerAve)

ConAve = space("","",0,"")
ConAve.name = "Connecticut Avenue"
ConAve.color = "light blue"
ConAve.value =120
ConAve.kind = "property"
board.append(ConAve)

Jail = space("","",0,"")
Jail.name = "Jail"
Jail.kind = "jail"
board.append(Jail)

CharPlace = space("","",0,"")
CharPlace.name = "St.Charles Place"
CharPlace.color = "pink"
CharPlace.value =140
CharPlace.kind = "property"
board.append(CharPlace)

ElecCom = space("","",0,"")
ElecCom.name = "Electric Company"
ElecCom.value =150
ElecCom.kind = "property"
board.append(ElecCom)

StaAve = space("","",0,"")
StaAve.name = "States Avenue"
StaAve.color = "pink"
StaAve.value =140
StaAve.kind = "property"
board.append(StaAve)

VirAve = space("","",0,"")
VirAve.name = "Virginia Avenue"
VirAve.color = "pink"
VirAve.value =160
VirAve.kind = "property"
board.append(VirAve)

PenRail = space("","",0,"")
PenRail.name = "Pennsylvania Railroad"
PenRail.value =200
PenRail.kind = "property"
board.append(PenRail)

JamePlace = space("","",0,"")
JamePlace.name = "St.James Place"
JamePlace.color = "orange"
JamePlace.value =180
JamePlace.kind = "property"
board.append(JamePlace)

ComChest2 = space("","",0,"")
ComChest2.name = "Community Chest"
ComChest2.kind = "community chest"
board.append(ComChest2)

TenAve = space("","",0,"")
TenAve.name = "Tennessee Avenue"
TenAve.color = "orange"
TenAve.value =180
TenAve.kind = "property"
board.append(TenAve)

NyAve = space("","",0,"")
NyAve.name = "New York Avenue"
NyAve.color = "orange"
NyAve.value =200
NyAve.kind = "property"
board.append(NyAve)

FreePark = space("","",0,"")
FreePark.name = "Free Parking"
FreePark.kind = "free parking"
board.append(FreePark)

KenAve = space("","",0,"")
KenAve.name = "Kentucky Avenue"
KenAve.color = "red"
KenAve.value =220
KenAve.kind = "property"
board.append(KenAve)

Chance2 = space("","",0,"")
Chance2.name = "Chance"
Chance2.kind = "chance"
board.append(Chance2)

FleeStr = space("","",0,"")
FleeStr.name = "Fleet Street"
FleeStr.color = "red"
FleeStr.value =220
FleeStr.kind = "property"
board.append(FleeStr)

TraSquare = space("","",0,"")
TraSquare.name = "Trafalgar Square"
TraSquare.color = "red"
TraSquare.value =240
TraSquare.kind = "property"
board.append(TraSquare)

FenStation = space("","",0,"")
FenStation.name = "Fenchurch St. Station"
FenStation.value =200
FenStation.kind = "property"
board.append(FenStation)

LeiSquare = space("","",0,"")
LeiSquare.name = "Leicester Square"
LeiSquare.color = "yellow"
LeiSquare.value =260
LeiSquare.kind = "property"
board.append(LeiSquare)

CovStr = space("","",0,"")
CovStr.name = "Coventry Street"
CovStr.color = "yellow"
CovStr.value =260
CovStr.kind = "property"
board.append(CovStr)

WatWorks = space("","",0,"")
WatWorks.name = "Water Works"
WatWorks.value =150
WatWorks.kind = "property"
board.append(WatWorks)

Piccad = space("","",0,"")
Piccad.name = "Piccadilly"
Piccad.color = "yellow"
Piccad.value =280
Piccad.kind = "property"
board.append(Piccad)

GoToJail = space("","",0,"")
GoToJail.name = "Go To Jail"
GoToJail.kind = "go to jail"
board.append(GoToJail)

RegStr = space("","",0,"")
RegStr.name = "Regent Street"
RegStr.color = "green"
RegStr.value =300
RegStr.kind = "property"
board.append(RegStr)

OxStr = space("","",0,"")
OxStr.name = "Oxford Street"
OxStr.color = "green"
OxStr.value =300
OxStr.kind = "property"
board.append(OxStr)

ComChest3 = space("","",0,"")
ComChest3.name = "Community Chest"
ComChest3.kind = "community chest"
board.append(ComChest3)

BonStr = space("","",0,"")
BonStr.name = "Bond Street"
BonStr.color = "green"
BonStr.value =320
BonStr.kind = "property"
board.append(BonStr)

LivSta = space("","",0,"")
LivSta.name = "Liverpool St. Station"
LivSta.value =200
LivSta.kind = "property"
board.append(LivSta) 

Chance3 = space("","",0,"")
Chance3.name = "Chance"
Chance3.kind = "chance"
board.append(Chance3) 

ParLan = space("","",0,"")
ParLan.name = "Park Lane"
ParLan.color = "blue"
ParLan.value =350
ParLan.kind = "property"
board.append(ParLan) 

SuTask = space("","",0,"")
SuTask.name = "Super Task"
SuTask.kind = "super task"
board.append(SuTask) 

MayFair = space("","",0,"")
MayFair.name = "May Fair"
MayFair.color = "blue"
MayFair.value =400
MayFair.kind = "property"
board.append(MayFair) 

players = int(input("How many players are there?"))
turn = 1
money = []
for i in range(players):
  money.append(1500)
propertys = []
for i in range(players):
  propertys.append([])
location = []
for i in range(players):
  location.append(0)
def next(turn,players):
  turn += 1
  if turn > players:
    turn = 1
  return turn
tasks = ["Advance to Go","Advance to St.Charles Place","Get out of Jail Free","Go back 3 spaces","Go to Jail","Pay each player 100 dollars"]
jailfree = []
jail= []
while True:
  print("Its player "+str(turn)+" turn" )
  input("Press enter to roll the dice!")
  dice = random.randint(2,12)
  if turn not in jail:
    
    spot = location[turn-1] + dice
    while spot>len(board):
      spot = spot - len(board)
  
  print("You rolled " +str(dice))
  if turn not in jail:
    print("You landed on " +board[spot].name )
  if board[spot].kind == "property":
    if money[turn-1]>board[spot].value:
      option = input("Would you like to purchase property?").lower()
      if option == "yes":
        board[spot].kind = "bought property"
        print("You have now bought property!")
        money[turn-1]-= board[spot].value
        propertys[turn-1].append(board[spot].name)
    else:
      print("Sorry you don't have enough money to buy this property")
  elif board[spot].kind == "bought property":
    for i in range(len(propertys)):
      if board[spot] in propertys[i]:
        owner = i+1
        break
    if board[spot].value > money[turn-1]:
      money[owner]+= money[turn-1]
      money[turn-1] = 0
    else:
      money[owner]+=board[spot].value
      money[turn-1]-=board[spot].value
    print("Sorry you have to give "+ str(board[spot].value)+" to player "+str(owner))
  elif board[spot].kind == "chance" or board[spot].kind == "community chest":
    card = random.choice(tasks)
    print("You drew " + card)
    if card == "Advance to Go":
      location[turn-1]=0
      money[turn-1]+=100
    if card == "Advance to St.Charles Place":
      location[turn-1]=board.index(CharPlace)
    if card == "Get out of Jail Free":
      jailfree.append(turn)
    if card == "Go back 3 spaces":
      location[turn-1]-=3
    if card == "Go to Jail":
      location[turn-1]=board.index(GoToJail)
      jail.append(turn)
      if turn in jailfree:
        print("You are out of Jail!")
        jailfree.remove(turn)
    if card == "Pay each player 100 dollars":
      money[turn-1]-=(players-1)*100
      for i in range (players):
        if i!=turn:
          money[i]+=100
    elif board[spot].kind == "free parking":
      print("You landed on Free Parking! You will now recive $150")
      money[turn-1]+=150
    elif board[spot].kind == "go":
      print("You are on go")
      money[turn-1]+=200
    elif board[spot].kind == "go to jail":
      if turn in jail:
        print("You are in jail")
        if dice == 12:
          jail.remove(turn)
          print("You rolled 12! You are now out of jail")
        elif money[turn-1]>50:
          pay = input("Do you want to pay $50 to get out of jail?").lower()
          if pay == "yes":
            money[turn-1]-=50
            jail.remove(turn)
    elif board[spot].kind == "income tax":
      print("You have landed on income tax. You have to pay each player $100")
      money[turn]-=100  
  turn = next(turn,players)