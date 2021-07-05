#-*-coding:utf8;-*-
#qpy:console

import youtube_dl
import os
import time
os.system('clear')

print("\033[0;31m░░░░░░░░░░░░░░░░░░\033[0;32m░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░")
print("\033[0;31m██░░██░░░░░░░░░░░\033[0;32m▄█░░░░░░████░░████████▄")
print("\033[0;31m██▄▄██░░░░░░░░░░\033[0;32m░████░░██████░░█████████")
print("\033[0;31m▀████▀░████░█░░█░\033[0;32m████░░█░██░█░▄▄░█░░▄▄██")
print("\033[0;31m░░██░░░█░░█░█▄▄█░\033[0;32m████░░█░░░░█░▀▀░█░░▄▄██")
print("\033[0;31m░░██░░░████░████░\033[0;32m▀███▄▄█▄▄▄▄█▄▄▄▄█▄▄▄▄█▀")
print("\033[0;31m░░░░░░░░░░░░░░░░░░░\033[0;32m▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀░░")
print("                                                            ")
print("                                                            ")
print("\033[0;33m         PROGRAMMING BY : \033[0;31m JIMMY X      ")
print(" \033[0;33m        TWITTR :\033[0;31mhttps://twitter.com/jimmy94911434 ")
print("                                                            ")
print("                                                           ")
print("You can download YouTube videos on Linux in high quality ^^")
print('\033[0;33m_'*60)


ydl={ }
path ="/storage/emulated/0"
os.chdir(path)

url=input("\033[0;31m[>]\033[0;36m ENTER YOUTUBE URL : ")
with youtube_dl.YoutubeDL(ydl)as ydl:
         ydl.download([url])

print("DOWNLOADED...")
