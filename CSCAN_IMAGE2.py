import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd
from pandas import Series, DataFrame 
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import interp1d
import ipyvolume as ipv
import cv2


def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)

#PATH
#input_path1="/home/changwan/GPR/C_SCAN_IMAGE_GPR_flip.txt"
#input_path2="/home/changwan/GPR/3D_IMAGE_GPR.txt"
input_path2="L:/MOGOD_GPR/2021/3D_CUBE_IMAGE_GPR.txt"



#READ DATASET
#data=np.loadtxt(input_path1)
data2=np.loadtxt(input_path2)


#C_SCAN_IMAGE


#RESAHPE THE INPUT DATA
#READ TEXT MADE BY FORTRAN PRINTED FOR THE MATRIX (J,I,K).
#BUT, THE PYTHON READ THE FILE AS THE STRUCTURE (J x I, K).
#FOR INSTANCE, IF THE STURCTURE IS (50,2300,100), 
#THE STRCUTURE READ is (115000,100).


print(data2.shape)    
data2_2=data2.reshape(50,2300,100)

print(data2_2.shape)


fig,host =plt.subplots()

print(data2_2.shape[0])

#print(data2_2.shape[1])
#print(data2_2.shape[2])

ay1_min=0
ay1_max=data2_2.shape[1]*0.05 #This is Northting.
ax1_min=0
ax1_max=data2_2.shape[2]*1 #This is Easting.

#data2_2[:,1500:2000,50] = 1000000 #Check the direction of the graph





#     ++++++++++++++++++++++
#++++++Before interploation++++++
#     ++++++++++++++++++++++
#depth = 1
#print
rows=list(range(data2_2.shape[0]))

#     ++++++++++++++++++++
#++++++Remove the average++++++
#     ++++++++++++++++++++

for depth in rows:

 data2_2[depth,:,:] = data2_2[depth,:,:] - np.mean(data2_2[depth,:,:])


for depth in rows:

# depth = int(input('Please enter the sample that you want. \n'))
# type(depth)

 plt.imshow(data2_2[depth,:,:]
           ,extent=(ax1_min,ax1_max,ay1_min,ay1_max)
           ,aspect="auto"
           ,cmap='gist_gray'
           ,interpolation = 'spline16')


#plt.imshow(data2_2[380,:,:],aspect="auto")
#plt.imshow(data2_2[380,:,:])
#plt.colorbar()

 plt.colorbar()
 plt.title("F1_500 MHz_survey_line_Int._1m", fontweight="bold")
 plt.xlabel("Easting [m]. Survey line interval_1 m")
 #plt.title("F1_250 MHz_survey_line_Int._1m", fontweight="bold")
 #plt.xlabel("Easting [m]. Survey line interval_2 m")


 plt.ylabel("Northing [m]. Distance interval_0.05 m")
 plt.grid()
 plt.show(block=False)
 plt.draw()
 plt.pause(0.5)
 fig.clear()

plt.grid()
plt.show()
#
#      +++++++++++++++
#+++++++Interpolation++++++
#      +++++++++++++++

"""
x=np.arange(0,data2_2.shape[2],1)
xint = np.linspace(x.min(), x.max(), 1000)
yint2d=np.zeros((1,data2_2.shape[1],xint.shape[0]))
d_profile=np.arange(0, data2_2.shape[1],1)
"""

#     ++++++++++++++++++
#++++++1D interpolation++++++
#     ++++++++++++++++++

#fq = interp1d(x,data2_2[380,100,:], kind = 'quadratic')
#yintq=fq(xint)
#plt.plot(xint, yintq, 'ro')
#plt.plot(x,data2_2[380,100,:],'bo')


#     ++++++++++++++++++++++++++++++++++++++
#++++++2D interpolatian along one direction++++++
#     ++++++++++++++++++++++++++++++++++++++
"""
for i in d_profile:

 fq = interp1d(x,data2_2[380,i,:], kind = 'quadratic')

 yint2d[0][i][:] =  fq(xint)
"""
#     ++++++++++++++++++
#++++++Tick designation++++++
#     ++++++++++++++++++
"""
ax1_min=0
ax1_max=yint2d.shape[1]*0.05
ay1_min=0

interval=0.5 *19 / 1000
print(interval)

ay1_max=yint2d.shape[2]*interval
"""

#plt.imshow(yint2d[0,:,:],extent=(ax1_min,ax1_max,ay1_min,ay1_max),aspect="auto")
#plt.imshow(yint2d[0,:,:],aspect="auto")
#plt.colorbar()


#plt.imshow(yint2d[0,:,:],aspect="auto")
#plt.colorbar()


#     ++++++++++
#++++++1D check++++++
#     ++++++++++
#plt.plot(xint,yint2d[0,100,:],'ro')
#plt.plot(x,data2_2[380,100,:],'bo')

#plt.grid()
#plt.show()

#print(yint2d.shape)

#ipv.figure()
#ipv.quickvolshow(yint2d)
#ipv.quickvolshow(data2_2)

#ipv.show()

"""
#B_SCAN_IMAGE
fig, host=plt.subplots(figsize=(15,18))

plt.title('item_name',fontsize=40)
plt.grid()

par1 = host.twiny()
par2 = host.twiny()

par2.spines["top"].set_position(("axes",1.1))
make_patch_spines_invisible(par2)
par2.spines["top"].set_visible(True)


par1_min=data_2.loc[0,['SC_Lat']]               
par1_max=data_2.loc[len(data_2)-1,['SC_Lat']]
par2_min=data_2.loc[0,['SC_Long']]               
par2_max=data_2.loc[len(data_2)-1,['SC_Long']]


ax1_min=0
ax1_max=len(data_2)*0.075
ay1_min=1000*0.025
ay1_max=0

#host.imshow(B_SCAN_IMAGE,'rainbow', aspect="auto")
#host.imshow(B_SCAN_IMAGE,'rainbow', aspect="auto")
host.imshow(B_SCAN_IMAGE,extent=(ax1_min,ax1_max,ay1_min,ay1_max),aspect="auto")


#B_SCAN_IMAGE_LIMIT
#host.set_ylim(ay1_min,ay1_max)
host.set_xlim(ax1_min,ax1_max)
par1.set_xlim(par1_min.item(),par1_max.item())
par2.set_xlim(par2_min.item(),par2_max.item())

#B_SCAN_IMAGE_LABEL

host.set_ylabel('DEPTH [KM]', fontsize=15)
host.set_xlabel('DISTANCE [KM]', fontsize=15)
par1.set_xlabel('LATITUDE [DEGREE]', fontsize=15)
par2.set_xlabel('LONGITUDEE [DEGREE]', fontsize=15)

#B_SCAN_IMAGE_TICK
host.tick_params(which="both", width=2)
host.tick_params(which="major",length=7)
par1.tick_params(which="both", width=2)
par1.tick_params(which="major",length=7)
par2.tick_params(which="both", width=2)
par2.tick_params(which="major",length=7)

#B_SCAN_IMAGE_MINORTICK
host.minorticks_on()
host.tick_params(which="minor",length=4,color='r')
par1.minorticks_on()
par1.tick_params(which="minor",length=4,color='r')
par2.minorticks_on()
par2.tick_params(which="minor",length=4,color='r')


#INTESNTIY#
plt.figure()
plt.title('item_number',fontsize=40)

plt.grid()

plt.plot(INTENSITY,color='black')

xt=np.arange(0,1200,200)
plt.xticks(xt,(i*0.025 for i in xt),fontsize=10)

plt.ylabel("INTENSITY [dB]",fontsize=20)
plt.xlabel("Depth [km]",fontsize=20)
plt.tick_params(which="both", width=2)
plt.tick_params(which="major",length=7)
plt.minorticks_on()
plt.tick_params(which="minor",length=4,color='r')
"""

#plt.show()



