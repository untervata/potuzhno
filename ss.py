import random 
def nomer():
    letters = [ "А", "В", "Е", "К", "М", "Н", "О", "Р", "С", "Т", "У", "Х"]
    partone = random.choice(letters)
    numbers = ''.join([str(random.randint(0, 9)) for _ in range(3)])
    parttwo = random.choice(letters)
    partt = random.choice(letters)
    car_number = f"{partone}{numbers}{parttwo}{partt}"  
    print(car_number)
nomer()



        
