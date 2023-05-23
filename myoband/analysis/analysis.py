import numpy as np
# Plotting:
from matplotlib import pyplot as plt
from matplotlib.pyplot import cm
from matplotlib.colors import colorConverter
import matplotlib as mpl
from ..plotting import imshow

## Better cmaps
from mycolorpy import colorlist as mcp

# Polygons: fast detection of points within polygon
from matplotlib.patches import Rectangle,Circle
from matplotlib.path import Path
## Better polygons: dilates random walk path into polygon
from shapely.geometry import LineString
from shapely.plotting import plot_polygon, plot_line
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

# Image analysis: find contour of image and skeleton of polygon
import skimage

def contour(slide):
    if len(np.shape(slide))==3:
        slide=np.sum(slide,axis=0)
    return skimage.measure.find_contours(slide, 0.9)

# def contour(self,ax):
#     self.get_contours()
#     colours=mcp.gen_color(cmap="Set1",n=len(self.contours))
#     for i,contour in enumerate(self.contours):
#         ax.plot(contour[:, 1], contour[:, 0], linewidth=2, c=colours[i])
#     return ax

def skeleton(slide):
    """
    Returns an array of dimensions of the slide. The array is zeros, with ones only where the skeleton is located.
    """
    return skimage.morphology.skeletonize(slide, method='lee') # 'lee' avoid bifurications

def get_pts(skeletons):

    pts={}
    for i in range(len(skeletons)):
        pts[i]=np.nonzero(skeletons[i].T)
    return pts

# slide=DirtySlide(30,15,0.1,0.1)
# n_bands=5
# A_bands = [A_Band(origin=[5+5*i,0],radius=0.5,length=20,σr=0.05,σθ=0.1,r0=2) for i in range(n_bands)]
# slide.add_A_bands(A_bands)
# fig, ax = plt.subplots()
# # A_bands[0].plot_polynomial()
# # plt.show()
# # exit()
# # slide.plot_A_bands(ax)
# # plt.show()
# # exit()
# # slide.get_dirty_slide()
# # slide=slide.get_compressed_slide()
# slide=slide.get_slide()
# processing = SlideAnalysis(slide)
# skeletons=processing.get_skeletons()
# processing.plot_skeletons(ax)
# processing.plot_contours(ax)
# ax.axis('image')
# ax.set_xticks([])
# ax.set_yticks([])
# plt.show()
# exit()




# skimage.morphology.skeletonize

# exit()
# plt.show()

# exit()

# fig,ax=plt.subplots()
# slide.plot_A_bands(ax)

# plt.show()

# exit()


# fig, ax = plt.subplots()
# A_bands[0].plot_A_band()
# plt.show()
# exit()

# class CleanSlide():
#     """
    
#     """


        

# nm=5 # number of A_bands
# ne=3 # number of edges per A_band
# A_bands=np.array([[0.5*np.random.random_sample() - i for i in range(nm)] for _ in range(ne)]).T # create nm A_bands with random spacing and ne edges
# []
# print(np.shape(x))
# exit()

# # count_a = 2
# # r = 2.5
# # r_squared = r * r
# # a_tuples = [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(count_a)]
# # b = (random.uniform(4, 8), random.uniform(4, 8))
# # print(a_tuples)
# # print(b)
# # exit()
# # def method3():
# #     """Using 1d arrays means loops are performed in C vector operations"""
# #     x, y = a_arrs
# #     dx = x - b[0]
# #     dy = y - b[1]
# #     return np.nonzero(((dx * dx) + (dy * dy)) <= r_squared)[0]
# # print(np.shape(x))
# plt.plot(x)
# plt.show()
