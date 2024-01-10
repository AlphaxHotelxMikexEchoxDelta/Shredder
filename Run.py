import subprocess, platform, os

OS =  platform.system()

if OS == "Linux":
    subprocess.call("clear ; python3 {}/Menu.py | lolcat".format(OS), shell=True)
elif OS == "Windows":
   os.system('cmd /k "cls & python3 {}/Menu.py"'.format(OS))




#salut!