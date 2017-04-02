#!/usr/bin/env python3

#requirement dnf install youtube-dl 
#install ffmpeg via the rpmfusion repo 
#https://rpmfusion.org/Configuration/
#### run ######
#### add a url to a file , python3 <script>, select 1 and enter the file path

import subprocess


def download():
    get =input("Enter url file list location path: ")

    f = open(get)
    line = f.readlines()


    for i in line:
        run = "youtube-dl -f 140 " + i
        print ("Processing. Call me leech ")
        subprocess.call(run, shell=True)

def search():
    get = input("What's your pleasure? Enter a search term: ")


    run = "youtube-dl -k \"ytsearch:" + get + "\"" 
    print ("Processing. Call me leech ")
    subprocess.call(run, shell=True)
#    print(mas)

print("Enter 1 if you have a URL file list. (one url per line) : ")
print("Enter 2 if you prefer to do a search and download all video and audio content: ")
print("Developed by OpenKB.org. Any questions please contact the developer Mas")


selection = input("What do you desire ?: ") 


if selection =="1" :
    download()
elif selection == "2":
    search()
else:
    print("Your not good at following instructions. Please rerun the application and make a valid seletion")

