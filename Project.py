# %% [markdown]
# # Final Project

# %%
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

from scipy import ndimage
import skimage.color as sc
import numpy as np


get_ipython().run_line_magic('pylab', 'inline')

PathDicom = "./DataP/"
lstFilesDCM = []  # create an empty list
for dirName, subdirList, fileList in os.walk(PathDicom):
    for filename in fileList:
        if ".dcm" in filename.lower():  # check whether the file is DICOM
            lstFilesDCM.append(os.path.join(dirName, filename))


# %%
patient = pydicom.read_file(lstFilesDCM[0])
print(patient.PatientPosition)
print(patient.StudyDate)
print(patient.Modality)

CalcPixelDims = (int(patient.Rows), int(patient.Columns), len(lstFilesDCM))
print(CalcPixelDims)

# %%
SpineImgArray = numpy.zeros(CalcPixelDims, dtype=patient.pixel_array.dtype)

for filenameDCM in lstFilesDCM:
    ds = pydicom.read_file(filenameDCM)
    SpineImgArray[:, :, lstFilesDCM.index(filenameDCM)] = ds.pixel_array


CalcPixelSpacing = (float(patient.PixelSpacing[0]), float(
    patient.PixelSpacing[1]), float(patient.SliceThickness))

x = numpy.arange(0.0, (CalcPixelDims[0]+1)
                 * CalcPixelSpacing[0], CalcPixelSpacing[0])
y = numpy.arange(0.0, (CalcPixelDims[1]+1)
                 * CalcPixelSpacing[1], CalcPixelSpacing[1])
z = numpy.arange(0.0, (CalcPixelDims[2]+1)
                 * CalcPixelSpacing[2], CalcPixelSpacing[2])


# %%
plt.figure(dpi=300)
plt.axes().set_aspect('equal', 'datalim')
plt.set_cmap(plt.gray())
plt.pcolormesh(x, y, numpy.flipud(SpineImgArray[:, :, 12]))


# %%
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


reader = SimpleITK.ImageSeriesReader()
filenamesDICOM = reader.GetGDCMSeriesFileNames(PathDicom)
reader.SetFileNames(filenamesDICOM)
img3DOriginal = reader.Execute()

imgOriginal = img3DOriginal[:, :, 8]

print(type(imgOriginal))
sitk_show(imgOriginal)
imgOriginal = sitk.ima

# %%
imgSmooth = SimpleITK.CurvatureFlow(image1=imgOriginal,
                                    timeStep=0.125,
                                    numberOfIterations=10)


sitk_show(imgSmooth)


# %%

lstSeeds = [(110, 85)]

imgWhiteMatter = SimpleITK.ConnectedThreshold(image1=imgSmooth,
                                              seedList=lstSeeds,
                                              lower=90,
                                              upper=400,
                                              replaceValue=1)


imgSmoothInt = SimpleITK.Cast(SimpleITK.RescaleIntensity(
    imgSmooth), imgWhiteMatter.GetPixelID())


sitk_show(SimpleITK.LabelOverlay(imgSmoothInt, imgWhiteMatter))

# %%

# %%
# Load the image from the source file
image_file = "DataP/T1_0005_D3.png"
image = sk_io.imread(image_file)

# Convert to grayscale so we only have one channel
bw_image = sk_col.rgb2gray(image)

# Find the mean threshold value
mean_val = threshold_mean(image)

# Threshold the image
binary_image = image > mean_val

# Plot the thresholded image
fig = plt.figure(figsize=(3, 3))
plt.imshow(binary_image, cmap="gray")
plt.title("Mean Threshold: " + str(mean_val))
plt.show()


# %%
fig, ax = try_all_threshold(image, figsize=(10, 10), verbose=False)
plt.show()


# %%
# Apply Minimum thresholding
min_val = threshold_minimum(bw_image)
binary_image_min = bw_image > min_val

# Apply Otsu thresholding
otsu_val = threshold_otsu(bw_image)
binary_image_otsu = bw_image > otsu_val

# Display the thresholded images
fig = plt.figure(figsize=(12, 12))

# Minimum
a = fig.add_subplot(1, 2, 1)
image_plot_1 = plt.imshow(binary_image_min, cmap="gray")
a.set_title("Min Threshold: " + str(min_val))

# Otsu
a = fig.add_subplot(1, 2, 2)
image_plot_2 = plt.imshow(binary_image_otsu, cmap="gray")
a.set_title("Otsu Threshold: " + str(otsu_val))

plt.show()


# %%
# Convert to grayscale so we only have one channel
box = (100, 120, 220, 270)

# image3 = Image.open(image_file).crop(box)
# image3 = array(image3, 'f')
bw_planes = sk_col.rgb2gray(image)
planes_otsu = threshold_otsu(image)
thresh_planes = bw_planes > planes_otsu

# Convert the thresholded image to its inverse
inverse_thresh = np.invert(thresh_planes)

fig = plt.figure(figsize=(6, 6))
plt.imshow(inverse_thresh, "gray")
plt.show()


# %%

# Contrast stretching
p2 = np.percentile(image, 2)
p98 = np.percentile(image, 98)
image_ct = exposure.rescale_intensity(image, in_range=(p2, p98))

# Histogram Equalization
image_eq = exposure.equalize_hist(image)

# Show the images
fig = plt.figure(figsize=(20, 12))

# Subplot for original image
a = fig.add_subplot(3, 3, 1)
imgplot = plt.imshow(image)
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
imgplot = plt.hist(image.ravel())

a = fig.add_subplot(3, 3, 5)
imgplot = plt.hist(image_ct.ravel())

a = fig.add_subplot(3, 3, 6)
imgplot = plt.hist(image_eq.ravel())

# Subplots for CDFs

a = fig.add_subplot(3, 3, 7)
imgplot = plt.hist(image.ravel(), bins=255, cumulative=True)

a = fig.add_subplot(3, 3, 8)
imgplot = plt.hist(image_ct.ravel(), bins=255, cumulative=True)

a = fig.add_subplot(3, 3, 9)
imgplot = plt.hist(image_eq.ravel(), bins=255, cumulative=True)

plt.show()


# %%

image2 = Image.open(image_file)

blurred_image = image2.filter(ImageFilter.BLUR)
sharpened_image = image2.filter(ImageFilter.SHARPEN)

# Display it
fig = plt.figure(figsize=(16, 12))

# Plot original image
a = fig.add_subplot(1, 3, 1)
image_plot_1 = plt.imshow(image2)
a.set_title("Original")

# Plot blurred image
a = fig.add_subplot(1, 3, 2)
image_plot_2 = plt.imshow(blurred_image)
a.set_title("Blurred")

# Plot sharpened image
a = fig.add_subplot(1, 3, 3)
image_plot_3 = plt.imshow(sharpened_image)
a.set_title("Sharpened")

plt.show()


# %%

my_kernel = (200, 50, -100,
             -50, 200, -50,
             -100, 50, 200)

filtered_image = image2.filter(ImageFilter.Kernel((3, 3), my_kernel))

# Display it
fig = plt.figure(figsize=(16, 12))

# Plot original image
a = fig.add_subplot(1, 2, 1)
image_plot_1 = plt.imshow(image2)
a.set_title("Original")

# Plot filtered image
a = fig.add_subplot(1, 2, 2)
image_plot_2 = plt.imshow(filtered_image)
a.set_title("Custom Filter")

plt.show()


# %%

edges_image = image2.filter(ImageFilter.FIND_EDGES)

# Display it
fig = plt.figure(figsize=(16, 12))

# Plot original image
a = fig.add_subplot(1, 2, 1)
image_plot_1 = plt.imshow(image2)
a.set_title("Original")

# Plot filtered image
a = fig.add_subplot(1, 2, 2)
image_plot_2 = plt.imshow(edges_image)
a.set_title("Edges")

plt.show()


# %%
def edge_sobel(image):
    image = sc.rgb2gray(image)  # Convert color image to gray scale
    dx = ndimage.sobel(image, 1)  # horizontal derivative
    dy = ndimage.sobel(image, 0)  # vertical derivative
    mag = np.hypot(dx, dy)  # magnitude
    mag *= 255.0 / np.amax(mag)  # normalize (Q&D)
    mag = mag.astype(np.uint8)
    return mag


sobel_image = edge_sobel(np.array(image2))

# Display it
fig = plt.figure(figsize=(16, 12))

# Plot original image
a = fig.add_subplot(1, 3, 1)
image_plot_1 = plt.imshow(image2)
a.set_title("Original")

# Plot PIL FIND_EDGES image
a = fig.add_subplot(1, 3, 2)
image_plot_2 = plt.imshow(edges_image)
a.set_title("Edges")

# Plot Sobel image
a = fig.add_subplot(1, 3, 3)
# Need to use a gray color map as we converted this to a grayscale image
image_plot_2 = plt.imshow(sobel_image, cmap="gray")
a.set_title("Sobel")

plt.show()


# %%
