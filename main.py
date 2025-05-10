import math
import os
import time
import shutil

BRIGHTNESS = ".,-~:;=!*#$@"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def render_sphere(r=10, w=30, h=30, t_steps=120, p_steps=60, dist=100):
    cols, lines = shutil.get_terminal_size((w, h))
    left = max((cols - w) // 2, 0)
    top = max((lines - h) // 2, 0)
    K1 = w * dist / (2 * r)
    A = 0.0
    while True:
        buf = [' '] * (w * h)
        zb = [0] * (w * h)
        for i in range(p_steps + 1):
            phi = math.pi * i / p_steps
            for j in range(t_steps + 1):
                theta = 2 * math.pi * j / t_steps
                x = r * math.sin(phi) * math.cos(theta)
                y = r * math.cos(phi)
                z = r * math.sin(phi) * math.sin(theta)
                x_r = x * math.cos(A) + z * math.sin(A)
                z_r = -x * math.sin(A) + z * math.cos(A)
                ooz = 1 / (z_r + dist)
                xp = int(w/2 + K1 * ooz * x_r)
                yp = int(h/2 - K1 * ooz * y)
                idx = xp + yp * w
                if 0 <= idx < w * h:
                    if ooz > zb[idx]:
                        zb[idx] = ooz
                        L = (math.sin(phi) * math.cos(theta) * math.cos(A)
                             + math.cos(phi) * math.sin(A))
                        li = int((L + 1) / 2 * (len(BRIGHTNESS) - 1))
                        buf[idx] = BRIGHTNESS[li]
        clear()
        for _ in range(top):
            print()
        for i in range(h):
            print(' ' * left + ''.join(buf[i*w:(i+1)*w]))
        A += 0.05
        time.sleep(0.05)

if __name__ == '__main__':
    try:
        render_sphere()
    except KeyboardInterrupt:
        pass