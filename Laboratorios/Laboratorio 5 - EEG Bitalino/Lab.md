# Análisis de Señales EEG con BiTalino: Métodos de Envolvente y Procesamiento

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Marco Teórico](#marco-teórico)
   - 2.1 [Señales EEG](#señales-eeg)
   - 2.2 [Métodos de Obtención de Envolvente](#métodos-de-obtención-de-envolvente)
3. [Metodología](#metodología)
   - 3.1 [Protocolo de Adquisición](#protocolo-de-adquisición)
   - 3.2 [Procesamiento de Señales](#procesamiento-de-señales)
4. [Resultados](#resultados)
   - 4.1 [Condición Basal](#condición-basal)
   - 4.2 [Mirada Fija](#mirada-fija)
   - 4.3 [30 Segundos (Basal2)](#30-segundos-basal2)
   - 4.4 [Parpadeo](#parpadeo)
   - 4.5 [Tarea de Resta](#tarea-de-resta)
   - 4.6 [Escuchando Huayno](#escuchando-huayno)
5. [Discusión](#discusión)
6. [Conclusiones](#conclusiones)
7. [Referencias](#referencias)

## Introducción

El electroencefalograma (EEG) es una técnica no invasiva que registra la actividad eléctrica del cerebro mediante electrodos colocados en el cuero cabelludo. La señal EEG refleja la suma de potenciales postsinápticos de miles de neuronas, proporcionando información valiosa sobre la función cerebral en diferentes estados cognitivos y conductuales.

En este trabajo de laboratorio se utilizó el sistema BiTalino para capturar señales EEG bajo diferentes condiciones experimentales, con el objetivo de analizar las características de la actividad cerebral mediante el cálculo de envolventes usando distintos métodos de procesamiento de señales.

## Marco Teórico

### Señales EEG

Las señales EEG se caracterizan por su naturaleza oscilatoria y su contenido frecuencial distribuido principalmente en las bandas alpha (8-13 Hz), beta (13-30 Hz), theta (4-8 Hz) y delta (0.5-4 Hz). La interpretación de estas señales requiere técnicas de procesamiento que permitan extraer información relevante sobre la actividad neural subyacente (Niedermeyer & Silva, 2005).

### Métodos de Obtención de Envolvente

La envolvente de una señal representa la variación temporal de su amplitud instantánea, siendo crucial para el análisis de señales EEG no estacionarias. Se implementaron tres métodos principales:

#### Hilbert + Filtro Pasa-Bajos

La transformada de Hilbert permite obtener la señal analítica, de la cual se extrae la amplitud instantánea. Posteriormente, se aplica un filtro pasa-bajos para suavizar la envolvente y eliminar fluctuaciones de alta frecuencia. Este método es especialmente efectivo para señales con componentes oscilatorias bien definidas.

Matemáticamente, para una señal x(t), su transformada de Hilbert H{x(t)} se define como:

```
H{x(t)} = (1/π) ∫ x(τ)/(t-τ) dτ
```

La señal analítica z(t) = x(t) + jH{x(t)} proporciona la amplitud instantánea |z(t)|.

#### Envolvente RMS Móvil (200ms ventana)

El método RMS (Root Mean Square) móvil calcula la raíz cuadrada de la media de los cuadrados de la señal en una ventana deslizante. Para este experimento se utilizó una ventana de 200 ms, proporcionando una medida robusta de la energía local de la señal EEG.

La fórmula RMS para una ventana de N muestras es:

```
RMS = √[(1/N) Σ x²(i)]
```

#### Hilbert + Savitzky-Golay

Este método combina la transformada de Hilbert para obtener la amplitud instantánea con el filtro Savitzky-Golay para el suavizado. El filtro Savitzky-Golay preserva mejor las características de la señal original mientras reduce el ruido, siendo particularmente útil para mantener picos y valles importantes en la envolvente (Savitzky & Golay, 1964).

## Metodología

### Protocolo de Adquisición

Se realizaron 6 tomas experimentales utilizando el sistema BiTalino para el registro de señales EEG. Las condiciones experimentales fueron las siguientes:

1. **Basal**: Estado de reposo con ojos cerrados
2. **Fijo**: Mirada fija hacia un punto específico
3. **30seg (Basal2)**: Segunda medición basal de 30 segundos
4. **Parpadeo**: Parpadeo voluntario repetitivo
5. **Resta**: Tarea cognitiva de resta mental
6. **Huayno**: Escucha de música tradicional andina

### Procesamiento de Señales

Para cada registro se aplicaron los tres métodos de obtención de envolvente mencionados anteriormente. El procesamiento incluyó filtrado previo de la señal cruda, eliminación de artefactos y normalización para facilitar la comparación entre métodos.

## Resultados

### Condición Basal

![EEGBasal](/Otros/EEGBasal.png)
*Figura 1: Señal EEG registrada durante condición basal*

![BasalSuavizada](/Otros/BasalSuavizada.png)
*Figura 2: Envolvente obtenida mediante Hilbert + Filtro Pasa-Bajos*

![BasalRMS](/Otros/BasalRMS.png)
*Figura 3: Envolvente RMS móvil con ventana de 200ms*

![BasalGolay](/Otros/BasalGolay.png)
*Figura 4: Envolvente obtenida mediante Hilbert + Savitzky-Golay*

Durante la condición basal se observó una actividad EEG característica del estado de reposo, con predominio de ondas alpha y fluctuaciones regulares de amplitud.

### Mirada Fija

![EEGFijos](/Otros/EEGFijo.png)
*Figura 5: Señal EEG durante tarea de mirada fija*

![FijoSuavizada](/Otros/FijoSuavizada.png)
*Figura 6: Envolvente obtenida mediante Hilbert + Filtro Pasa-Bajos*

![FijoRMS](/Otros/FijoRMS.png)
*Figura 7: Envolvente RMS móvil con ventana de 200ms*

![FijoGolay](/Otros/FijoGolay.png)
*Figura 8: Envolvente obtenida mediante Hilbert + Savitzky-Golay*

La tarea de mirada fija mostró una reducción en la actividad alpha comparada con el estado basal, reflejando el incremento en el nivel de atención visual.

### 30 Segundos (Basal2)

![EEG30seg](/Otros/EEG30seg.png)
*Figura 9: Señal EEG durante segunda medición basal*

![30segSuavizada](/Otros/30segSuavizada.png)
*Figura 10: Envolvente obtenida mediante Hilbert + Filtro Pasa-Bajos*

![30segRMS](/Otros/30segRMS.png)
*Figura 11: Envolvente RMS móvil con ventana de 200ms*

![30segGolay](/Otros/30segGolay.png)
*Figura 12: Envolvente obtenida mediante Hilbert + Savitzky-Golay*

La segunda medición basal confirmó la reproducibilidad de los patrones observados en la primera condición de reposo.

### Parpadeo

![EEGParpadeo](/Otros/EEGParpadeo.png)
*Figura 13: Señal EEG durante parpadeo voluntario*

![ParpadeoSuavizada](/Otros/ParpadeoSuavizada.png)
*Figura 14: Envolvente obtenida mediante Hilbert + Filtro Pasa-Bajos*

![ParpadeoRMS](/Otros/ParpadeoRMS.png)
*Figura 15: Envolvente RMS móvil con ventana de 200ms*

![ParpadeoGolay](/Otros/ParpadeoGolay.png)
*Figura 16: Envolvente obtenida mediante Hilbert + Savitzky-Golay*

El parpadeo voluntario generó artefactos característicos de alta amplitud, claramente identificables en todas las envolventes calculadas.

### Tarea de Resta

![EEGResta](/Otros/EEGResta.png)
*Figura 17: Señal EEG durante tarea de resta mental*

![RestaSuavizada](/Otros/RestaSuavizada.png)
*Figura 18: Envolvente obtenida mediante Hilbert + Filtro Pasa-Bajos*

![RestaRMS](/Otros/RestaRMS.png)
*Figura 19: Envolvente RMS móvil con ventana de 200ms*

![RestaGolay](/Otros/RestaGolay.png)
*Figura 20: Envolvente obtenida mediante Hilbert + Savitzky-Golay*

Durante la tarea cognitiva de resta mental se observó un incremento en la actividad beta, indicativo del procesamiento cognitivo activo.

### Escuchando Huayno

![EEGHuayno](/Otros/EEGHuayno.png)
*Figura 21: Señal EEG durante escucha de música tradicional*

![HuaynoSuavizada](/Otros/HuaynoSuavizada.png)
*Figura 22: Envolvente obtenida mediante Hilbert + Filtro Pasa-Bajos*

![HuaynoRMS](/Otros/HuaynoRMS.png)
*Figura 23: Envolvente RMS móvil con ventana de 200ms*

![HuaynoGolay](/Otros/HuaynoGolay.png)
*Figura 24: Envolvente obtenida mediante Hilbert + Savitzky-Golay*

La escucha de música tradicional andina mostró patrones únicos de activación, posiblemente relacionados con el procesamiento auditivo y la respuesta emocional.

## Discusión

Los tres métodos de obtención de envolvente mostraron ventajas específicas dependiendo de las características de la señal EEG analizada. El método Hilbert + filtro pasa-bajos proporcionó envolventes suaves y continuas, ideales para análisis de tendencias generales. El método RMS móvil mostró mayor sensibilidad a cambios abruptos en la amplitud, siendo útil para detectar eventos transitorios. Por su parte, el filtro Savitzky-Golay preservó mejor los detalles finos de la envolvente mientras mantenía un nivel adecuado de suavizado.

La comparación entre condiciones experimentales reveló diferencias claras en los patrones de activación cerebral. Las condiciones basales mostraron la actividad alpha característica del estado de reposo, mientras que las tareas cognitivas y sensoriales produjeron cambios específicos en la actividad neural (Berger, 1929; Cohen, 2014).

## Conclusiones

Este estudio demostró la efectividad del sistema BiTalino para el registro de señales EEG en diferentes condiciones experimentales. Los tres métodos de obtención de envolvente implementados proporcionaron información complementaria sobre la dinámica temporal de la actividad cerebral.

Los resultados confirman que cada método de envolvente tiene aplicaciones específicas según el tipo de análisis requerido. La combinación de múltiples técnicas de procesamiento permite una caracterización más completa de las señales EEG registradas.

Las diferencias observadas entre condiciones experimentales validan la sensibilidad del sistema de registro y los métodos de análisis implementados para detectar cambios en la actividad neural asociados con diferentes estados cognitivos y conductuales.

## Referencias

Berger, H. (1929). Über das Elektroenkephalogramm des Menschen. *Archiv für Psychiatrie und Nervenkrankheiten*, 87(1), 527-570.

Cohen, M. X. (2014). *Analyzing neural time series data: theory and practice*. MIT Press.

Niedermeyer, E., & Silva, F. L. D. (2005). *Electroencephalography: basic principles, clinical applications, and related fields*. Lippincott Williams & Wilkins.

Savitzky, A., & Golay, M. J. (1964). Smoothing and differentiation of data by simplified least squares procedures. *Analytical Chemistry*, 36(8), 1627-1639.

Teplan, M. (2002). Fundamentals of EEG measurement. *Measurement Science Review*, 2(2), 1-11.
