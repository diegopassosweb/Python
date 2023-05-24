import random

def roll_dice():
    
     dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),
        
     }
     roll = input("Quer fazer randomizar dados? (Sim/Não): ")
     while roll.lower() == "Sim".lower():
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            
            print(f"Randomizamos {dice1} e {dice2}")
            print("\n".join(dice_drawing[dice1]))
            print("\n".join(dice_drawing[dice2]))
            
            roll = input("Randomizar de novo? (Sim/Não): ")

roll_dice()