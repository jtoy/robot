from image import classify
from drive_safe import gof, stop, left, right, backward, turnOffMotors


stopped = True
turning = False
THRESH = 25
turnCount = 0
maxTurnCount = 3


def main():
    while(True):
        print("driving!")

        mind = 1000
        d = []

        for i in range(3):
            d.append(distance(i))
            if d[i] < mind:
                mind = d[i]
            print(d[i])

        print(d)
        print("Min d " + str(mind))

        if (mind < 6 and stopped and turning):
            do('echo "backing up." | flite ')
            backward(255, 1)
        elif (turnCount > maxTurnCount):
            do('echo "backing up." | flite ')
            backward(255, 1)
            turnCount = 0
        elif (mind >= THRESH and stopped):
            stopped = False
            turning = False
            gof()
            turnCount = 0
        elif (mind < THRESH and not stopped):
            stopped = True

        elif (mind < THRESH and stopped):
            if (not turning):
                stop()
                turning = True
            else:
                turnCount += 1

            if d[2] > d[0]:
                do('echo "turning left." | flite ')
                left(255, 0.5)
            else:
                do('echo "turning right." | flite ')
                right(255, 0.5)

            time.sleep(0.3)
            stopped = True
            classify_image()


if __name__ == '__main__':
    main()
