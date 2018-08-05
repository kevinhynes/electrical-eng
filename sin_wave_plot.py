import matplotlib.pyplot as plt
import math

w = 200*math.pi
t = [0.0001*i for i in range(1, 210)]
ps_cos = math.pi/5
ps_sin = math.pi*(0.3)

cos_wave = [math.cos(w*x - ps_cos) for x in t]
sin_wave = [math.sin(w*x + ps_sin) for x in t]
cos_wave_2 = [math.cos(w*x - 0.6) for x in t]
sin_wave_2 = [math.sin(w*x + 0.9424) for x in t]


plt.subplot(2, 1, 1) #(rows, columns, selected)
# x and y axis
plt.plot([0.001, 0.001], [-1, 1], color='black', linestyle='--')
plt.plot(t, [0]*len(t), color='black', linestyle='--')
plt.axis([0, .025, -1, 1])
plt.plot(t, cos_wave)
plt.plot(t, sin_wave, linestyle=':')

plt.subplot(2, 1, 2)
# x and y axis
plt.plot([0.001, 0.001], [-1, 1], color='black', linestyle='--')
plt.plot(t, [0]*len(t), color='black', linestyle='--')
plt.axis([0, .025, -1, 1])
plt.plot(t, cos_wave_2)
plt.plot(t, sin_wave_2)


plt.show()
