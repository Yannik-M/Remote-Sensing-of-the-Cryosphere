"""
This is a Python script to read Landsat and Sentinel satellite scenes
"""
import numpy as np

import matplotlib.pyplot as plt

import gdal

ds = gdal.Open(r'/this/is/your/path/to/Landsat.tif')

data = ds.ReadAsArray()
gt = ds.GetGeoTransform()
proj = ds.GetProjection()

ds = none
