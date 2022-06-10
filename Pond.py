import numpy as np
import pandas as pd


alt = np.loadtxt('river.alt')
Alt_out=[]
p=input('Floating mean smoothing of the profile. Indicate size of mobile window: ')
p=int(p)

for index in range(0, p):
	Alt_out.append('Nan')
	
for index in range(p, len(alt)-p):
    average = np.mean(alt[index-p : index+p+1])
    Alt_out.append(average)
    
for index in range(len(alt)-p, len(alt)):
	Alt_out.append('Nan')

df=pd.DataFrame(Alt_out)
df.to_csv('moy_alt.dat', index=False)
