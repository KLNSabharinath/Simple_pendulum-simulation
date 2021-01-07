
# coding: utf-8

# In[4]:


import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as pyplot


# In[5]:


theta_start=np.pi/3
theta_change=0.0


# In[6]:


def pendulum(theta, wid=200, hei=200, m=1, l=1):
    img = Image.new("RGB",(wid,hei),'White')
    L = int(0.4*hei*l)
    d = int(0.02*hei)*m**(1/3)
    draw = ImageDraw.Draw(img)
    
    x0 = int(wid/2)
    y0 = int(hei/2)
    x = x0 + L*(np.sin(theta))
    y = y0 + L*(np.cos(theta))
    
    draw.line([(x0,y0),(x,y)],fill=(0,0,0),width=1)
    draw.ellipse([(x-d,y-d),(x+d,y+d)],fill=(0,0,255),outline=None)
    return img


# In[7]:


img= pendulum(theta_start)
img.show()


# In[8]:


def energy(theta,theta_change,m=1,l=1,g=9.8):
    y = l*(np.cos(theta))           #height of the mass
    epot = m*y*g                    #potential energy  
    ekin = m/2*(l*theta_change)**2      #kinetic energy
    return epot, ekin


# In[9]:


epot,ekin=energy(theta_start, theta_change)
print('potential energy: '+str(epot)[:5])
print('kinetic energy: '+str(ekin)[:5])


# In[10]:


def trajectory(theta_start, theta_change, iter=1000, dt=0.1, g=9.8, l=1):
    phase_traject=np.zeros((iter,2))                            #phase-space trajectory
    phase_traject[0,:] = np.array([theta_start,theta_change])
    
    for i in range(iter-1):
        theta_dd = -(g/l)*np.sin(phase_traject[i,0])
        phase_traject[i+1,1] = phase_traject[i,1] + dt*theta_dd
        phase_traject[i+1,0] = phase_traject[i,0] + dt*phase_traject[i,1]
    return phase_traject


# In[19]:


frames_per_sec = 20
frame_every=(1/(dt*(frames_per_sec)))


# In[131]:


frames = []
def render_traject(phase_traject, m=1, l=1, g=9.8, save_path='', frame_every =1):
    #frames=[]
    
    for i in range(phase_traject.shape[0]):
        if i % frame_every == 0:
            theta=phase_traject[i,0]
            theta_d=phase_traject[i,1]
            
            img=pendulum(theta,wid=200,hei=200,m=m,l=l)
            frames.append(img)
            name= r"C:\Users\DELL\Desktop\simulation\images_" + str(i) + '.jpg'
            img.save(name,'JPEG')
            


# In[132]:


render_traject(phase_traject, frame_every = frame_every)

