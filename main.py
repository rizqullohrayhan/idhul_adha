import turtle
import random
import pygame

pygame.mixer.init()
pygame.mixer.music.load("music/bg_music.mp3")
pygame.mixer.music.play()

sc = turtle.Screen()
sc.bgcolor("midnightblue")
sc.title("Selamat Idul Adha 1447 H")
sc.setup(700, 500)

t = turtle.Turtle()

t.penup()
t.goto(0, -230)
t.pencolor("white")
t.write("By github.com/rizqullohrayhan",
        align="center", font=("Arial", 11, "normal"))
t.pencolor("black")

def pindah(turtle, x, y):
    turtle.penup(); turtle.goto(x, y); turtle.pendown()

def kotak(x, y, w, h, warna):
    t.fillcolor(warna)
    pindah(t, x, y)
    t.begin_fill()
    for _ in range(2):
        t.forward(w); t.left(90)
        t.forward(h); t.left(90)
    t.end_fill()
    t.penup()

def kubah(cx, cy, r, warna):
    t.fillcolor(warna)
    pindah(t, cx - r, cy)
    t.begin_fill()
    t.setheading(0)
    t.left(90)
    t.circle(r, 180)
    t.end_fill()
    t.penup()

# Tanah
kotak(-350, -200, 700, 100, "#2e8b57")

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

# Jendela
kotak(-90, -20, 20, 10, "#7a5c2e")
kotak(-70, -20, 20, 10, "#7a5c2e")
kotak(60, -20, 20, 10, "#7a5c2e")
kotak(80, -20, 20, 10, "#7a5c2e")

# Bulan sabit
pindah(t, 0, 105)
t.fillcolor("gold")
t.begin_fill()
t.setheading(180)
t.circle(-30, 360)
t.end_fill()
pindah(t, 10, 115)
t.color("midnightblue", "midnightblue")
t.begin_fill()
t.setheading(180)
t.circle(-25, 360)
t.end_fill()

# Bintang
def bintang(x, y, warna):
    pindah(t, x, y)
    t.pencolor("black")
    t.fillcolor(warna)
    t.begin_fill()
    t.setheading(90)
    for _ in range(5):
        t.forward(8)
        t.left(72)
        t.forward(8)
        t.right(144)
    t.end_fill()

# Bintang di atas kubah
bintang(10, 130, "gold")

for l in range(10):
    if l % 2 == 0:
        x = random.choice([i for i in range(-300, 300) if i < -130])
    else:
        x = random.choice([i for i in range(-300, 300) if i > 130])

    y = random.randint(20, 200)
    bintang(x, y, "gold")

# Teks
t.pencolor("gold")
t.penup()
t.goto(0, 200)
t.write("Selamat Hari Raya", align="center",
        font=("Arial", 18, "bold"))
t.goto(0, 170)
t.write("Idul Adha 1447 H", align="center",
        font=("Arial", 16, "bold"))
t.goto(0, -180)
t.pencolor("white")
t.write("Taqabbalallahu Minna wa Minkum",
        align="center", font=("Arial", 11, "normal"))


# Animasi kembang api
f = turtle.Turtle()
f.hideturtle()
f.speed(60)

def firework(size):
    for num in range(20):
         f.forward(size)
         f.right(180-(360/20))

C_BRIGHT_MIN = 0x10
C_BRIGHT_MAX = 0xef
F_SIZE_MIN = 15
F_SIZE_MAX = 40
FIREWORK_PER_CLEAR = 5

while True:
    x = random.choice([i for i in range(-300, 300) if i < -150 or i > 130])
    y = random.randint(20, 200)
    pindah(f, x, y)
    for i in range(FIREWORK_PER_CLEAR):
        # this generates a random color sequence using RGB
        color_r = hex(random.randint(C_BRIGHT_MIN, C_BRIGHT_MAX))[2:]
        color_g = hex(random.randint(C_BRIGHT_MIN, C_BRIGHT_MAX))[2:]
        color_b = hex(random.randint(C_BRIGHT_MIN, C_BRIGHT_MAX))[2:]
        f.color('#'+color_r+color_g+color_b)
        firework(random.randint(F_SIZE_MIN, F_SIZE_MAX))
        x = random.choice([i for i in range(-300, 300) if i < -150 or i > 130])
        y = random.randint(20, 200)
        pindah(f, x, y)
    f.clear()
