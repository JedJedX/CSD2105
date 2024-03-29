
import matplotlib.pyplot as plt
def circle(RD):
    x = 0
    y = RD
    d = 5.0/4.0-RD

    xplot = []
    yplot = []

    while y > x:
      plotpoints(x, y, xplot, yplot)
      if d < 0:
        d += 2.0 * x + 3.0
      else:
        d += 2.0 * (x-y)+5.0
        y -= 1
      x += 1

    setPixel = list(zip(xplot, yplot))
    setPixel.extend([(y, x) for x, y in setPixel])
    setPixel.extend([(-x, y) for x, y in setPixel])
    setPixel.extend([(-y, x) for x, y in setPixel])
    setPixel.extend([(x, -y) for x, y in setPixel])
    setPixel.extend([(y, x) for x, y in setPixel])
    setPixel.extend([(y, -x) for x, y in setPixel])
    setPixel.extend([(-x, -y) for x, y in setPixel])

    xplot, yplot = zip(*setPixel)

    plt.scatter(xplot, yplot, marker='o')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


def plotpoints(x, y, xplot, yplot):
    xplot.append(x)
    yplot.append(y)
def main():
    x1, y1 = 20, 20
    x2, y2 = 20, 30

    radius = 200
    circle(radius)

if __name__ == "__main__":
    main()