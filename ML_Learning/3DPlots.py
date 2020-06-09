import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Total Line profile = 8000 m
# Speed increases linearly for 1/3rd of total time
g = 9.8
tspdkph = 75
tspdmps = int(tspdkph * 5 / 18)
# print(tspdmps)
carlen = 23
trainlen = carlen * 8
panto1 = 29  # Position of pantograph 1 from the end of train
panto2 = 74  # Position of pantograph 2 from the end of train
panto3 = 115  # Position of pantograph 3 from the end of train
time = 600  # total simulation time in seconds
samples = time * 100
nprofsam = 6
n_sec_start = 2000  # starting point of neutral section in meters
n_sec_len = 260  # length of neutral section in meters
n_sec = [None] * samples
n_sec_det = n_sec_start - 90  # Point at which neutral section is detected
n_sec_opn = n_sec_start - 10  # Point at which neutral section is opened
n_sec_cls = n_sec_start + n_sec_len + 10  # Point at which neutral section is opened

dist = np.zeros(samples)
distp1 = np.zeros(samples)
distp2 = np.zeros(samples)
distp3 = np.zeros(samples)
# distp1[0] = panto1*-1
# distp2[0] = panto2*-1
# distp3[0] = panto3*-1
j = 0


def train_mov(i):
    # if i < samples:
    #     i = i + 1
    redDot.set_data(dist[i], t[i])
    greenDot.set_data(distp1[i], t[i])
    # blackDot.set_data(distp2[i], t[i])
    # cyanDot.set_data(distp3[i], t[i])

    return redDot, greenDot,
    # global n
    # if n <= samples-1:
    #     n = n+1
    # else:
    #     n = 0
    # train = [None] * samples
    # train[n + trainlen] = dist[n + trainlen]
    # train[n + trainlen - panto1] = dist[n + trainlen - panto1]
    # train[n + trainlen - panto2] = dist[n + trainlen - panto2]
    # train[n + trainlen - panto3] = dist[n + trainlen - panto3]


def distcalc(vloc):
    j = 0
    for i in range(samples - 1):
        dist[i + 1] = dist[i] + vloc[i] * (t[i + 1] - t[i])
        if dist[i] > panto1:
            distp1[i + 1] = distp1[i] + vloc[i] * (t[j + 1] - t[j]+i-j)
            j = j + 1
        # distp2[i + 1] = distp2[i] + vloc[i] * (t[i + 1] - t[i])
        # distp3[i + 1] = distp3[i] + vloc[i] * (t[i + 1] - t[i])
        if (dist[i] >= n_sec_start) & (dist[i] <= n_sec_start + n_sec_len):
            n_sec[i] = dist[i]


t = np.linspace(0, time, samples)  # 600 corresponds to 600 seconds or 10 mins of simulation

# v = np.ones(samples) * tspdmps
vp1 = np.concatenate((np.linspace(0, tspdmps, int(samples / nprofsam)), np.ones(int(samples / nprofsam)) * tspdmps,
                      np.linspace(tspdmps, 0, int(samples / nprofsam))), axis=0)
vp1 = np.concatenate((vp1, vp1), axis=0)
# tp1 = t + panto1/vp1
distcalc(vp1)
# print(distp1[0:1000])
# m = t - (panto1 / vp1)
# plt.subplot(2, 1, 1)
plt.figure(1)
plt.plot(t, vp1)
plt.title('Speed Profile')
plt.xlabel('Time (s)')
plt.ylabel('Speed (m/s)')

# plt.subplot(2, 1, 2)

fig2 = plt.figure(2)
plt.plot(dist, t, 'r')
plt.plot(n_sec, t)

plt.title('Distance Travelled')
plt.ylabel('Time (sec)')
plt.xlabel('Distance Travelled (m)')
redDot, = plt.plot(dist[0], 0, 'ro', markersize=3)
greenDot, = plt.plot(distp1[0], 0, 'go', markersize=3)
blackDot, = plt.plot(distp2[0], 0, 'bo', markersize=3)
cyanDot, = plt.plot(distp3[0], 0, 'co', markersize=3)
anim = animation.FuncAnimation(fig2, train_mov, frames=samples, interval=1, blit=True)
plt.show()
