from gdp_analysis import *
import matplotlib.pyplot as plt


plt.title("Crecimiento del PIB (%)")
plt.plot(years, mgdp, color='r')
plt.show()

plt.title("Crecimiento del PIB per cápita (%)")
plt.plot(years, mper_c)
plt.show()

plt.title("Comparación")
plt.plot(years,mper_c)
plt.plot(years,mgdp, color = 'r')
plt.show()

plt.title("Diferencia")
plt.plot(years,diferencia)
plt.show()

plt.title("Crecimiento Poblacional")
plt.plot(years,mpog,color = 'g')
plt.show()

plt.title("Población vs Diferencia de tasas")
plt.plot(years,diferencia)
plt.plot(years,mpog, color = 'g')
plt.show()

plt.title("Desviación Estandar")
plt.plot(years, desv)
plt.show()

#desv = pd.DataFrame([desv])

#desv.to_csv(r'C:\Users\LENOVO\OneDrive\Documentos\Tec\Segundo Semestre\Economía\resultados.csv', index=False, header=True)

