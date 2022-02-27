#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio

#first program:
from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 40*60
    exsecs = 30*60
    eyessecs = 45*60

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes >eyessecs:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            musiconloop('eyes.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musiconloop('physical.mp3', 'donephy')
            init_exercise = time()
            log_now("Physical Activity done at")


#Second program:
# import time
# import winsound
# def water_func():
#     # time.sleep(5)
#     winsound.PlaySound("water.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
#     ans_inp = input("Please drink water and type Drank: ").capitalize()
#
#     if ans_inp == "Drank":
#         winsound.PlaySound(None, winsound.SND_PURGE)
#         with open("Health Log.txt", "a") as f:
#                 f.write(time.asctime(time.localtime(time.time())) +" "+"Drank Water"+"\n")
#     while ans_inp != "Drank":
#         print("----Invalid input! Try again----")
#         ans_inp = input("Please drink water and type Drank: ").capitalize()
#         if ans_inp == "Drank":
#             winsound.PlaySound(None, winsound.SND_PURGE)
#             with open("Health Log.txt", "a") as f:
#                 f.write(time.asctime(time.localtime(time.time())) +" "+"Drank Water"+"\n")
#
# def eye_func():
#     # time.sleep(5)
#     winsound.PlaySound("eye.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
#     ans_inp = input("Please do Eye Exercise and type Eydone: ").capitalize()
#
#     if ans_inp == "Eydone":
#         winsound.PlaySound(None, winsound.SND_PURGE)
#         with open("Health Log.txt", "a") as f:
#                 f.write(time.asctime(time.localtime(time.time())) +" "+"Done Eye Exercise"+"\n")
#     while ans_inp != "Eydone":
#         print("----Invalid input! Try again----")
#         ans_inp = input("Please do Eye Exercise and type Eydone: ").capitalize()
#         if ans_inp == "Eydone":
#             winsound.PlaySound(None, winsound.SND_PURGE)
#             with open("Health Log.txt", "a") as f:
#                 f.write(time.asctime(time.localtime(time.time())) +" "+"Done Eye Exercise"+"\n")
#
# def phy_func():
#     # time.sleep(5)
#     winsound.PlaySound("physical.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
#     ans_inp = input("Please do Physical Activity and type Exdone: ").capitalize()
#
#     if ans_inp == "Exdone":
#         winsound.PlaySound(None, winsound.SND_PURGE)
#         with open("Health Log.txt", "a") as f:
#                 f.write(time.asctime(time.localtime(time.time())) +" "+"Done Physical Activity"+"\n")
#     while ans_inp != "Exdone":
#         print("----Invalid input! Try again----")
#         ans_inp = input("Please do Physical Activity and type Exdone: ").capitalize()
#         if ans_inp == "Exdone":
#             winsound.PlaySound(None, winsound.SND_PURGE)
#             with open("Health Log.txt", "a") as f:
#                 f.write(time.asctime(time.localtime(time.time())) +" "+"Done Physical Activity"+"\n")
#
# while True:
#     water_func()
#     while True:
#         time.sleep(5)
#         eye_func()
#         break
#     while True:
#         time.sleep(5)
#         water_func()
#         break
#     while True:
#         time.sleep(5)
#         phy_func()
#         break
#     while True:
#         time.sleep(5)
#         eye_func()
#         break
#     time.sleep(20)

# Third program:
# import time
# import pygame
#
# # Music did not played hence I have printed it as well.
# def playMusic(file):
#     print(file)
#     pygame.init()
#     pygame.mixer.init()
#     pygame.mixer.music.load(file)
#     pygame.mixer.music.play()
#
#
# def IsOfficeTime(currenttime):
#     if currenttime > '09:00:00' and currenttime < '17:00:00':
#         return True
#     else:
#         return False
#
#
# NumberofWaterRemaining = 18
#
# WaterAfterEvery = 2  # Seconds  - 20 minutes
# EyeExerciseAfterEvery = 2  # Seconds - 30 minutes
# PhysicalExerciseAfterEvery = 2  # Seconds  - 45 minutes
#
# waterMp3 = 'water.mp3'
# eyesMp3 = 'eyes.mp3'
# PhysicalMp3 = 'physical.mp3'
#
# currenttime = time.strftime('%H:%M:%S')
# WaterTakenAt = time.time()
# EyeExerciseAt = time.time()
# PhysicalExerciseAt = time.time()
#
# SleepTime = 6  # Sleep time in seconds It will check after every 60 seconds.
#
# while (IsOfficeTime(currenttime)):
#     #     Check for water
#     if NumberofWaterRemaining > 0:
#         if (time.time() - WaterTakenAt) > WaterAfterEvery:  # water after every 20 minutes
#             print("Time to drink water")
#             while True:
#                 # playMusic()
#                 if input("Enter Done if you had water: ").lower() == "done":
#                     WaterTakenAt = time.time()
#                     NumberofWaterRemaining -= 1
#                     break
#         if time.time() - EyeExerciseAt > EyeExerciseAfterEvery:
#             print("Time to do eye exercise")
#             while True:
#                 # playMusic()
#                 if input("Enter Done if you done eye exercise : ").lower() == "done":
#                     EyeExerciseAt = time.time()
#                     break
#         if time.time() - PhysicalExerciseAt > PhysicalExerciseAfterEvery:
#             print("Time to do Physical exercise")
#             while True:
#                 # playMusic()
#                 if input("Enter Done if you done Physical exercise : ").lower() == "done":
#                     PhysicalExerciseAt = time.time()
#                     break
#
#     time.sleep(SleepTime)
#     currenttime = time.strftime('%H:%M:%S')


