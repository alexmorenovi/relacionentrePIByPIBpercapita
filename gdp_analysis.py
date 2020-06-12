import pandas as pd
import numpy as np
import matplotlib as plt

gdp = pd.read_csv("GDPG.csv")
per_c = pd.read_csv("GDPPCG.csv")
pop = pd.read_csv("GPG.csv")

mgdp = []
mper_c = []
mpog = []

m_match = []

desv = []

for i in range(1961,2019):
    mean1 = gdp[str(i)].mean()
    mean2 = per_c[str(i)].mean()
    mean3 = pop[str(i)].mean()
    mgdp.append(mean1)
    mper_c.append(mean2)
    mpog.append(mean3)
    count = 0

    for z in range(0,len(gdp[str(i)])+1):
        x = gdp[str(i)].isna()
        y = per_c[str(i)].isna()

    for w in range(len(x)):
        if x[w] != y[w]:
            count += 1

    m_match.append(count)
    
    desv1 = per_c[str(i)].std()
    desv.append(desv1)

print("Average GDP Growth:",mgdp)
print("Average GDP per Capita Growth:",mper_c)
#print("Missmatching:",m_match) # Is almost perfect

years = range(1961,2019)

x1 = np.array(mgdp)
x2 = np.array(mper_c)

diferencia = x1-x2

