# -*- coding: cp936 -*-
import arcpy
from arcpy.sa import *
import numpy as np

#精度分析工具
def accuracy_analysis(test_samples,classified_image): 
    confuse = {}
    for i in range(1,7):
        for j in range(1,7):
            confuse[i,j] = 0

    #从分类结果图像中提取验证样本点对应的分类值，产生新的验证样本点文件
    outPointFeatures = arcpy.CreateUniqueName("c:\\data\\tmp\\xx.shp")
    ExtractValuesToPoints(test_samples,classified_image,outPointFeatures)

    #产生混淆矩阵
    cur = arcpy.SearchCursor(outPointFeatures)
    n = 0
    for row in cur:
        n = n + 1
        i = row.GrndTruth
        j = row.RASTERVALU
        confuse[i,j] = confuse[i,j] + 1
    del outPointFeatures

    #根据混淆矩阵计算分类总精度和Kappa系数
    right_n = 0
    row_column = 0
    for k in range(1,7):
        right_n = right_n + confuse[k,k]
        row = 0
        for r in range(1,7):
            row = confuse[k,r] +row
        column = 0
        for c in range(1,7):
            column = confuse[c,k] +column
        row_column = row*column + row_column
    overall_precise = float(right_n)/float(n)
    Kappa = float(n*right_n - row_column)/float(n*n - row_column)
    print "n:",n
    print "overall_precise:",overall_precise
    print "Kappa:",Kappa

#面积统计
def area_stat(classifiedraster):
    #Raster转NumPyArray，6表示空值转换后的值 
    R_Array = arcpy.RasterToNumPyArray (classifiedraster, "", "", "", 6)
    #二维展平为一维
    stat = np.bincount(R_Array.flatten())
    #stat是一个列表，列表中的每个元素记录对应类型的像元数
    sum_pixel = stat[0]+stat[1]+stat[2]+stat[3]+stat[4]+stat[5]
    message = "农业用地：%f，林地：%f，疏林草地：%f，居民地：%f，水域：%f，裸地：%f"%(
                float(stat[0])/float(sum_pixel),float(stat[1])/float(sum_pixel),
                float(stat[2])/float(sum_pixel),float(stat[3])/float(sum_pixel),
                float(stat[4])/float(sum_pixel),float(stat[5])/float(sum_pixel))
    arcpy.AddMessage (message)

#定义检验样本点数据和分类结果图像数据，并调用精度分析函数
test_samples = "c:\\研究生\\欧阳\\test_samples.shp"
classified_image = "c:\\研究生\\欧阳\\result\\svm2016.img"
accuracy_analysis(test_samples,classified_image)
##classified_raster = Raster("c:\\研究生\\欧阳\\tmp\\image1.img")
##area_stat(classified_raster)
    
