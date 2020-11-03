# This code is for generating NDSI map from Landsat data

from osgeo import gdal

ds = gdal.Open('/this/is/your/path/to/Landsat.tif', gdal.GA_ReadOnly)
rb = ds.GetRasterBand(1)
img_array = rb.ReadAsArray()


