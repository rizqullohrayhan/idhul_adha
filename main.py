import turtle
import math

sc = turtle.Screen()
sc.bgcolor("midnightblue")
sc.title("Selamat Idul Adha 1446 H")
sc.setup(700, 500)

# Turtle script example
t = turtle.Turtle()
# t.hideturtle()

def pindah(x, y):
    t.penup(); t.goto(x, y); t.pendown()

def kotak(x, y, w, h, warna):
    t.fillcolor(warna)
    pindah(x, y)
    t.begin_fill()
    for _ in range(2):
        t.forward(w); t.left(90)
        t.forward(h); t.left(90)
    t.end_fill()
    t.penup()

def kubah(cx, cy, r, warna):
    t.fillcolor(warna)
    pindah(cx - r, cy)
    t.begin_fill()
    t.setheading(0)
    t.left(90)
    t.circle(r, 180)
    t.end_fill()
    t.penup()

# Badan masjid
kotak(-100, -100, 200, 120, "#c8a96e")

# Kubah utama
kubah(110, 20, 55, "#c8a96e")

# Menara kiri & kanan
t.left(90)
kotak(-130, -100, 30, 160, "#b8935a")
kotak(100, -100, 30, 160, "#b8935a")
kubah(-85, 60, 15, "#b8935a")
kubah(145, 60, 15, "#b8935a")

# Pintu
kotak(-30, -60, 40, 60, "#7a5c2e")

# Bulan sabit
pindah(0, 75)
t.fillcolor("gold")
t.begin_fill()
t.setheading(180)
t.circle(-30, 360)
t.end_fill()
pindah(10, 85)
t.fillcolor("midnightblue")
t.begin_fill()
t.setheading(180)
t.circle(-25, 360)
t.end_fill()

# Bintang
def bintang(x, y, ukuran, warna):
    pindah(x, y)
    t.fillcolor(warna)
    t.begin_fill()
    t.setheading(90)
    for _ in range(5):
        t.forward(ukuran)
        t.right(144)
    t.end_fill()
    
bintang(0, 100, 18, "gold")

# Teks
t.pencolor("gold")
t.penup()
t.goto(0, 140)
t.write("Selamat Hari Raya", align="center",
        font=("Arial", 18, "bold"))
t.goto(0, 110)
t.write("Idul Adha 1446 H", align="center",
        font=("Arial", 16, "bold"))
t.goto(0, -220)
t.write("Taqabbalallahu Minna wa Minkum",
        align="center", font=("Arial", 11, "normal"))

turtle.done()
