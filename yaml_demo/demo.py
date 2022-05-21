# import locale
# print(locale.getpreferredencoding())
import random
import tkinter as tk
import threading
import time

def dow():
    window = tk.Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()

    a =random.randrange(0 , width)

    b = random.randrange(0, height)

    window.title('520快乐')

    window.geometry("200x50" + "+" + str(a) + "+" + str(b))

    tk.Label(window,
             text = '520快乐',
             bg = 'Pink',
             font = ('楷体', 17),
             width = 15, height = 2).pack()
    window.mainloop()
threads = []
for i in range(10):
    t = threading.Thread(target=dow)
    threads.append(t)
    time.sleep(0.5)
    threads[i].start()

if __name__ == '__main__':
    dow()