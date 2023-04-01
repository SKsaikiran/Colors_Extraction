#!/usr/bin/env python
# coding: utf-8

# In[21]:


#To extract the percentage of colors and segregate them in a single input image and display the highlighted highest color point and the color percentage graph as ouput


# In[48]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[49]:


# Load the image
img = cv2.imread('C:/Users/Sai Kiran/Desktop/Sample/Luffy.jpg')


# In[50]:


# Convert the image from RGB to HSV color space
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


# In[51]:


# Define the ranges for each color in HSV color space
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])
lower_green = np.array([50, 50, 50])
upper_green = np.array([70, 255, 255])
lower_yellow = np.array([20, 50, 50])
upper_yellow = np.array([30, 255, 255])
lower_orange = np.array([10, 50, 50])
upper_orange = np.array([20, 255, 255])
lower_purple = np.array([130, 50, 50])
upper_purple = np.array([150, 255, 255])
lower_pink = np.array([150, 50, 50])
upper_pink = np.array([170, 255, 255])
lower_gray = np.array([0, 0, 50])
upper_gray = np.array([180, 50, 255])
lower_brown = np.array([0, 50, 50])
upper_brown = np.array([10, 255, 255])
lower_cyan = np.array([80, 50, 50])
upper_cyan = np.array([100, 255, 255])
lower_magenta = np.array([150, 50, 50])
upper_magenta = np.array([170, 255, 255])


# In[52]:


# Create a mask for each color range and apply it to the image to extract that color
red_mask = cv2.inRange(hsv_img, lower_red, upper_red)
blue_mask = cv2.inRange(hsv_img, lower_blue, upper_blue)
green_mask = cv2.inRange(hsv_img, lower_green, upper_green)
yellow_mask = cv2.inRange(hsv_img, lower_yellow, upper_yellow)
orange_mask = cv2.inRange(hsv_img, lower_orange, upper_orange)
purple_mask = cv2.inRange(hsv_img, lower_purple, upper_purple)
pink_mask = cv2.inRange(hsv_img, lower_pink, upper_pink)
gray_mask = cv2.inRange(hsv_img, lower_gray, upper_gray)
brown_mask = cv2.inRange(hsv_img, lower_brown, upper_brown)
cyan_mask = cv2.inRange(hsv_img, lower_cyan, upper_cyan)
magenta_mask = cv2.inRange(hsv_img, lower_magenta, upper_magenta)


# In[53]:


# Calculate the percentage of each color in the image
total_pixels = img.shape[0] * img.shape[1]
red_percentage = (cv2.countNonZero(red_mask) / total_pixels) * 100
blue_percentage = (cv2.countNonZero(blue_mask) / total_pixels) * 100
green_percentage = (cv2.countNonZero(green_mask) / total_pixels) * 100
yellow_percentage = (cv2.countNonZero(yellow_mask) / total_pixels) * 100
orange_percentage = (cv2.countNonZero(orange_mask) / total_pixels) * 100
purple_percentage = (cv2.countNonZero(purple_mask) / total_pixels) * 100
pink_percentage = (cv2.countNonZero(pink_mask) / total_pixels) * 100
gray_percentage = (cv2.countNonZero(gray_mask) / total_pixels) * 100
brown_percentage = (cv2.countNonZero(brown_mask) / total_pixels) * 100
cyan_percentage = (cv2.countNonZero(cyan_mask) / total_pixels) * 100
magenta_percentage = (cv2.countNonZero(magenta_mask) / total_pixels) * 100


# In[54]:


# Display the accuracy and color name and its percentage as output
print(f"Red: {red_percentage}%")
print(f"Blue: {blue_percentage}%")
print(f"Green: {green_percentage}%")
print(f"Yellow: {yellow_percentage}%")
print(f"Orange: {orange_percentage}%")
print(f"purple: {purple_percentage}%")
print(f"Pink: {pink_percentage}%")
print(f"Gray: {gray_percentage}%")
print(f"Brown: {brown_percentage}%")
print(f"Cyan: {cyan_percentage}%")
print(f"Magenta: {magenta_percentage}%")


# In[55]:


color_dict = {'red': red_percentage,
              'blue': blue_percentage,
              'green': green_percentage,
              'yellow': yellow_percentage,
              'orange': orange_percentage,
              'purple': purple_percentage,
              'pink': pink_percentage,
              'gray': gray_percentage,
              'brown': brown_percentage,
              'cyan': cyan_percentage,
              'magenta': magenta_percentage}


# In[56]:


plt.bar(color_dict.keys(), color_dict.values())
plt.show()


# In[57]:


cv2.circle(img, (y, x), 5, (0, 0, 255), -1)


# In[58]:


img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[59]:


cv2.putText(img, f'Highest color point: ({y},{x})', (20, img.shape[0] + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)


# In[60]:


fig, ax = plt.subplots(figsize=(10, 8))
ax.imshow(img)
plt.subplots_adjust(bottom=0.2)
plt.show()

