#%%
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

years = range(2000, 2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]
plt.figure(figsize=(12, 6))
matplotlib.rcParams['font.size'] = 20
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000001'
sns.set_style("darkgrid")
fmt = 's-b'
plt.plot(years, apples, fmt);
plt.plot(years, oranges, 'o--r');
plt.xlabel('Año')
plt.ylabel('Rendimiento (toneladas por hectárea)');
plt.title("Rendimiento de los campos en Baja California")
plt.legend(['Manzanas', 'Naranjas'])

plt.show()
#%%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load data into a Pandas dataframe
flowers_df = sns.load_dataset("iris")
print (flowers_df)
print (flowers_df.species.unique())

plt.figure(figsize=(12, 6))
plt.title('Dimensiones de Sepalo')
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', s=100, data=flowers_df);

plt.figure(figsize=(12, 6))
plt.title('Dimensiones de Sepalo')
plt.hist(flowers_df.sepal_width);

plt.figure(figsize=(12, 6))
plt.title('Dimensiones de Sepalo')
plt.hist(flowers_df.sepal_width, bins=3);

plt.figure(figsize=(12, 6))
plt.title('Dimensiones de Sepalo')
plt.hist(flowers_df.sepal_width, bins=np.arange(2, 6, 0.25));

plt.figure(figsize=(12, 6))
plt.title('Dimensiones de Sepalo')
plt.hist(flowers_df.sepal_width, bins=[1, 3, 4, 4.5]);

plt.figure(figsize=(12, 6))
plt.title('Dimensiones de Sepalo')
setosa_df = flowers_df[flowers_df.species == 'setosa']
versicolor_df = flowers_df[flowers_df.species == 'versicolor']
virginica_df = flowers_df[flowers_df.species == 'virginica']
plt.hist(setosa_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25));
plt.hist(versicolor_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25));
plt.hist(virginica_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25));

plt.figure(figsize=(12, 6))
plt.title('Dimensiones de Sepalo')
setosa_df = flowers_df[flowers_df.species == 'setosa']
versicolor_df = flowers_df[flowers_df.species == 'versicolor']
virginica_df = flowers_df[flowers_df.species == 'virginica']
plt.hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width],
  bins=np.arange(2, 5, 0.25),
  stacked=True);

plt.legend(['Setosa', 'Versicolor', 'Virginica']);
#%%
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

years = range(2000, 2006)
apples = [0.35, 0.6, 0.9, 0.8, 0.65, 0.8]
oranges = [0.4, 0.8, 0.9, 0.7, 0.6, 0.8]
plt.figure(figsize=(12, 6))
matplotlib.rcParams['font.size'] = 20
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'
sns.set_style("darkgrid")
plt.bar(years, oranges);
plt.bar(years, oranges, bottom=apples);
plt.xlabel('Año')
plt.ylabel('Rendimiento (toneladas por hectárea)');
plt.title("Rendimiento de los campos en Baja California")
plt.legend(['Manzanas', 'Naranjas'])
#%%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
tips_df = sns.load_dataset("tips");
print(tips_df)

sns.barplot(x='day', y='total_bill', data=tips_df);
#%%
sns.barplot(x='day', y='total_bill', hue='sex', data=tips_df);
#%%
sns.barplot(x='total_bill', y='day', hue='sex', data=tips_df);
#%%
# Chart title
plt.title("Daily Total Bill")
# Draw a nested boxplot to show bills by day and time
sns.boxplot(x=tips_df.day,

y=tips_df.total_bill,
hue=tips_df.smoker);
#%%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
flights_df = sns.load_dataset("flights").pivot(index="month", columns="year", values="passengers")
print(flights_df)

flights_df = sns.load_dataset("flights").pivot(index="month", columns="year", values="passengers")
print(flights_df)
plt.title("Número de pasajeros (1000s)")
sns.heatmap(flights_df);

#%%
flights_df = sns.load_dataset("flights").pivot(index="month", columns="year", values="passengers")
plt.title("Número de pasajeros (1000s)")
sns.heatmap(flights_df, fmt="d", annot=True, cmap='Blues');

#%%
flowers_df = sns.load_dataset("iris")
plt.figure(figsize=(12, 6))
plt.title('Flores')
sns.kdeplot(x=flowers_df.sepal_length,
  y=flowers_df.sepal_width,
  shade=True,
  shade_lowest=False);

#%%
flowers_df = sns.load_dataset("iris")
plt.figure(figsize=(12, 6))
plt.title('Flores')
setosa = flowers_df[flowers_df.species ==
'setosa']
virginica = flowers_df[flowers_df.species ==
'virginica']
plt.title("Flowers (Setosa & Virginica)")
sns.kdeplot(x=setosa.sepal_length,
  y=setosa.sepal_width,
  shade=True, cmap='Reds',
  shade_lowest=False)

sns.kdeplot(x=virginica.sepal_length,
  y=virginica.sepal_width,
  shade=True, cmap='Blues',
  shade_lowest=False);
#%%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image
img = Image.open('grafica.jpg')
img_array = np.array(img)
plt.imshow(img);
#%%
img = Image.open('grafica.jpg')
img_array = np.array(img)
plt.grid(False)
plt.title('A data science meme')
plt.axis('off')
plt.imshow(img_array[125:325,105:305]);
#%%
import matplotlib.pyplot as plt       #Importar la libreria matplotlib para crear gráficas 
import seaborn as sns                 #Importa la libreria seaborn para crear gráficas estadísticos 
import numpy as np                    #Importa la libreria numpy para realizar calculos numéricos 

# Crear la figura con 2*3 como ejes
fig, axes = plt.subplots(2, 3, figsize=(16, 8))

#Producción de manzanas y naranjas (graficá de líneas)
axes[0,0].plot(years, apples, 's-b')      #Grafica la producción de manzanas por años 
axes[0,0].plot(years, oranges, 'o--r')    #Grafica la producción de naranjas por años
axes[0,0].set_xlabel('Año')       #Etiqueta para el eje x 
axes[0,0].set_ylabel('Producción (toneladas por hectárea)')   #Etiqueta del eje y
axes[0,0].legend(['Manzanas', 'Naranjas'])        #Agregar una leyenda para identificar cual es naranjas y cual es manzanas 
axes[0,0].set_title('Producción de Cultivos en Kanto')    #Agregar título de la gráfica 

# Longitud vs. Anchura del sépalo (gráfica de disperción)
axes[0,1].set_title('Longitud vs. Anchura del Sépalo')      #Agregar título a la gráfica 
sns.scatterplot(x=flowers_df.sepal_length,
                y=flowers_df.sepal_width,
                hue=flowers_df.species,
                s=100,
                ax=axes[0,1])         # Dibuja un gráfico de dispersión de la longitud vs. anchura del sépalo
axes[0,1].set_xlabel('Longitud del Sépalo')     #Etiqueta de eje x
axes[0,1].set_ylabel('Anchura del Sépalo')      #Etiqueta de eje y

#Distribución de la Anchura del Sépalo (histograma)
axes[0,2].set_title('Distribución de la Anchura del Sépalo')    #Título de la gráfica 
axes[0,2].set_xlabel('Anchura del Sépalo')      #Etiqueta del eje x
axes[0,2].set_ylabel('Frecuencia')              #Etiqueta de eje y 
axes[0,2].hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width],
               bins=np.arange(2, 5, 0.25),
               stacked=True)          #Crear un histograma de la anchura del sépalo para tres especies  
axes[0,2].legend(['Setosa', 'Versicolor', 'Virginica'])   #Etiqueta para identificar las especies 

#Cuentas de restaurantes (gráfico de barras)
axes[1,0].set_title('Cuentas de Restaurantes')    #Título del gráfico
sns.barplot(x='day', y='total_bill', hue='sex', data=tips_df, ax=axes[1,0])     #Crea un gráfico de barras de las cuentas por día y sexo 
axes[1,0].set_xlabel('Día')       #Etiqueta del eje x
axes[1,0].set_ylabel('Factura Total')     #Etiqueta del eje y 

#Tráfico aéreo (mapa de calor)
axes[1,1].set_title('Tráfico Aéreo')      #Título del mapa 
sns.heatmap(flights_df, cmap='Blues', ax=axes[1,1])   #Crear un  mapa de calor del tráfico aereo en color azul
axes[1,1].set_xlabel('Mes')   #Etiqueta del eje x
axes[1,1].set_ylabel('Año')   #Etiqueta del eje y 

#Ciencia de Datos (Imagen)
axes[1,2].set_title('Ciencia de Datos')   #Título del gráfico
axes[1,2].imshow(img)     #Mostar imagen
axes[1,2].grid(False)     #Desacivar cuadrícula de la imagen 
axes[1,2].set_xticks([])    #Eliminar marcas del eje x
axes[1,2].set_yticks([])    #Eliminar marcas de eje y 

# Ajustar el diseño de la figura
plt.tight_layout(pad=2)
