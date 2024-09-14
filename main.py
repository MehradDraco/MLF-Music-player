import playsound
import colorama
from time import sleep
from os import system as bash
bash("clear")
print(colorama.Fore.RED,"")
bash("cat lastplayed.txt")
print(colorama.Fore.LIGHTBLUE_EX,"")
folder = input("Music Folder Location: ")
music = input("Music name: ")
print("")
file = open("lastplayed.txt", "a")
file.write(music)
file.close()
file = open("lastplayed.txt", "a")
file.write("                                                  ")
file.close()
print(colorama.Fore.YELLOW,"Playing",colorama.Fore.CYAN,music,colorama.Fore.WHITE,":)")
playsound.playsound(folder+music)
print("")
input("Press any buttons to exit...")
bash("killall python")
