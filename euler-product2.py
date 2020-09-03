#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 23:45:45 2020
Euler's product formula for sin(x)
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(start=-8,stop=8,num=100)

y0 = x

y1 = x*(1 - (x/np.pi)**2 )

y2 = y1*(1 - (x/(2*np.pi))**2 )

y3 = y2 * (1 - (x/(3*np.pi))**2 )

y4 = y3 * (1 - (x/(4*np.pi))**2 )

y5 = y4 * (1 - (x/(5*np.pi))**2 )


y6 = np.sin(x)


# plt.plot(x,y1, color='red') 
# plt.plot(x,y2, color='red') 
# plt.plot(x,y3, color='red')
# plt.plot(x,y4, color='red')
# plt.plot(x,y5, color='red')
# plt.plot(x,y6, color='blue')

plt.subplot(3,2,1)
plt.plot(x,x, color='red') # y0 is the tangent line
plt.plot(x,y6, color='blue')

plt.xlim(-10,10)
plt.ylim(-5,5)

plt.subplot(3,2,2)
plt.plot(x,y1, color='red')
plt.plot(x,y6, color='blue')

plt.xlim(-10,10)
plt.ylim(-5,5)


plt.subplot(3,2,3)
plt.plot(x ,y2 , color='red')
plt.plot(x ,y6 , color='blue')

plt.xlim(-10,10)
plt.ylim(-5,5)


plt.subplot(3,2,4)
plt.plot(x ,y3 , color='red')
plt.plot(x ,y6 , color='blue')

plt.xlim(-10,10)
plt.ylim(-5,5)


plt.subplot(3,2,5)
plt.plot(x ,y4 , color='red')
plt.plot(x ,y6 , color='blue')

plt.xlim(-10,10)
plt.ylim(-5,5)


plt.subplot(3,2,6)
plt.plot(x ,y5 , color='red')
plt.plot(x ,y6 , color='blue')

plt.xlim(-10,10)
plt.ylim(-5,5)


plt.show()



