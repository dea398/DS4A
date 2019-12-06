#%% [markdown]
# # Final Project

#%%
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
        if ".ima" in filename.lower():  # check whether the file is DICOM
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
