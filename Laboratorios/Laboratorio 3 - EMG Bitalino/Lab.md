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

| Antebrazo en reposo | Antebrazo sin oposición | Antebrazo con oposición |
|---------------------|-------------------------|-------------------------|
| <a href="https://youtube.com/shorts/F46p1PJufy0?feature=share"><img src="https://img.youtube.com/vi/F46p1PJufy0/0.jpg" width="250" height="140"></a> 
 <a href="https://youtube.com/shorts/cBVej_iqN20?feature=share"><img src="https://img.youtube.com/vi/cBvej_iqN20/0.jpg" width="250" height="140"></a> 
 <a href="https://youtube.com/shorts/O7S6IrTmvPA?feature=share"><img src="https://img.youtube.com/vi/O7S6lRxxxxx/0.jpg" width="250" height="140"></a> |


## Ploteo en Python

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

## Ploteo en Python

### Plots EMG trapecio basal
![Plots EMG trapecio basal](/Otros/TrapecioBasal.png)

### Plots EMG trapecio en movimiento libre
![Plots EMG trapecio en movimiento libre](/Otros/TrapecioLibre.png)

### Plots EMG trapecio en movimiento limitado
![Plots EMG trapecio en movimiento limitado](/Otros/TrapecioLimitado.png)

</div>


### Bibliografía:
