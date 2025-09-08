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
### Antebrazos:
<div align="center">

|  **Antebrazo en reposo**  | **Antebrazo sin oposición** | **Antebrazo con oposición** |
|:------------:|:---------------:|:------------:|

<figure>
  <img src="/Otros/AntebrazoBasal.png">
  <figcaption>Plots EMG Antebrazo Basal</figcaption>
</figure>

<figure>
  <img src="/Otros/AntebrazoLibre.png">
  <figcaption>Plots EMG Antebrazo en movimiento libre</figcaption>
</figure>

<figure>
  <img src="/Otros/AntebrazoLimitado.png">
  <figcaption>Plots EMG Antebrazo en movimiento limitado</figcaption>
</figure>

</div>

#### Ploteo en Python:

### Bisceps:
<div align="center">

|  **Bisceps en reposo**  | **Bisceps sin oposición** | **Bisceps con oposición** |
|:------------:|:---------------:|:------------:|


</div>

#### Ploteo en Python:

### Trapezio:
<div align="center">

|  **Trapezio en reposo**  | **Trapezio sin oposición** | **Trapezio con oposición** |
|:------------:|:---------------:|:------------:|

</div>

#### Ploteo en Python:

### Bibliografía:
