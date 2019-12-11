# %% [markdown]
# # Final Project

# Loading libraries
from skimage import exposure
import numpy as np
from PIL import Image, ImageFilter
from skimage.filters import threshold_minimum, threshold_otsu
from skimage.filters import try_all_threshold
from skimage.filters import threshold_mean
from skimage import io as sk_io, color as sk_col, morphology as sk_mm
from IPython import get_ipython
import pydicom
import SimpleITK
import os
import numpy
import matplotlib.pyplot as plt

import pandas as pd
import cv2 as cv

from skimage import measure
from skimage.transform import resize
from sklearn.cluster import KMeans

from scipy import ndimage
import skimage.color as sc
import numpy as np


# %%
# Load the image from the source file
image_file = "DataP/T1_0005_D5.png"
image_sk = sk_io.imread(image_file)

fig = plt.figure(figsize=(6, 6))
plt.imshow(image_sk)
plt.show()


# %%
print(image_sk)

plt.hist(image_sk.ravel())
plt.show()

plt.hist(image_sk.ravel(), bins=255, cumulative=True)
plt.show()

# %%

# Contrast stretching
p2 = np.percentile(image_sk, 2)
p98 = np.percentile(image_sk, 98)
image_ct = exposure.rescale_intensity(image_sk, in_range=(p2, p98))

# Histogram Equalization
image_eq = exposure.equalize_hist(image_sk)

# Show the images
fig = plt.figure(figsize=(20, 12))

# Subplot for original image
a = fig.add_subplot(3, 3, 1)
imgplot = plt.imshow(image_sk)
a.set_title('Original')

# Subplot for contrast stretched image
a = fig.add_subplot(3, 3, 2)
imgplot = plt.imshow(image_ct)
a.set_title('Contrast Stretched')

# Subplot for equalized image
a = fig.add_subplot(3, 3, 3)
imgplot = plt.imshow(image_eq)
a.set_title('Histogram Equalized')

# Subplots for histograms
a = fig.add_subplot(3, 3, 4)
imgplot = plt.hist(image_sk.ravel())

a = fig.add_subplot(3, 3, 5)
imgplot = plt.hist(image_ct.ravel())

a = fig.add_subplot(3, 3, 6)
imgplot = plt.hist(image_eq.ravel())

# Subplots for CDFs

a = fig.add_subplot(3, 3, 7)
imgplot = plt.hist(image_sk.ravel(), bins=255, cumulative=True)

a = fig.add_subplot(3, 3, 8)
imgplot = plt.hist(image_ct.ravel(), bins=255, cumulative=True)

a = fig.add_subplot(3, 3, 9)
imgplot = plt.hist(image_eq.ravel(), bins=255, cumulative=True)

plt.show()

# %%
# Apply operations
eroded_image = sk_mm.erosion(image_sk)
dilated_image = sk_mm.dilation(image_sk)
closed_image = sk_mm.closing(image_sk)
opened_image = sk_mm.opening(image_sk)

# Display it
fig = plt.figure(figsize=(20, 20))

# Plot original image
a = fig.add_subplot(5, 1, 1)
plt.imshow(image_sk, cmap="gray")
a.set_title("Original")

# Plot eroded image
a = fig.add_subplot(5, 1, 2)
plt.imshow(eroded_image, cmap="gray")
a.set_title("Eroded")

# Plot dilated image
a = fig.add_subplot(5, 1, 3)
plt.imshow(dilated_image, cmap="gray")
a.set_title("Dilated")

# Plot closed image
a = fig.add_subplot(5, 1, 4)
plt.imshow(closed_image, cmap="gray")
a.set_title("Closed")

# Plot opened image
a = fig.add_subplot(5, 1, 5)
plt.imshow(opened_image, cmap="gray")
a.set_title("Opened")

plt.show()


# %%
# Apply operations to Equalize Image
eq_eroded_image = sk_mm.erosion(image_eq)
eq_dilated_image = sk_mm.dilation(image_eq)
eq_closed_image = sk_mm.closing(image_eq)
eq_opened_image = sk_mm.opening(image_eq)

# Display it
fig = plt.figure(figsize=(20, 20))

# Plot equalize image
a = fig.add_subplot(5, 1, 1)
plt.imshow(image_eq, cmap="gray")
a.set_title("Equalize")

# Plot eroded image
a = fig.add_subplot(5, 1, 2)
plt.imshow(eq_eroded_image, cmap="gray")
a.set_title("Eroded")

# Plot dilated image
a = fig.add_subplot(5, 1, 3)
plt.imshow(eq_dilated_image, cmap="gray")
a.set_title("Dilated")

# Plot closed image
a = fig.add_subplot(5, 1, 4)
plt.imshow(eq_closed_image, cmap="gray")
a.set_title("Closed")

# Plot opened image
a = fig.add_subplot(5, 1, 5)
plt.imshow(eq_opened_image, cmap="gray")
a.set_title("Opened")

plt.show()

# %%

# Apply operations Contrast Stretched
ct_eroded_image = sk_mm.erosion(image_ct)
ct_dilated_image = sk_mm.dilation(image_ct)
ct_closed_image = sk_mm.closing(image_ct)
ct_opened_image = sk_mm.opening(image_ct)

# Display it
fig = plt.figure(figsize=(20, 20))

# Plot contrast image
a = fig.add_subplot(5, 1, 1)
plt.imshow(image_ct, cmap="gray")
a.set_title("Contrast Stretched")

# Plot eroded image
a = fig.add_subplot(5, 1, 2)
plt.imshow(ct_eroded_image, cmap="gray")
a.set_title("Eroded")

# Plot dilated image
a = fig.add_subplot(5, 1, 3)
plt.imshow(ct_dilated_image, cmap="gray")
a.set_title("Dilated")

# Plot closed image
a = fig.add_subplot(5, 1, 4)
plt.imshow(ct_closed_image, cmap="gray")
a.set_title("Closed")

# Plot opened image
a = fig.add_subplot(5, 1, 5)
plt.imshow(ct_opened_image, cmap="gray")
a.set_title("Opened")

plt.show()


# %%
# Standardize the pixel values
def make_mask(img, display=False):
    row_size = img.shape[0]
    col_size = img.shape[1]

    mean = np.mean(img)
    std = np.std(img)
    img = img-mean
    img = img/std
    # Find the average pixel value near the lungs
    # to renormalize washed out images
    middle = img[int(col_size/5):int(col_size/5*4),
                 int(row_size/5):int(row_size/5*4)]
    mean = np.mean(middle)
    max = np.max(img)
    min = np.min(img)
    # To improve threshold finding, I'm moving the
    # underflow and overflow on the pixel spectrum
    img[img == max] = mean
    img[img == min] = mean
    #
    # Using Kmeans to separate foreground (soft tissue / bone) and background (lung/air)
    #
    kmeans = KMeans(n_clusters=2).fit(
        np.reshape(middle, [np.prod(middle.shape), 1]))
    centers = sorted(kmeans.cluster_centers_.flatten())
    threshold = np.mean(centers)
    thresh_img = np.where(img < threshold, 1.0, 0.0)  # threshold the image

    # First erode away the finer elements, then dilate to include some of the pixels surrounding the lung.
    # We don't want to accidentally clip the lung.

    eroded = sk_mm.erosion(thresh_img, np.ones([3, 3]))
    dilation = sk_mm.dilation(eroded, np.ones([8, 8]))

    # Different labels are displayed in different colors
    labels = measure.label(dilation)
    label_vals = np.unique(labels)
    regions = measure.regionprops(labels)
    good_labels = []
    for prop in regions:
        B = prop.bbox
        if B[2]-B[0] < row_size/10*9 and B[3]-B[1] < col_size/10*9 and B[0] > row_size/5 and B[2] < col_size/5*4:
            good_labels.append(prop.label)
    mask = np.ndarray([row_size, col_size], dtype=np.int8)
    mask[:] = 0

    #
    #  After just the lungs are left, we do another large dilation
    #  in order to fill in and out the lung mask
    #
    for N in good_labels:
        mask = mask + np.where(labels == N, 1, 0)
    mask = sk_mm.dilation(mask, np.ones([10, 10]))  # one last dilation

    if (display):
        fig, ax = plt.subplots(3, 2, figsize=[12, 12])
        ax[0, 0].set_title("Original")
        ax[0, 0].imshow(img, cmap='gray')
        ax[0, 0].axis('off')
        ax[0, 1].set_title("Threshold")
        ax[0, 1].imshow(thresh_img, cmap='gray')
        ax[0, 1].axis('off')
        ax[1, 0].set_title("After Erosion and Dilation")
        ax[1, 0].imshow(dilation, cmap='gray')
        ax[1, 0].axis('off')
        ax[1, 1].set_title("Color Labels")
        ax[1, 1].imshow(labels)
        ax[1, 1].axis('off')
        ax[2, 0].set_title("Final Mask")
        ax[2, 0].imshow(mask, cmap='gray')
        ax[2, 0].axis('off')
        ax[2, 1].set_title("Apply Mask on Original")
        ax[2, 1].imshow(mask*img, cmap='gray')
        ax[2, 1].axis('off')

        plt.show()
    return mask*img


# %%
make_mask(image_sk, display=True)

# %%
box = (100, 120, 220, 270)
print("Dilated Images")

# Display it
fig = plt.figure(figsize=(20, 20))


crop_dilated_image = Image.fromarray(dilated_image, 'L').crop(box)
a = fig.add_subplot(5, 1, 1)
a.set_title("Crop Dilated Image")
plt.imshow(crop_dilated_image, "gray")
plt.show()

crop_eq_dilated_image = Image.fromarray(eq_dilated_image, 'L').crop(box)
a = fig.add_subplot(5, 1, 2)
a.set_title("crop_eq_dilated_image")
plt.imshow(crop_eq_dilated_image, "gray")
plt.show()

crop_ct_dilated_image = Image.fromarray(ct_dilated_image, 'L').crop(box)
a = fig.add_subplot(5, 1, 3)
a.set_title("crop_ct_dilated_image")
plt.imshow(crop_ct_dilated_image, "gray")

plt.show()
# %%
print("Eroded Images")

# Display it
fig = plt.figure(figsize=(20, 20))


crop_eroded_image = Image.fromarray(eroded_image, 'L').crop(box)
a = fig.add_subplot(5, 1, 1)
a.set_title("Crop Eroded Image")
plt.imshow(crop_eroded_image, "gray")
plt.show()

crop_eq_eroded_image = Image.fromarray(eq_eroded_image, 'L').crop(box)
a = fig.add_subplot(5, 1, 2)
a.set_title("crop_eq_eroded_image")
plt.imshow(crop_eq_eroded_image, "gray")
plt.show()

crop_ct_eroded_image = Image.fromarray(ct_eroded_image, 'L').crop(box)
a = fig.add_subplot(5, 1, 3)
a.set_title("crop_ct_eroded_image")
plt.imshow(crop_ct_eroded_image, "gray")

plt.show()


# %%
print("Closed Images")

# Display it
fig = plt.figure(figsize=(20, 20))


crop_closed_image = Image.fromarray(closed_image, 'L').crop(box)
a = fig.add_subplot(5, 1, 1)
a.set_title("Crop Closed Image")
plt.imshow(crop_closed_image, "gray")
plt.show()

crop_eq_closed_image = Image.fromarray(eq_closed_image, 'L').crop(box)
a = fig.add_subplot(5, 1, 2)
a.set_title("crop_eq_closed_image")
plt.imshow(crop_eq_closed_image, "gray")
plt.show()

crop_ct_closed_image = Image.fromarray(ct_closed_image, 'L').crop(box)
a = fig.add_subplot(5, 1, 3)
a.set_title("crop_ct_closed_image")
plt.imshow(crop_ct_closed_image, "gray")

plt.show()


# %%
print("Opened Images")

# Display it
fig = plt.figure(figsize=(20, 20))


crop_opened_image = Image.fromarray(opened_image, 'L').crop(box)
a = fig.add_subplot(5, 1, 1)
a.set_title("Crop Opened Image")
plt.imshow(crop_opened_image, "gray")
plt.show()

crop_eq_opened_image = Image.fromarray(eq_opened_image, 'L').crop(box)
a = fig.add_subplot(5, 1, 2)
a.set_title("crop_eq_opened_image")
plt.imshow(crop_eq_opened_image, "gray")
plt.show()

crop_ct_opened_image = Image.fromarray(ct_opened_image, 'L').crop(box)
a = fig.add_subplot(5, 1, 3)
a.set_title("crop_ct_opened_image")
plt.imshow(crop_ct_opened_image, "gray")

plt.show()


# %%
print("Creating an array of images to see which one is better. We excluded the equalize images")
print()
crop_images = {}
crop_images['crop_dilated_image'] = crop_dilated_image
crop_images['crop_ct_dilated_image'] = crop_ct_dilated_image

crop_images['crop_eroded_image'] = crop_eroded_image
crop_images['crop_ct_eroded_image'] = crop_ct_eroded_image

crop_images['crop_closed_image'] = crop_closed_image
crop_images['crop_ct_closed_image'] = crop_ct_closed_image

crop_images['crop_opened_image'] = crop_opened_image
crop_images['crop_ct_opened_image'] = crop_ct_opened_image

# %%

print("Now we define a function to smooth the images using SimpleITK")


def sitk_show(img, title=None, margin=0.05, dpi=40):
    nda = SimpleITK.GetArrayFromImage(img)
    spacing = img.GetSpacing()
    figsize = (1 + margin) * nda.shape[0] / \
        dpi, (1 + margin) * nda.shape[1] / dpi
    extent = (0, nda.shape[1]*spacing[1], nda.shape[0]*spacing[0], 0)
    fig = plt.figure(figsize=figsize, dpi=dpi)
    ax = fig.add_axes([margin, margin, 1 - 2*margin, 1 - 2*margin])

    plt.set_cmap("gray")
    ax.imshow(nda, extent=extent, interpolation=None)

    if title:
        plt.title(title)

    plt.show()


# %%
smooth_crop_images = {}
for key, value in crop_images.items():

    img = SimpleITK.GetImageFromArray(value)
    imgSmooth = SimpleITK.CurvatureFlow(image1=img,
                                        timeStep=0.125,
                                        numberOfIterations=25)
    smooth_crop_images[key] = imgSmooth
    sitk_show(imgSmooth, "Smoothing " + key)

# %%
print("Experimenting with segmentation using Connected Threshold without smoothed images")
lstSeeds = [(30, 30), (60, 100)]
for key, value in crop_images.items():
    # lstSeeds = [(30, 30)]

    img = SimpleITK.GetImageFromArray(value)
    imgGrayMatter = SimpleITK.ConnectedThreshold(image1=img,
                                                 seedList=lstSeeds,
                                                 lower=30,
                                                 upper=90,
                                                 replaceValue=1)

    imgSmoothInt = SimpleITK.Cast(SimpleITK.RescaleIntensity(
        imgSmooth), imgGrayMatter.GetPixelID())

    sitk_show(SimpleITK.LabelOverlay(imgSmoothInt,
                                     imgGrayMatter), "Segmentation of " + key)


# %%
print("Experimenting with segmentation using Connected Threshold and Smoothed images")
grayMatter_crop_images = {}
lstSeeds = [(30, 30), (60, 100)]
for key, value in smooth_crop_images.items():

    #img = SimpleITK.GetImageFromArray(value)
    imgGrayMatter = SimpleITK.ConnectedThreshold(image1=value,
                                                 seedList=lstSeeds,
                                                 lower=30,
                                                 upper=90,
                                                 replaceValue=1)

    imgSmoothInt = SimpleITK.Cast(SimpleITK.RescaleIntensity(
        imgSmooth), imgGrayMatter.GetPixelID())
    grayMatter_crop_images[key] = imgGrayMatter

    sitk_show(SimpleITK.LabelOverlay(imgSmoothInt,
                                     imgGrayMatter), "Segmentation of " + key)


# %%
print('Hole-filling of the segmented white matter')

for key, value in grayMatter_crop_images.items():
    imgGrayMatterNoHoles = SimpleITK.VotingBinaryHoleFilling(image1=value,
                                                             radius=[2]*3,
                                                             majorityThreshold=1,
                                                             backgroundValue=0,
                                                             foregroundValue=1)
    sitk_show(SimpleITK.LabelOverlay(imgSmoothInt,
                                     imgGrayMatterNoHoles), "Hole Filling of " + key)


# %%
print('Segmentation and hole-filling of grey matter')

#lstSeeds = [(60, 145), (75, 100), (10, 30), (75, 60)]
lstSeeds = [(75, 100)]
for key, value in smooth_crop_images.items():

    imgWhiteMatter = SimpleITK.ConnectedThreshold(image1=value,
                                                  seedList=lstSeeds,
                                                  lower=30,
                                                  upper=120,
                                                  replaceValue=2)

    imgWhiteMatterNoHoles = SimpleITK.VotingBinaryHoleFilling(image1=imgWhiteMatter,
                                                              radius=[2]*3,
                                                              majorityThreshold=1,
                                                              backgroundValue=0,
                                                              foregroundValue=2)  # labelWhiteMatter

    sitk_show(SimpleITK.LabelOverlay(imgSmoothInt,
                                     imgWhiteMatterNoHoles), "White of " + key)


# %%
