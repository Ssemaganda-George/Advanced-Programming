import matplotlib.pyplot as plt 

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage

# Creating an object of the Player class
player1 = Player("Alice", 100)
player1.take_damage(20)
print(f"{player1.name}'s health: {player1.health}")	


class Calculation1:
    def __init__(self, x, y):
        self.x1 = x
        self.x2 = y
    
    def Sum(self):
        print(self.x1, self.x2)
        return self.x1 + self.x2

class Calculation2:
    def __init__(self, x, y):
        self.x1 = x
        self.x2 = y
    
    def Subtraction(self): 
        return self.x1 - self.x2
    
    def Multiplication(self): 
        return self.x1 * self.x2
    
    def Division(self):
        return self.x1 / self.x2

class Derived(Calculation1, Calculation2):
    pass

x = int(input("x1="))
y = int(input("x2="))
derived1 = Derived(x, y)
result = derived1.Sum()
print(result) 

# Visualization
labels = ['Input 1', 'Input 2', 'Sum']
data = [x, y, result]

plt.bar(labels, data, color=['blue', 'orange', 'green'])
plt.xlabel('Parameters')
plt.ylabel('Values')
plt.title('Input and Output Visualization')
plt.show()