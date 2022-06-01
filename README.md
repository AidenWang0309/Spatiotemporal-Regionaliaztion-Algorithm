# Spatiotemporal Regionaliaztion Algorithm

## Introduction

With the improvement of sensor network and human observation capabilities, a large amount of data with spatal and temporal attributes has been generated. Cluster analysis of spatiotemporal data is also a hot topic in recent years.

Therefore, we propose a regionalization-based clustering algorithm considering spatial and temporal contiguity (**STR method**). In addition, we also integrate it into a toolbox of ArcGIS Pro for users to use. 

## The framework of STR method

This figure illustrates the implementation of the spatiotemporal constraint regionalization algorithm, which contains three steps and one iteration rule namely **Search Neiborhood**, **Value Distance**, and **Neiborhoods Merage**.

![image](https://github.com/AidenWang0309/Spatiotemporal-Regionaliaztion-Algorithm/blob/main/ST-Method.png)

## Toolbox of ArcGIS Pro

The following figure is the interface of toolbox.

The ***Input cubes*** is input data, ***'Attributes'*** is the attributes users need, ***'Number of Spatiotemporal Domain'*** is the cluster number you want.

![image](https://github.com/AidenWang0309/Spatiotemporal-Regionaliaztion-Algorithm/blob/main/STR%20Toolbox.png)

## Regionalization results

The following figure is the regionalization result of **synthetic dataset** using STR method. *K represents the different clustering numbers*.

![image](https://github.com/AidenWang0309/Spatiotemporal-Regionaliaztion-Algorithm/blob/main/Synthetic%20Result1.png)

The following figure is the regionalization result of **real-world dataset** (Chinese air pollutant data in 2019) using STR method.

![image](https://github.com/AidenWang0309/Spatiotemporal-Regionaliaztion-Algorithm/blob/main/ClusterAll-1.png)
