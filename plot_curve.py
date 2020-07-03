"""
use matplot
"""

import os
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

# set the output dir path
code_path = os.path.dirname(os.path.realpath(__file__))

output_dir = os.path.join(code_path,'output')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

curve_dir = os.path.join(output_dir,'curve')
if not os.path.exists(curve_dir):
    os.makedirs(curve_dir)

# plot 2 curves with 2 subplot in one figure
def plot_curve(data_list1,data_list2):
    fig,(ax1,ax2) = plt.subplots(1,2,figsize=(19,8))
    plt.title('Learning Curve',fontsize=18)     # figure title

    ax1.plot(data_list1,'-b',label='data1')     # plot the data_list1, give the label name
    ax1.set_title('Learning Curve',fontsize=18)
    ax1.set_xlabel('epoch number',fontsize=14)
    ax1.set_ylabel('Cross entropy',fontsize=14)
    ax1.legend(loc='upper right')

    ax2.plot( data_list2,'-b',label='data2')     # plot the data_list1, give the label name
    ax2.set_title('Accuracy',fontsize=18)
    ax2.set_xlabel('epoch number',fontsize=14)
    ax2.set_ylabel('accuracy rate',fontsize=14)
    ax2.legend()

    save_path = os.path.join(curve_dir,'learning_curve.png')
    fig.savefig(save_path)                      # save figure
    plt.clf()
    plt.close(fig)
    return

# plot the dynamic curve in loop
def plot_ion():
    x_list = []
    
    # dynamic data list
    data_list1 = []
    data_list2 = []
    data_list3 = []

    fig,(ax1, ax2, ax3) = plt.subplots(1,3,figsize=(19,8))
    plt.ion()
    for i in range(10):
        
        # plt.subplot(3,1,1)
        ax1.cla()
        ax1.plot( x_list,data_list1,'-b')
        ax1.set_title('data 1)',fontsize=18)
        ax1.set_xlabel('x',fontsize=14)
        ax1.set_ylabel('data 1',fontsize=14)
        # plt.subplot(3,1,2)
        ax2.cla()
        ax2.plot( x_list,data_list2,'-b')
        ax2.set_title('data 2',fontsize=18)
        ax2.set_xlabel('x',fontsize=14)
        ax2.set_ylabel('data 2',fontsize=14)
        # plt.subplot(3,1,3)
        ax3.cla()
        ax3.plot( x_list,data_list3,'-b')
        ax3.set_title('data 3',fontsize=18)
        ax3.set_xlabel('x',fontsize=14)
        ax3.set_ylabel('data 3',fontsize=14)
        plt.pause(0.1)

        """
        update the data list 1~3
        """
    plt.ioff()
    save_path = os.path.join(curve_dir,'curve.png')
    fig.savefig(save_path)

def visualize_animate(img_list):
    fig = plt.figure(figsize=(8,8))
    plt.axis("off")
    ## Animation for your generation
    # https://matplotlib.org/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.save
    ## input : image_list (size = (the number of sample times, how many samples created each time, image )   )
    ims = [[plt.imshow(np.transpose(i,(1,2,0)), animated=True)] for i in img_list]
    ani = animation.ArtistAnimation(fig, ims, interval=1000, repeat_delay=1000, blit=True)  # make the img_list to animation object
    save_path = os.path.join(curve_dir,'image.gif')
    ani.save(save_path, writer='imagemagick', fps=1)    # save the animation as gif
    plt.show()
    plt.clf()
    plt.close(fig)

    for i,img in enumerate(img_list):
        fig = plt.figure(figsize=(8,8))
        plt.axis("off")
        plt.imshow(np.transpose(img,(1,2,0)))
        save_path = os.path.join(curve_dir,'5epoch_image_'+str(i)+'.png')   # save the image per frame from img_list
        fig.savefig(save_path,dpi=fig.dpi,bbox_inches='tight',pad_inches=0.0)
        plt.clf()
        plt.close(fig)

    return