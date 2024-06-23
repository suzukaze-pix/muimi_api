from fastapi import FastAPI
import random
import cv2
import torch


muimi_list = ["ModuleNotFoundError: Universe Not Found","Fatal Python error: Unicorn Buffer Overflow","TypeError: Demonic Possession Detected","AttributeError: Time Traveler Conflict",'TypeError: Book Burn Detected',"TypeError: Comic Sans Detected","NameError: Future Not Found","AttributeError: No Funk Music detected","AttributionError: Insane Request"]


app = FastAPI()
@app.get("/")
def Send_muimi():
    blank()
    return NoImiSellect()

def NoImiSellect():
    return random.choice(muimi_list)

def blank():
    return None

















#グランドマザー・テレサ
