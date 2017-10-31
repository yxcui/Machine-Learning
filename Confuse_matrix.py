# -*- coding: cp936 -*-
import arcpy
from arcpy.sa import *
import numpy as np

#���ȷ�������
def accuracy_analysis(test_samples,classified_image): 
    confuse = {}
    for i in range(1,7):
        for j in range(1,7):
            confuse[i,j] = 0

    #�ӷ�����ͼ������ȡ��֤�������Ӧ�ķ���ֵ�������µ���֤�������ļ�
    outPointFeatures = arcpy.CreateUniqueName("c:\\data\\tmp\\xx.shp")
    ExtractValuesToPoints(test_samples,classified_image,outPointFeatures)

    #������������
    cur = arcpy.SearchCursor(outPointFeatures)
    n = 0
    for row in cur:
        n = n + 1
        i = row.GrndTruth
        j = row.RASTERVALU
        confuse[i,j] = confuse[i,j] + 1
    del outPointFeatures

    #���ݻ��������������ܾ��Ⱥ�Kappaϵ��
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

#���ͳ��
def area_stat(classifiedraster):
    #RasterתNumPyArray��6��ʾ��ֵת�����ֵ 
    R_Array = arcpy.RasterToNumPyArray (classifiedraster, "", "", "", 6)
    #��άչƽΪһά
    stat = np.bincount(R_Array.flatten())
    #stat��һ���б��б��е�ÿ��Ԫ�ؼ�¼��Ӧ���͵���Ԫ��
    sum_pixel = stat[0]+stat[1]+stat[2]+stat[3]+stat[4]+stat[5]
    message = "ũҵ�õأ�%f���ֵأ�%f�����ֲݵأ�%f������أ�%f��ˮ��%f����أ�%f"%(
                float(stat[0])/float(sum_pixel),float(stat[1])/float(sum_pixel),
                float(stat[2])/float(sum_pixel),float(stat[3])/float(sum_pixel),
                float(stat[4])/float(sum_pixel),float(stat[5])/float(sum_pixel))
    arcpy.AddMessage (message)

#����������������ݺͷ�����ͼ�����ݣ������þ��ȷ�������
test_samples = "c:\\�о���\\ŷ��\\test_samples.shp"
classified_image = "c:\\�о���\\ŷ��\\result\\svm2016.img"
accuracy_analysis(test_samples,classified_image)
##classified_raster = Raster("c:\\�о���\\ŷ��\\tmp\\image1.img")
##area_stat(classified_raster)
    
