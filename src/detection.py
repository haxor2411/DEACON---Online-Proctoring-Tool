import time
import audio
import head_pose
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
from PIL import Image, ImageTk, ImageGrab
import tkinter as tk
import os




PLOT_LENGTH = 200

# place holders 
GLOBAL_CHEAT = 0
PERCENTAGE_CHEAT = 0
CHEAT_THRESH = 0.6
XDATA = list(range(200))
YDATA = [0]*200
x = 0
y = []





#Capturing snapshot
import cv2

def capture_and_display_snapshot(output_dir, filename):
    
    cap = cv2.VideoCapture(0)

 


    
    ret, frame = cap.read()

    os.makedirs(output_dir, exist_ok=True)

    
    file_path = os.path.join(output_dir, filename)


    cv2.imwrite(file_path, frame)

 
    cap.release()

    print(f"Snapshot saved as {file_path}")













def avg(current, previous):
    if previous > 1:
        return 0.65
    if current == 0:
        if previous < 0.01:
            return 0.01
        return previous / 1.01
    if previous == 0:
        return current
    return 1 * previous + 0.1 * current

def process():
    global GLOBAL_CHEAT, PERCENTAGE_CHEAT, CHEAT_THRESH, x #head_pose.X_AXIS_CHEAT, head_pose.Y_AXIS_CHEAT, audio.AUDIO_CHEAT
    # print(head_pose.X_AXIS_CHEAT, head_pose.Y_AXIS_CHEAT)
    # print("entered proess()...")
    if GLOBAL_CHEAT == 0:
        if head_pose.X_AXIS_CHEAT == 0:
            if head_pose.Y_AXIS_CHEAT == 0:
                if audio.AUDIO_CHEAT == 0:
                    PERCENTAGE_CHEAT = avg(0, PERCENTAGE_CHEAT)
                else:
                    PERCENTAGE_CHEAT = avg(0.2, PERCENTAGE_CHEAT)
            else:
                if audio.AUDIO_CHEAT == 0:
                    PERCENTAGE_CHEAT = avg(0.2, PERCENTAGE_CHEAT)
                else:
                    PERCENTAGE_CHEAT = avg(0.4, PERCENTAGE_CHEAT)
        else:
            if head_pose.Y_AXIS_CHEAT == 0:
                if audio.AUDIO_CHEAT == 0:
                    PERCENTAGE_CHEAT = avg(0.1, PERCENTAGE_CHEAT)
                else:
                    PERCENTAGE_CHEAT = avg(0.4, PERCENTAGE_CHEAT)
            else:
                if audio.AUDIO_CHEAT == 0:
                    PERCENTAGE_CHEAT = avg(0.15, PERCENTAGE_CHEAT)
                else:
                    PERCENTAGE_CHEAT = avg(0.25, PERCENTAGE_CHEAT)
    else:
        if head_pose.X_AXIS_CHEAT == 0:
            if head_pose.Y_AXIS_CHEAT == 0:
                if audio.AUDIO_CHEAT == 0:
                    PERCENTAGE_CHEAT = avg(0, PERCENTAGE_CHEAT)
                else:
                    PERCENTAGE_CHEAT = avg(0.55, PERCENTAGE_CHEAT)
            else:
                if audio.AUDIO_CHEAT == 0:
                    PERCENTAGE_CHEAT = avg(0.55, PERCENTAGE_CHEAT)
                else:
                    PERCENTAGE_CHEAT = avg(0.85, PERCENTAGE_CHEAT)
        else:
            if head_pose.Y_AXIS_CHEAT == 0:
                if audio.AUDIO_CHEAT == 0:
                    PERCENTAGE_CHEAT = avg(0.6, PERCENTAGE_CHEAT)
                else:
                    PERCENTAGE_CHEAT = avg(0.85, PERCENTAGE_CHEAT)
            else:
                if audio.AUDIO_CHEAT == 0:
                    PERCENTAGE_CHEAT = avg(0.5, PERCENTAGE_CHEAT)
                else:
                    PERCENTAGE_CHEAT = avg(0.85, PERCENTAGE_CHEAT)

    if PERCENTAGE_CHEAT > CHEAT_THRESH:
        GLOBAL_CHEAT = 1
        x += 1
        print("CHEATING")
    else:
        GLOBAL_CHEAT = 0
    print("Cheat percent: ", PERCENTAGE_CHEAT, GLOBAL_CHEAT)

def run_detection():
    global XDATA,YDATA,x
    plt.show()
    axes = plt.gca()
    axes.set_xlim(0, 200)
    axes.set_ylim(0,1)
    line, = axes.plot(XDATA, YDATA, 'r-')
    plt.title("SUSpicious Behaviour Detection")
    plt.xlabel("Time")
    plt.ylabel("Cheat Probablity")
    i = 0
    while True:
        YDATA.pop(0)
        YDATA.append(PERCENTAGE_CHEAT)
        line.set_xdata(XDATA)
        line.set_ydata(YDATA)
        plt.draw()
        plt.pause(1e-17)

            
        if x>5:
            messagebox.showinfo("Warning", "Cheating")
            y.append(0)
            i+=1
            output_directory = "snapshots"
            snapshot_filename = "snapshot{}.jpg".format(i)
            capture_and_display_snapshot(output_directory, snapshot_filename)
     
            x = 0

        if len(y) > 3:
            messagebox.showinfo("OOPS !", "Exam Terminated")   
            break     
        time.sleep(1/2)
        process()