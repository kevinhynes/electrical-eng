import matplotlib.pyplot as plt
import math
from fractions import Fraction

plt.close('all')
plt.figure(1, figsize=(7, 8)) # Create new 7"x8" window
### AC STEADY-STATE CIRCUIT ###
f = 60
w = 2*math.pi*f
T = 1/f
t = [(2*T)*(i/100) for i in range(0, 101)] # Graph will not depent on frequency
ps = 2*math.pi*(90/360)

voltage = [math.sin(w*x) for x in t]
current = [math.sin(w*x - ps) for x in t]
xtick_locations = [T*i/4 for i in range(0, 9)]
xtick_labels = [str(Fraction(i/4)) + 'T' for i in range(0, 9)]

acplt = plt.subplot(2, 1, 1) 
acplt.axis([0, 2*T, -1, 1]) # frame the graph
acplt.plot(t, [0]*len(t), color='black') # x-axis
acplt.plot(t, voltage, color='blue', label="Inductor Voltage")
acplt.plot(t, current, color='red', linestyle=':', label="Inductor Current")
acplt.set_xticks(xtick_locations)
acplt.set_xticklabels(xtick_labels)
acplt.set_title("Steady State AC - Inductor Voltage vs Current")
acplt.legend(loc=1) # loc = integer 0-10
acplt.set_ylabel('V / I')
acplt.set_xlabel('time')
acplt.text(5/4*T, -0.75, f'f={f}Hz')
acplt.grid(True)

### DC TRANSIENT CIRCUIT ###
Vs = 10
L = 10
R = 1
TC = L/R
res = 0.001 # resolution == milliseconds
total_seconds = 100
sweep = total_seconds/res
t = range(0, int(sweep))

'''
At time t = 0, voltage source is switched on in an LR circuit.
Voltage across inductor == Vs at this instant (assume R is internal to inductor).
Use Universal Time Constant Formula to plot the inductor's voltage and current 
over time.

Initial Voltage is Vs but decays over time (negative change)
Initial Current is 0 and increases to Vs/R
'''

voltage = [Vs+(-1)*Vs*(1 - (1/math.exp(x*res/TC))) for x in t]
current = [(Vs/R)*(1 - (1/math.exp(x*res/TC))) for x in t]    
dcplt = plt.subplot(2, 1, 2)
dcplt.axis = ([0, sweep], [0, 10])
dcplt.plot(t, voltage, color='blue', label="Inductor Voltage")
dcplt.plot(t, current, color='red', linestyle=':', label="Inductor Current")
dcplt.set_title("Transient DC - Inductor Voltage vs Current")
dcplt.set_ylabel("V/I")
dcplt.set_xlabel('milliseconds')
dcplt.legend()


plt.subplots_adjust(hspace = 0.75)
plt.show()

#How to enter symbols using TeX
#xtick_labels = ['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$']

#Creating different subplots
#plt.subplot(2, 1, 1) #(rows, columns, selected plot)
