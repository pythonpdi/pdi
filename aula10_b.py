# -*- coding: utf-8 -*-
"""Aula10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15Tmw9h9NuyJm8p1-lJuI4UiLyrrXrqn7
"""

!pip install gdal
!pip install rasterio

!pip install spectral

"""**TIFFFILE**"""

# Bibliotecas
import tifffile as tif
import matplotlib.pyplot as plt
from spectral import imshow

# Leitura de imagem
img = tif.imread('/content/L71221071_07120010720_DN.tif')

# Verificando dimensões
img.shape

# Visualizando
plt.imshow(img[:,:,3], cmap='Greys_r')

imshow(img, bands=(2,3,0))

"""**GDAL**"""

from osgeo import gdal
import numpy as np

img2 = gdal.Open('/content/L71221071_07120010720_DN.tif')

img3 = img2.ReadAsArray()

img3.shape

img3 = img3.swapaxes(0,1)

img3.shape

imshow(img3, (2,3,1))

b1 = img2.GetRasterBand(1).ReadAsArray()
b2 = img2.GetRasterBand(2).ReadAsArray()
b4 = img2.GetRasterBand(4).ReadAsArray()

stack = np.dstack([b1,b2,b4])

stack.shape

imshow(stack, (1,2,0))

"""**Rasterio**"""

import rasterio
from  rasterio.plot import show

rst = rasterio.open('/content/L71221071_07120010720_DN.tif')

print(rst)

show(rst, cmap='Greys_r')

b1 = rst.read(1)
b2 = rst.read(2)
b4 = rst.read(4)

stack = np.dstack([b1,b2,b4])

with rasterio.open('/content/L71221071_07120010720_DN.tif') as rst:
  b1 = rst.read(1)
  b2 = rst.read(2)
  b4 = rst.read(4)

stack2 = np.dstack([b1,b2,b4])

imshow(stack2, (1,2,0))

