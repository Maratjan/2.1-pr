import numpy as np  #импорт бибилотеки numpy с последующим обращением как np
import pandas as pd
import matplotlib.pyplot as plt
import folium 
dataset_path = r"C:\Users\Hero\Desktop\2.1 pr\Map-Crime_Incidents-Previous_Three_Months.csv" # определение пути к файлу с данными 
SF= pd.read_csv(dataset_path) # определение кадра данных, взятых из csv файла
pd.set_option('display.max_rows', 6) #задание настройки пандасу, чтобы в кадре максимум показывалось 6 строк
pd.set_option('display.max_columns', 5) #задание настройки пандасу, чтобы в кадре максимум показывалось 6 строк
SF['Month'] = pd.to_datetime(SF['Date']).dt.month
SF['Day'] = pd.to_datetime(SF['Date']).dt.day
print(len(SF.columns)) # количество переменных в кадре 
print(len(SF)) # количество строк в кадре 
print(SF)