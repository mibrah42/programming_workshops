import time
import random
from playsound import playsound

names = [
    "Arda Celik",
    "Hossein Amirinia",
    "Matthew Oinonen",
    "Niraj Reginald",
    "Hanan Hiba",
    "Yusuf Shaik",
    "Danial Asghar",
    "Ghadeer Abdelkader",
    "Adam Wong Chew Onn",
    "Jeremy Francis",
    "Meghana Govind",
    "Sheila Kuria",
    "Hamza Farhat Ali",
    "Charisse Chan"
]

def pickAName(names):
    for i in range(10,-1,-1):
        print(i)
        time.sleep(0.5)
    randomNumber = random.randint(0,len(names) - 1)
    playsound('drumroll.mp3')
    playsound('tada.mp3')
    print(names[randomNumber])

pickAName(names)


