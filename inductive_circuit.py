import matplotlib.pyplot as plt
import math
from fractions import Fraction

f = 60
w = 2*math.pi*f
T = 1/f
t = [(2*T)*(i/100) for i in range(0, 101)]
ps = 2*math.pi*(90/360)

voltage = [math.sin(w*x) for x in t]
current = [math.sin(w*x - ps) for x in t]
xtick_locations = [T*i/4 for i in range(0, 9)]
xtick_labels = [str(Fraction(i/4)) + 'T' for i in range(0, 9)]

plt.close('all')

plt.axis([0, 2*T, -1, 1]) # frame the graph
plt.plot(t, [0]*len(t), color='black') # x-axis
plt.plot(t, voltage, color='blue', label="Inductor Voltage")
plt.plot(t, current, color='red', linestyle=':', label="Inductor Current")

ax_x = plt.subplot()
ax_x.set_xticks(xtick_locations)
ax_x.set_xticklabels(xtick_labels)

plt.title("Inductor Voltage vs Current")
plt.legend(loc=1) # loc = integer 0-10
plt.ylabel('V / I')
plt.xlabel('time')
plt.text(5/4*T, -0.75, f'f={f}Hz')
plt.grid(True)

plt.show()


#How to enter symbols using TeX
#xtick_labels = ['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$']

#Creating different subplots
#plt.subplot(2, 1, 1) #(rows, columns, selected plot)
