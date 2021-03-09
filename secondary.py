import tkinter as tk
import sys
import os

a = ""
b = ""
c = -1

def exchange():
    usg = open("Usage.gpf", "r")
    cont = usg.readlines()
    usg.close()
    cont[c] = a+"\n"
    usg = open("Usage.gpf", "w")
    for i in range(len(cont)):
        usg.write(cont[i])
    usg.close()


    usg = open("password.gpf", "r")
    cont = usg.readlines()
    usg.close()
    cont[c] = b+"\n"
    usg = open("password.gpf", "w")
    for i in range(len(cont)):
        usg.write(cont[i])
    usg.close()

    ext = open("ext.bat", "w")
    ext.write("start Window.pyw")
    ext.close()
    os.system("start ext.bat")
    sys.exit()
def check_border(x, y, a, b, c, d):
    # print(str(a), "\t", str(b), "\t", str(c), "\t", str(d))
    # print(str(x)+"\t"+str(y))
    if x >= a and x <= c and y >= b and y <= d:
        print("1")
        return True
    else:
        print("0")
        return False


def callback(event):
    print(event.x)
    if check_border(event.x, event.y, 10, 40, 190, 90):
        exchange()
    #if check_border(event.x, event.y, 120, 40, 190, 90):
     #   sys.exit()
def set(usage, password, slot):
    head = tk.Tk(className="Menu")
    head.resizable(False, False)
    hc = tk.Canvas(head, width = "200", height = "100")
    hc.bind("<Button-1>", callback)
    hc.pack()
    hc.create_rectangle(0, 0, 1000, 1000, fill = "yellow")
    hc.create_text(50, 10, text = "Are you sure to exchange?", anchor = "nw")
    hc.create_rectangle(10, 40, 190, 90, fill = "green")
    #hc.create_rectangle(120, 40, 190, 90, fill = "red")
    global a
    a = usage
    global b
    b = password
    global c
    c = slot

    head.mainloop()






