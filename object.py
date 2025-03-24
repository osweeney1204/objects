class Player:
 def __init__(self,gender,health, name, defaultWeapon, credits):
    self.name=name
    self.defaultWeapon=defaultWeapon
    self.credits=credits
    self.gender=gender
    self.health=health
    print("Player Object Created",self.gender,self.health)
def playerHurt(self, damage):
    self.health=self.health-damage
    print("Damage=", damage, "New Health=", self.health)
def isDead(self):
   if self.health<=0:
      return True
   else:
      return False

p1=Player("F",110)
p2=Player("M",100)

print(p2.isDead())
print(p1.isDead())
print(p1.health)
print(p1.gender)
print(p2.health)
print(p2.gender)