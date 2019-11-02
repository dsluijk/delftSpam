import png

from string import Template
from os import system
from time import sleep

xOffset = 250
yOffset = 600
address = Template('2001:610:1908:a000:$x:$y:$b$g:$r$a')

f = open('img.png', 'rb')
r = png.Reader(file=f)
image = r.read()

x = image[0]
y = image[1]
img = list(image[2])

for i in range(y):
  for j in range(x):
    if(img[i - 1][(j - 1) * 4 + 3] == 0):
      continue

    r = hex(img[i - 1][(j - 1) * 4 + 0])[2:].zfill(2)
    g = hex(img[i - 1][(j - 1) * 4 + 1])[2:].zfill(2)
    b = hex(img[i - 1][(j - 1) * 4 + 2])[2:].zfill(2)
    a = hex(img[i - 1][(j - 1) * 4 + 3])[2:].zfill(2)
    xVal = hex(xOffset + j)[2:].zfill(4)
    yVal = hex(yOffset + i)[2:].zfill(4)
    addr = address.substitute(x=xVal, y=yVal, r=r, g=g, b=b, a=a)
    # This sends a ping every 0.2 seconds per pixel
    system("ping -i 0.2 -6 " + addr + " > /dev/null 2>&1 &")

# Run forever, as all actual code is forked
while True:
  time.sleep(60)