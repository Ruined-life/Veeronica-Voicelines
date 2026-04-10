# Forsaken Voicelines

## Overview
This is a script that will bring the survivors to life. Adding voicelines for specific actions.

NOTE:
The voicelines I used are from people I found on youtube so all credits go to them (you can look at each person in the CREDITS file)

RECOMMEND VOLUME TO PLAY AT

<img src="volume.png" width="300">

---

## Features
```md
Voice lines upon ability activation
Idle voice lines

TO BE ADDED:
Damage sounds
Death sounds
```
---

## Project Structure
```md
src -> main logic
gui -> displays gui and grabs character
audio -> houses all the voicelines for each character
CREDITS -> the owners of the voicelines
requirements -> packages needed to run the program
```
---

## Install Instructions
## Windows
```md
Download Wininstaller.ps1 
https://github.com/Ruined-life/Forsaken-Voicelines/releases
Open a command prompt window
Take note of where the file was installed (Move it into its own empty folder)
Copy the file path of where you put the file
Paste this: 
cd <file_path>
then do ./Wininstaller.ps1

It will likely throw an error about a policy. To fix it paste this:
powershell -ExecutionPolicy Bypass -File .\installer.ps1
```
## Linux
```md
Download Linuxinstaller.sh 
https://github.com/Ruined-life/Forsaken-Voicelines/releases
Run Linuxinstaller.sh
```
