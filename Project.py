# %% [markdown]
# # Final Project

# %%
# Loading libraries
from IPython import get_ipython
import pydicom
import SimpleITK
import os
import numpy
import matplotlib.pyplot as plt
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

sitk_show(imgOriginal)


# %%
imgSmooth = SimpleITK.CurvatureFlow(image1=imgOriginal,
                                    timeStep=0.125,
                                    numberOfIterations=5)


sitk_show(imgSmooth)
