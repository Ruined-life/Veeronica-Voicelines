from playsound import playsound
import gi

import random
import time

from pynput import keyboard

import pyautogui
import pytesseract


# -----------------------------
# Sound file lists
# -----------------------------

Graffiti = [
    "Vocal Only/Graffiti/graffiti1[vocals].wav",
    "Vocal Only/Graffiti/graffiti2[vocals].wav",
    "Vocal Only/Graffiti/graffiti3[vocals].wav"
]

Damage = [
    "Vocal Only/Damage/damage2[vocals].wav",
    "Vocal Only/Damage/damage3[vocals].wav",
    "Vocal Only/Damage/damage4[vocals].wav",
    "Vocal Only/Damage/damage5[vocals].wav"
]

DamageSound = [
    "Vocal Only/Damage/damage6.mp3",
    "Vocal Only/Damage/damage7.mp3",
    "Vocal Only/Damage/damage8.mp3",
    "Vocal Only/Damage/damage9.mp3"
]

Idle = [
    "Vocal Only/Idle/idle1[vocals].mp3",
    "Vocal Only/Idle/idle2[vocals].mp3",
    "Vocal Only/Idle/idle3[vocals].mp3"
]

Skateboard = [
    "Vocal Only/Skateboard/Skate1[vocals].mp3",
    "Vocal Only/Skateboard/Skate2[vocals].mp3",
    "Vocal Only/Skateboard/Skate3[vocals].mp3",
    "Vocal Only/Skateboard/Skate4[vocals].mp3",
    "Vocal Only/Skateboard/Skate5[vocals].mp3",
    "Vocal Only/Skateboard/Skate6[vocals].mp3",
    "Vocal Only/Skateboard/Skate7[vocals].mp3"
]

Battery = [
    "Vocal Only/Battery/Battery2[vocals].mp3",
    "Vocal Only/Battery/Battery3[vocals].mp3",
    "Vocal Only/Battery/Battery4[vocals].mp3",
    "Vocal Only/Battery/Battery5[vocals].mp3"
]


# -----------------------------
# Variables
# -----------------------------

previous_health = None
last_keypress_time = time.time()  # replaces key_timer entirely
idle_delay = 20                  # 60 seconds of no input → idle sound


# -----------------------------
# Sound selection
# -----------------------------

def sound_select(mode):
    if mode == "damage":
        playsound(random.choice(Damage))

    elif mode == "grafiti":
        playsound(random.choice(Graffiti))

    elif mode == "idle":
        playsound(random.choice(Idle))

    elif mode == "skate":
        playsound(random.choice(Skateboard))

    elif mode == "battery":
        playsound(random.choice(Battery))

    elif mode == "damagesound":
        playsound(random.choice(DamageSound))    


# -----------------------------
# OCR Health Scanner
# -----------------------------

def screenshot_health():
    region = (455, 912, 40, 40)
    screenshot = pyautogui.screenshot(region=region)

    text = pytesseract.image_to_string(
        screenshot,
        config="--psm 7 -c tessedit_char_whitelist=0123456789"
    ).strip()

    try:
        return int(text)
    except ValueError:
        return None


# -----------------------------
# Keypress listener
# -----------------------------

def on_press(key):
    global last_keypress_time

    # Update timestamp for ANY key you react to
    last_keypress_time = time.time()

    try:
        if key == keyboard.Key.space:
            print("space pressed")
            sound_select("skate")

        elif key.char == "q":
            print("q pressed")
            sound_select("grafiti")

        elif key.char == "e":
            print("e pressed")
            sound_select("skate")

        elif key.char == "t":
            print("t pressed")
            sound_select("battery")

    except AttributeError:
        pass


listener = keyboard.Listener(on_press=on_press)
listener.start()


# -----------------------------
# Main Loop
# -----------------------------

while True:
    # ---------------------
    # Idle sound system
    # ---------------------
    if time.time() - last_keypress_time >= idle_delay:
        print("Idle timeout reached → playing idle sound")
        sound_select("idle")

        # Reset timer so it doesn't loop spam idle
        last_keypress_time = time.time()

    # ---------------------
    # Health scanning
    # ---------------------
    current_health = screenshot_health()

    if current_health is not None:
        print("Current health:", current_health)

        # First-time setup for previous health
        if previous_health is None:
            previous_health = current_health

        else:
            # Damage detection with threshold
            if current_health < previous_health:
                difference = previous_health - current_health

                if difference >= 5:  # threshold can be tuned
                    print(f"Health decreased by {difference}!")
                    sound_select("damage")
                else:  
                    print(f"Health decreased by {difference}!")  
                    sound_select("damagesound")

            previous_health = current_health

    else:
        print("OCR failed this frame.")

    time.sleep(1.0)  # smoother + less CPU

