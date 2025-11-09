import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium 
dataset_path = r"C:\Users\Hero\Desktop\4 Kurs\IOT\2 praktika\Map-Crime_Incidents-Previous_Three_Months.csv"
SF= pd.read_csv(dataset_path)
print(SF.head(n=5))