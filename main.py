import py5

xSpeed = 2
xposawan = 800
x2posawan = 350
x3posawan = 1100

# car
cSpeed = 3
xCar= 100
ycar = 300
yspeed = 2


# Titik-titik kontrol kurva bezier
p0 = (0, 450)  # Titik awal
p_peak = (160, 250)  # Titik puncak
p1 = (320, 450)  # Titik akhir
pd0 = (320, 450)  # Titik awal
pd_peak = (480, 650)  # Titik puncak
pd1 = (640, 450)  # Titik akhir
p02 = (640, 450)  # Titik awal
p_peak2 = (800, 250)  # Titik puncak
p12 = (960, 450)  # Titik akhir
pd02 = (960, 450)  # Titik awal
pd_peak2 = (1120, 650)  # Titik puncak
pd12 = (1280, 450)  # Titik akhir


def setup():
    py5.smooth()
    py5.size(1280, 720)
    py5.background(10,255,255)
    py5.stroke(0)
    py5.frame_rate(25)  # Atur frame rate
    
    #gambar matahari
    py5.stroke(255,255,0)
    py5.fill(255,255,0)
    py5.ellipse(640, 120, 100, 100)

    #gambar tanah
    py5.fill(0,150,0)
    py5.stroke(0,150,0)
    py5.rect(0, 500, 1280, 720, 0, 0, 0, 0)

    # Gambar kurva Bezier menggunakan fungsi bezier() dari py5s
    py5.no_fill()
    py5.stroke_weight(10)  # Ketebalan garis
    py5.stroke(200, 120, 0)  # Warna biru untuk kurva

    # Gambar kurva bezier 1
    bezierup1 = py5.bezier(p0[0], p0[1], p_peak[0], p_peak[1], p1[0], p1[1], p1[0], p1[1])
    bezierdown1 = py5.bezier(pd0[0], pd0[1], pd_peak[0], pd_peak[1], pd1[0], pd1[1], pd1[0], pd1[1])

    # Gambar kurva bezier 2
    bezierup2 = py5.bezier(p02[0], p02[1], p_peak2[0], p_peak2[1], p12[0], p12[1], p12[0], p12[1])
    bezierdown2 = py5.bezier(pd02[0], pd02[1], pd_peak2[0], pd_peak2[1], pd12[0], pd12[1], pd12[0], pd12[1])
    


def draw():
    global xSpeed, xposawan,x2posawan, x3posawan, cSpeed ,xCar, ycar, yspeed

    py5.fill(10, 255, 255)  # Warna latar belakang
    py5.no_stroke()  # Tanpa stroke
    py5.rect(0, 0, py5.width, py5.height)  # Menggambar latar belakang
    

    py5.stroke(255,255,0)
    py5.fill(255,255,0)
    py5.ellipse(640, 120, 100, 100)

    #gambar tanah
    py5.fill(0,150,0)
    py5.stroke(0,150,0)
    py5.rect(0, 500, 1280, 720, 0, 0, 0, 0)

    # Gambar kurva Bezier menggunakan fungsi bezier() dari py5s
    py5.no_fill()
    py5.stroke_weight(10)  # Ketebalan garis
    py5.stroke(200, 120, 0)  # Warna biru untuk kurva

        
    
    bezierup1 = py5.bezier(p0[0], p0[1], p_peak[0], p_peak[1], p1[0], p1[1], p1[0], p1[1])
    bezierdown1 = py5.bezier(pd0[0], pd0[1], pd_peak[0], pd_peak[1], pd1[0], pd1[1], pd1[0], pd1[1])

    bezierup2 = py5.bezier(p02[0], p02[1], p_peak2[0], p_peak2[1], p12[0], p12[1], p12[0], p12[1])
    bezierdown2 = py5.bezier(pd02[0], pd02[1], pd_peak2[0], pd_peak2[1], pd12[0], pd12[1], pd12[0], pd12[1])
    
    #cloud
    xposawan -= xSpeed
    x2posawan -= xSpeed
    x3posawan -= xSpeed

    if xposawan < -60 :
        xposawan = +1480


    if x2posawan < -120:
        x2posawan += 1680


    if x3posawan < -150:
        x3posawan += 1650


    cloud(xposawan,70)
    cloud2(x2posawan,140)
    cloud3(x3posawan,140)

    #animasi Car
    xCar += cSpeed

    if (xCar >= (py5.width + 100) or xCar <= 0):
        xCar -= (py5.width + 100)
        ycar += 40

    ycar += yspeed

    if (ycar >= (py5.height - 200) or ycar <= 300):
        # print('Bye!')
        yspeed *= -1

    # Memanggil fungsi untuk menggambar mobil
    car(xCar, ycar)


def cloud(x,y):
    for i in range(3):
        py5.fill(255)
        py5.stroke(255)
        py5.ellipse(x, y, 100, 100)
        x -= 50

def cloud2(x,y):
    for i in range(3):
        if i == 0:
            cloud(x,y)
        elif i == 1:
            cloud(x-110,y+35)
        else:
            cloud(x+50,y+50)

def cloud3(x,y):
    for i in range(3):
        if i == 0:
            cloud(x,y)
        elif i == 1:
            cloud(x-50,y+55)
        else:
            cloud(x+90,y+60)
        
def car(x,y):
    py5.fill(255,0,0)
    py5.stroke(255,0,0)
    py5.rect(x, y, 100, 50, 0, 20, 0, 0)


    # wheel
    py5.stroke_weight(8)
    py5.stroke(0)
    py5.fill(255)
    py5.ellipse(x+20, y+50, 30, 30)
    py5.ellipse(x+80, y+50, 30, 30)
    #human

    py5.no_stroke()
    py5.fill(255, 253, 208)
    py5.rect(x+25, y-25, 40, 20, 0, 0, 0, 0)
    py5.fill(0)
    py5.rect(x+25, y-45, 40, 20, 10, 10, 0, 0)


def calculate_bezier_y(p0, p_peak, p1, pd0, pd_peak, pd1, x):
    if p0[0] <= x < p1[0]:  # Mobil berada di antara kurva 1 dan 2
        t = (x - p0[0]) / (p1[0] - p0[0])  # parameter t
        # Interpolasi kuadratik untuk titik atas kurva Bezier
        y_top = ((1 - t) ** 2) * p0[1] + 2 * (1 - t) * t * p_peak[1] + (t ** 2) * p1[1]
        y_bottom = ((1 - t) ** 2) * pd0[1] + 2 * (1 - t) * t * pd_peak[1] + (t ** 2) * pd1[1]
    else:  # Mobil berada di antara kurva 3 dan 4
        t = (x - p1[0]) / (pd1[0] - p1[0])  # parameter t
        # Interpolasi kuadratik untuk titik atas kurva Bezier
        y_top = ((1 - t) ** 2) * p0[1] + 2 * (1 - t) * t * p_peak[1] + (t ** 2) * p1[1]
        y_bottom = ((1 - t) ** 2) * pd0[1] + 2 * (1 - t) * t * pd_peak[1] + (t ** 2) * pd1[1]

    # Mengembalikan posisi y berdasarkan kurva atas dan bawah
    return (y_top + y_bottom) / 2



py5.run_sketch()
