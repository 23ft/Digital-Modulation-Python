from matplotlib import pyplot as plt
import numpy as np

plt.rcParams["figure.autolayout"] = True

x_values = [-1.5,-1,1,1.5]
y_values = [0]*4
fig, axis = plt.subplots(1,2,sharex='col')
fig.suptitle('QPSK Modulation', fontsize=12)

axis[0].set_title('Constelation Diagram')
axis[0].set_xlabel('Time [s]')
#axis[0].set_ylabel('Amplitude [V]')
#axis[0].set_xlim(0,timeDomainVisibleLimit)
axis[0].grid(linestyle='dotted')
axis[0].plot(1,1,marker="o", markersize=10, color="red")
axis[0].plot(1,-1, marker="o", markersize=10, color="red")
axis[0].plot(-1,1, marker="o", markersize=10, color="red")
axis[0].plot(-1,-1, marker="o", markersize=10, color="red")
axis[0].plot(x_values,y_values, color="black")
axis[0].plot(y_values,x_values, color="black")
axis[0].set_xlim(-2, 2)
axis[0].set_ylim(-2, 2)    

axis[1].set_title('Phasorial Diagram')
axis[1].set_xlabel('Time [s]')
#axis[0].set_ylabel('Amplitude [V]')
#axis[0].set_xlim(0,timeDomainVisibleLimit)
axis[1].grid(linestyle='dotted')
axis[1].plot(1,1, markersize=10, color="red")
axis[1].plot(1,-1,  markersize=10, color="red")
axis[1].plot(-1,1,  markersize=10, color="red")
axis[1].plot(-1,-1, markersize=10, color="red")

axis[1].arrow(0,0,1,1,head_width=0.2, head_length=0.2) 
axis[1].arrow(0,0,1,-1,head_width=0.2, head_length=0.2)
axis[1].arrow(0,0,-1,1,head_width=0.2, head_length=0.2)
axis[1].arrow(0,0,-1,-1,head_width=0.2, head_length=0.2)

axis[1].plot(x_values,y_values, color="black")
axis[1].plot(y_values,x_values, color="black")
axis[1].set_xlim(-2, 2)
axis[1].set_ylim(-2, 2)    


plt.show()
