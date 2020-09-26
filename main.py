from tkinter import *
from PIL import ImageTk, Image

laberint = Tk()
laberint["bg"] = "black"
laberint.title('лаберинт')

c = Canvas(laberint, height=360, width=480)
c.pack()
x = 0
y = 0
x2 = 0
y2 = 0
c.create_rectangle(x, y, x+2000, y+2000, fill='black', outline='pink')
level1 = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                 WWWWWW    KW",
    "WWWWWWWWWWW  WWW  WWWWWW  W  W",
    "WWWWWWW      WWW  WWWWWW  W  W",
    "WWWWWWW  WWWWWWW          W  W",
    "W K      WWW     KWWWWWW  W  W",
    "W  WWWW  WWW  WWWWWWWW    W  W",
    "W  WWWW  WWW       WWW  WWW  W",
    "W     W    WWWWWW  WWW  W    W",
    "WWWW  WWW  WWWWWW    W  W  WWW",
    "WW            WWWWW  WK W    W",
    "WW  WWWWWWW   WWW       WWW  W",
    "WW    W                 WWW  W",
    "WWWW  W       WWWWWWWWWWW    W",
    "WW    WWWWWWWWWWWWWWWWWWW    W",
    "WW    W                     KW",
    "WW  KWW  WWWWWWWWWWWWWWWW  WWW",
    "WW  WWW       KWWW         WWW",
    "WWWWWWWWWWWWWWWWWWWWWWWEWWWWWW",
]
exits = []
walls = []
keys = []
coord_keys = []

pilImage = Image.open("wall.png")
image = ImageTk.PhotoImage(pilImage)

pilImage2 = Image.open("croco2.png")
image2 = ImageTk.PhotoImage(pilImage2)

pilImage4 = Image.open("croco.png")
image4 = ImageTk.PhotoImage(pilImage4)

pilImage3 = Image.open("tube.png")

pilImage5 = Image.open("key.png")
image5 = ImageTk.PhotoImage(pilImage5)

image3 = ImageTk.PhotoImage(pilImage3)
player = c.create_image(16, 16, anchor=NW, image=image2)
for w_string in level1:
    for w_char in w_string:
        if 'W' in w_char:
            c.create_image(x+8, y+8, image=image)
            # c.create_rectangle(x, y, x + 16, y + 16, fill='green', outline='black')
            # c.create_rectangle(x, y, x+16, y+16, fill='black', outline='pink')
            walls.append((x, y, x + 16, y + 16))
        elif 'E' in w_char:
            c.create_image(x + 8, y + 8, image=image3)
            # c.create_rectangle(x, y, x + 16, y + 16, fill='yellow')
            exits.append((x, y, x + 16, y + 16))
        elif 'K' in w_char:
            k = c.create_image(x + 8, y + 8, image=image5)
            # c.create_rectangle(x, y, x + 16, y + 16, fill='yellow')
            coord_keys.append((x, y, x + 16, y + 16))
            keys.append(k)
        x = x + 16
    x = 0
    y = y + 16
print(walls, exits)


# player = c.create_rectangle(17, 17, 31, 31, fill='red')

text_keys = c.create_text(400, 330, text=f"left to collect {len(keys)} keys", fill='grey')


def player_move(event):
    dx = dy = 0
    key = event.keysym
    if key == "Up":
        dy = -4
    elif key == "Down":
        dy = 4
    elif key == "Left":
        c.itemconfig(player, image=image4)
        dx = -4
    elif key == "Right":
        c.itemconfig(player, image=image2)
        dx = 4
    c.move(player, dx, dy)
    for wall in walls:
        if player in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
            c.move(player, - dx, - dy)
            return
    c.move(player, dx, dy)


    for key in coord_keys:
        if player in c.find_overlapping(key[0], key[1], key[2], key[3]):
            print("key")

            ind = coord_keys.index(key)
            del coord_keys[ind]
            c.delete(keys[ind])
            del keys[ind]
            c.itemconfig(text_keys, text=f"left to collect {len(keys)} keys")
            return
    laberint.update()


c.bind_all('<Key>', player_move)
mainloop()
