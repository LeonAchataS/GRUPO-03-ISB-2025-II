# Laboratorio 3 lectura de EMG con Bitalino

## Tabla de Contenido
- [Introducción](#introducción)
- [Objetivos](#objetivos)
- [Materiales](#materiales)
- [Ploteo en Python](#ploteo-en-python)
- [Resultados](#resultados)
- [Bibliografía](#bibliografía)

## Introducción
##### Cada que se desea mover un músculo se realiza la contracción y relajación de las fibras de miosina mediante la producción de potenciales de acción. Estos en sí estan mediados por la variación de potencial eléctrico a lo largo de la membrana celular debido al intercambio iónico:
<div align="center">
  
![Potencia de Acción](https://www.itaca.edu.es/IMAGENES/INFORMACION%20ESPECIALISTAS/potencial-accion-3-19.gif)

</div>

##### Esta variación de voltaje (señal) puede ser captado y posteriormente medido por dispositivos como lo es Bitalino. La señal oscila entre los 20 Hz a 500 Hz por lo que para poder muestrearla sin que pierda su forma, se tiene que elegir una frequencia de muestreo de al menos 1 kHz. Valor indicado por el teorema de Nyquist en la que se indica que la señal de muestreo debe ser como mínimo el doble de la máxima frequencia de la señal original.

## Objetivos:
#### - Adquirir y procesar señales EMG
#### - Realizar una correcta configuración del Bitalino
#### - Explicar el por qué de las variaciones en las señales captadas en los distintos estados

## Materiales
#### - Bitalino
#### - Laptop o PC con conexión Bluetooth y el programa OpenSignals instalado
#### - 3 electrodos húmedos
#### - Cámara

## Ploteo en Python
  
Para el ploteo y análisis de las señales EMG se utilizó Python debido a que ofrece librerías especializadas como NumPy, SciPy, Pandas y Matplotlib, que permiten procesar datos biomédicos de forma eficiente y visualizarlos claramente. El código usado es el siguiente: <br>
[Código en Python para el ploteo](/Laboratorios/Laboratorio%203%20-%20EMG%20Bitalino/Ploteo%20Python.ipynb)

En primer lugar, se cargaron los archivos de texto correspondientes a cada músculo (trapecio, antebrazo y bíceps) y se extrajo la señal cruda para graficarla en el dominio del tiempo. Posteriormente, se aplicó la Transformada Rápida de Fourier (FFT) con el fin de observar las componentes de frecuencia que conforman la señal, identificando los rangos de mayor energía muscular. Finalmente, se empleó el método de Welch para obtener la densidad espectral de potencia (PSD), una técnica que mejora la interpretación de la señal al reducir el ruido y suavizar el espectro. Con este procedimiento se logró representar y comparar la actividad muscular en distintas regiones, facilitando el análisis de sus características espectrales.

Para el análisis de las señales EMG se utilizaron dos enfoques en el dominio de la frecuencia: la Transformada Rápida de Fourier (FFT) y el método de Welch. La FFT se eligió porque permite obtener de manera directa y eficiente el espectro de frecuencias de la señal, mostrando la distribución de energía en los distintos componentes armónicos. Esto es útil para identificar picos asociados al ruido eléctrico (como el de 60 Hz) y al mismo tiempo visualizar el rango de frecuencias característico de la actividad muscular (generalmente entre 20 y 450 Hz).

Sin embargo, la FFT puede mostrar un espectro ruidoso debido a la naturaleza no estacionaria de la señal EMG. Por ello, se complementó con el método de Welch, que divide la señal en segmentos, aplica ventanas y promedia los espectros parciales, reduciendo la varianza y obteniendo una estimación más suave y confiable de la densidad espectral de potencia. Esta combinación permite no solo detectar la presencia de frecuencias dominantes, sino también tener una representación más clara y estable del contenido espectral de la señal muscular. 

Por cada músculo se realizó 3 pruebas:

 + Reposo (basal)
 + Movimiento libre
 + Movimiento limitado 

## Resultados

### Antebrazos:
<div align="center">
  
| **Antebrazo en reposo** | **Antebrazo sin oposición** | **Antebrazo con oposición** |
|---------------------|-------------------------|-------------------------|
| <a href="https://www.youtube.com/watch?v=F46p1PJufy0"><img src="https://img.youtube.com/vi/F46p1PJufy0/0.jpg" width="250" height="140"></a> | <a href="https://www.youtube.com/watch?v=cBVej_iqN20"><img src="https://img.youtube.com/vi/cBVej_iqN20/0.jpg" width="250" height="140"></a> | <a href="https://www.youtube.com/watch?v=O7S6IrTmvPA"><img src="https://img.youtube.com/vi/O7S6IrTmvPA/0.jpg" width="250" height="140"></a> |

### Plots EMG antebrazo basal
![Plots EMG antebrazo basal](/Otros/AntebrazoBasal.png)

### Plots EMG Antebrazo en movimiento libre
![Plots EMG Antebrazo en movimiento libre](/Otros/AntebrazoLibre.png)

### Plots EMG Antebrazo en movimiento limitado
![Plots EMG Antebrazo en movimiento limitado](/Otros/AntebrazoLimitado.png)

</div>

##### La señal EMG de superficie se obtiene mediante electrodos colocados sobre el músculo del antebrazo; en reposo, la actividad eléctrica es casi nula, lo que genera una señal muy plana [1]. Al movilizar sin resistencia, solo se reclutan unas pocas unidades motoras, lo que se traduce en una amplitud baja y un patrón irregular. Cuando se aplica oposición o resistencia, se incrementa tanto el reclutamiento de unidades motoras como la frecuencia de descarga, provocando una señal de mayor amplitud y con distribución más densa, lo que refleja un incremento en la fuerza requerida [2], [3].

### Biceps:
<div align="center">

|  **Bisceps en reposo**  | **Bisceps sin oposición** | **Bisceps con oposición** |
|:------------:|:---------------:|:------------:|
| <a href="https://www.youtube.com/watch?v=VZrON9HyObU"><img src="https://img.youtube.com/vi/VZrON9HyObU/0.jpg" width="250" height="140"></a> | <a href="https://www.youtube.com/watch?v=jC3mxfnijYQ"><img src="https://img.youtube.com/vi/jC3mxfnijYQ/0.jpg" width="250" height="140"></a> | <a href="https://www.youtube.com/watch?v=hM2iXm7oM7Q"><img src="https://img.youtube.com/vi/hM2iXm7oM7Q/0.jpg" width="250" height="140"></a> |


### Plots EMG bíceps basal
![Plots EMG bíceps basal](/Otros/BicepBasal.png)

### Plots EMG Antebrazo en movimiento libre
![Plots EMG Bíceps en movimiento libre](/Otros/BicepLibre.png)

### Plots EMG Antebrazo en movimiento limitado
![Plots EMG Bíceps en movimiento limitado](/Otros/BicepLimitado.png)

</div>

##### La señal EMG de superficie del bíceps braquial se registra mediante electrodos en la piel sobre el músculo, y su amplitud está directamente relacionada con la fuerza ejercida y el reclutamiento de unidades motoras. Cuando el músculo está en reposo, la actividad es prácticamente cero, resultando en una señal casi plana. Al contraer sin resistencia, se activan solo algunas unidades motoras, generando una señal de baja amplitud. En cambio, al realizar contracciones con oposición o mayor carga, tanto el reclutamiento de unidades motoras como la frecuencia de descarga aumentan, lo que se refleja en una señal EMG de mayor amplitud y mayor densidad [4], [5]. Además, la ubicación de los electrodos es clave: colocarlos sobre el vientre muscular produce una relación más lineal entre amplitud EMG y fuerza, con menor variabilidad que otras ubicaciones [6]. En resumen, el EMG superficial del bíceps permite observar cómo varía la activación muscular según la demanda de fuerza y la técnica de registro.

### Trapecio:
<div align="center">

|  **Trapecio en reposo**  | **Trapecio sin oposición** | **Trapecio con oposición** |
|:------------:|:---------------:|:------------:|
| <a href="https://www.youtube.com/watch?v=s1ZrVtxSbU4"><img src="https://img.youtube.com/vi/s1ZrVtxSbU4/0.jpg" width="250" height="140"></a> | <a href="https://www.youtube.com/watch?v=bVA3Ll9P19Q"><img src="https://img.youtube.com/vi/bVA3Ll9P19Q/0.jpg" width="250" height="140"></a> | <a href="https://www.youtube.com/watch?v=Q7mYDY2JNNM"><img src="https://img.youtube.com/vi/Q7mYDY2JNNM/0.jpg" width="250" height="140"></a> |


### Plots EMG trapecio basal
![Plots EMG trapecio basal](/Otros/TrapecioBasal.png)

### Plots EMG trapecio en movimiento libre
![Plots EMG trapecio en movimiento libre](/Otros/TrapecioLibre.png)

### Plots EMG trapecio en movimiento limitado
![Plots EMG trapecio en movimiento limitado](/Otros/TrapecioLimitado.png)

</div>

##### La señal EMG superficial en el trapecio superior refleja la variación de la actividad muscular según el nivel de contracción. En reposo, la señal es casi plana porque no hay activación significativa. Cuando el hombro se eleva sin resistencia, se activan pocas unidades motoras, lo que produce un registro de baja amplitud e irregularidad. En cambio, al mantener o elevar el hombro contra resistencia, el reclutamiento de fibras aumenta junto con la frecuencia de descarga, lo que se traduce en una señal de mayor amplitud y un patrón más denso [7].

De cada prueba con los datos recopilados se puede concluir que:

 + Plot Basal<br>
   En la señal temporal se observa una actividad casi constante con pocas variaciones, lo que refleja el estado de reposo muscular. En el espectro FFT aparecen picos aislados asociados principalmente a ruido de red eléctrica (60 Hz) y armónicos, mientras que la mayor parte de la energía es baja. En el método de Welch, la densidad espectral de potencia confirma que la señal se mantiene estable con picos definidos en frecuencias específicas, típicos de ruido más que de contracción muscular.

 + Movimiento libre<br>
   En la señal temporal se aprecian contracciones claras, repetitivas y de mayor amplitud, lo que indica un mayor reclutamiento de fibras musculares durante el movimiento voluntario. En el FFT, la energía se distribuye en un rango más amplio de frecuencias (principalmente entre 50 y 150 Hz), lo cual es característico de la activación muscular real. El Welch suaviza la señal espectral y muestra un pico predominante en bajas frecuencias, junto con una pendiente descendente, típico de una contracción dinámica con alta variabilidad.
   
 + Movimiento limitado<br>
  En la señal temporal se distinguen contracciones menos regulares pero con amplitudes elevadas en ciertos momentos, reflejando un esfuerzo parcial o con restricción. En el FFT, la energía sigue distribuida en un rango amplio pero con menor intensidad que en el movimiento libre. El análisis de Welch muestra un pico más pronunciado alrededor de los 50 Hz, pero con menor dispersión en altas frecuencias, lo que sugiere una activación muscular más controlada o forzada. 


## Bibliografía:
#### [1] Akira Furui, H. Hayashi, and T. Tsuji, “A Scale Mixture-Based Stochastic Model of Surface EMG Signals With Variable Variances,” IEEE Transactions on Biomedical Engineering, vol. 66, no. 10, pp. 2780–2788, Jan. 2019, doi: https://doi.org/10.1109/tbme.2019.2895683.
#### [2] I. Campanini, C. Disselhorst-Klug, W. Z. Rymer, and R. Merletti, “Surface EMG in Clinical Assessment and Neurorehabilitation: Barriers Limiting Its Use,” Frontiers in Neurology, vol. 11, no. 934, Sep. 2020, doi: https://doi.org/10.3389/fneur.2020.00934.
#### [3] F. Felici and A. Del Vecchio, “Surface Electromyography: What Limits Its Use in Exercise and Sport Physiology?,” Frontiers in Neurology, vol. 11, no. 11, Nov. 2020, doi: https://doi.org/10.3389/fneur.2020.578504.
#### [4] Z. A. Riley, A. H. Maerz, J. C. Litsey, and R. M. Enoka, “Motor unit recruitment in human biceps brachii during sustained voluntary contractions,” The Journal of physiology, vol. 586, no. 8, pp. 2183–93, 2008, doi: https://doi.org/10.1113/jphysiol.2008.150698.
#### [5] D. Borzelli, M. Gazzoni, A. Botter, L. Gastaldi, A. d’Avella, and T. M. Vieira, “Contraction level, but not force direction or wrist position, affects the spatial distribution of motor unit recruitment in the biceps brachii muscle,” European Journal of Applied Physiology, vol. 120, no. 4, pp. 853–860, Feb. 2020, doi: https://doi.org/10.1007/s00421-020-04324-6.
#### [6] N. U. Ahamed, K. Sundaraj, M. Alqahtani, O. Altwijri, Md. A. Ali, and Md. A. Islam, “EMG-force relationship during static contraction: Effects on sensor placement locations on biceps brachii muscle,” Technology and Health Care, vol. 22, no. 4, pp. 505–513, Aug. 2014, doi: https://doi.org/10.3233/thc-140842.
#### [7] I. Javed et al., “Electromyographic analysis of bilateral upper trapezius muscles at different levels of work-pace among sewing machine operators,” BMC Musculoskeletal Disorders, vol. 25, no. 1, Oct. 2024, doi: https://doi.org/10.1186/s12891-024-07874-4.

### Contribución:
##### - Leon Achata 33.33%
##### - Nicolas Arango 33.33%
##### - Hans Navarro 33.33%
