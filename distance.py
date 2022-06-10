#PROFILS TOPO

import numpy as np
import math
import pandas as pd

# CALCUL DE LA DISTANCE ENTRE LES POINTS DU PROFIL AVEC LA FORMULE DE HAVERSINE

results = []
dist = []

positions = np.loadtxt('river.dat')
totaldistance = 0

for i in range(1, len(positions)):
    loc1 = positions[i - 1]
    loc2 = positions[i]
    
# Attention les fichiers GMT sont écris sous la forme Long / Lat
    lat1 = loc1[1]
    lng1 = loc1[0]

    lat2 = loc2[1]
    lng2 = loc2[0]

    degreesToRadians = (math.pi / 180)
    latrad1 = lat1 * degreesToRadians
    latrad2 = lat2 * degreesToRadians
    dlat = (lat2 - lat1) * degreesToRadians
    dlng = (lng2 - lng1) * degreesToRadians

    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(latrad1) * \
    math.cos(latrad2) * math.sin(dlng / 2) * math.sin(dlng / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    r = 6371009  # Rayon moyen de la Terre

    results.append(r * c) # Ajouter la nouvelle distance à la liste

    totaldistance = totaldistance + (c * r)
    dist.append(totaldistance)
    
df = pd.DataFrame(dist)
df.to_csv('river.dis', index=False) # Enregistre les distances totales dans le fichier "cubangototaldist.dis"


TotDist = (sum(results) / 1000)  # Conversion de m en km
print('La longueur totale du segment de rivière est de: ',TotDist, 'km')