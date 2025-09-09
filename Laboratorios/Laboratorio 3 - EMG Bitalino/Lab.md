# Laboratorio 3 lectura de EMG con Bitalino
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

## Resultados

### Ploteo en Python

Para el análisis de las señales EMG se utilizaron dos enfoques en el dominio de la frecuencia: la Transformada Rápida de Fourier (FFT) y el método de Welch. La FFT se eligió porque permite obtener de manera directa y eficiente el espectro de frecuencias de la señal, mostrando la distribución de energía en los distintos componentes armónicos. Esto es útil para identificar picos asociados al ruido eléctrico (como el de 60 Hz) y al mismo tiempo visualizar el rango de frecuencias característico de la actividad muscular (generalmente entre 20 y 450 Hz).

Sin embargo, la FFT puede mostrar un espectro ruidoso debido a la naturaleza no estacionaria de la señal EMG. Por ello, se complementó con el método de Welch, que divide la señal en segmentos, aplica ventanas y promedia los espectros parciales, reduciendo la varianza y obteniendo una estimación más suave y confiable de la densidad espectral de potencia. Esta combinación permite no solo detectar la presencia de frecuencias dominantes, sino también tener una representación más clara y estable del contenido espectral de la señal muscular. 

Por cada músculo se realizó 3 pruebas:

 + Reposo (basal)
 + Movimiento libre
 + Movimiento limitado 

De cada prueba con los datos recopilados se puede decir que:

 + Plot Basal
   En la señal temporal se observa una actividad casi constante con pocas variaciones, lo que refleja el estado de reposo muscular. En el espectro FFT aparecen picos aislados asociados principalmente a ruido de red eléctrica (60 Hz) y armónicos, mientras que la mayor parte de la energía es baja. En el método de Welch, la densidad espectral de potencia confirma que la señal se mantiene estable con picos definidos en frecuencias específicas, típicos de ruido más que de contracción muscular.

 + Movimiento libre
   En la señal temporal se aprecian contracciones claras, repetitivas y de mayor amplitud, lo que indica un mayor reclutamiento de fibras musculares durante el movimiento voluntario. En el FFT, la energía se distribuye en un rango más amplio de frecuencias (principalmente entre 50 y 150 Hz), lo cual es característico de la activación muscular real. El Welch suaviza la señal espectral y muestra un pico predominante en bajas frecuencias, junto con una pendiente descendente, típico de una contracción dinámica con alta variabilidad.
   
 + Movimiento limitado
   En la señal temporal se distinguen contracciones menos regulares pero con amplitudes elevadas en ciertos momentos, reflejando un esfuerzo parcial o con restricción. En el FFT, la energía sigue distribuida en un rango amplio pero con menor intensidad que en el movimiento libre. El análisis de Welch muestra un pico más pronunciado alrededor de los 50 Hz, pero con menor dispersión en altas frecuencias, lo que sugiere una activación muscular más controlada o forzada. 

## Plot por músculo 

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

### Bisceps:
<div align="center">

|  **Bisceps en reposo**  | **Bisceps sin oposición** | **Bisceps con oposición** |
|:------------:|:---------------:|:------------:|
| <a href="https://www.youtube.com/watch?v=VZrON9HyObU"><img src="https://img.youtube.com/vi/VZrON9HyObU/0.jpg" width="250" height="140"></a> | <a href="https://www.youtube.com/watch?v=jC3mxfnijYQ"><img src="https://img.youtube.com/vi/jC3mxfnijYQ/0.jpg" width="250" height="140"></a> | <a href="https://www.youtube.com/watch?v=hM2iXm7oM7Q"><img src="https://img.youtube.com/vi/hM2iXm7oM7Q/0.jpg" width="250" height="140"></a> |




## Ploteo en Python

### Plots EMG bíceps basal
![Plots EMG bíceps basal](/Otros/BicepBasal.png)

### Plots EMG Antebrazo en movimiento libre
![Plots EMG Bíceps en movimiento libre](/Otros/BicepLibre.png)

### Plots EMG Antebrazo en movimiento limitado
![Plots EMG Bíceps en movimiento limitado](/Otros/BicepLimitado.png)

</div>

### Trapecio:
<div align="center">

|  **Trapecio en reposo**  | **Trapecio sin oposición** | **Trapecio con oposición** |
|:------------:|:---------------:|:------------:|
| <a href="https://www.youtube.com/watch?v=s1ZrVtxSbU4"><img src="https://img.youtube.com/vi/s1ZrVtxSbU4/0.jpg" width="250" height="140"></a> | <a href="https://www.youtube.com/watch?v=bVA3Ll9P19Q"><img src="https://img.youtube.com/vi/bVA3Ll9P19Q/0.jpg" width="250" height="140"></a> | <a href="https://www.youtube.com/watch?v=Q7mYDY2JNNM"><img src="https://img.youtube.com/vi/Q7mYDY2JNNM/0.jpg" width="250" height="140"></a> |




## Ploteo en Python

### Plots EMG trapecio basal
![Plots EMG trapecio basal](/Otros/TrapecioBasal.png)

##### El ruido captado por el sensor es menor puesto que se tiene mejor conexión con la tierra. En parte por que el grosor de la piel es menor en la parte de atrás de la oreja en contraste con el apófisis estiloide del cúbito. El electrodo tiene mayor zona de contacto a comparación de colocarlo en el proceso mastoideo como sucedió en los casos anteriores.

### Plots EMG trapecio en movimiento libre
![Plots EMG trapecio en movimiento libre](/Otros/TrapecioLibre.png)

### Plots EMG trapecio en movimiento limitado
![Plots EMG trapecio en movimiento limitado](/Otros/TrapecioLimitado.png)

</div>


### Bibliografía:
