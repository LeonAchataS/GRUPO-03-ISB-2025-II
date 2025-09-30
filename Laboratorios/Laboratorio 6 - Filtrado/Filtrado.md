# Filtrado Digital de Señales Biomédicas: ECG y EMG

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Señales Biomédicas](#señales-biomédicas)
   - 2.1 [Electrocardiograma (ECG)](#electrocardiograma-ecg)
   - 2.2 [Electromiografía (EMG)](#electromiografía-emg)
3. [Fundamentos del Filtrado Digital](#fundamentos-del-filtrado-digital)
   - 3.1 [Filtro FIR con Ventana](#1-fir-con-ventana)
   - 3.2 [Filtro Butterworth](#2-butterworth)
   - 3.3 [Filtro Chebyshev Tipo I](#3-chebyshev-tipo-i)
   - 3.4 [Filtro Notch](#4-notch)
4. [Metodología](#metodología)
5. [Ploteo en Python](#Ploteo-en-Python)
7. [Resultados y Análisis](#resultados-y-análisis)
   - 5.1 [Señal ECG Basal](#señal-1-ecg-basal)
   - 5.2 [Señal ECG Agitado](#señal-2-ecg-agitado)
   - 5.3 [Señal EMG Bíceps Libre](#señal-3-emg-bíceps-libre)
   - 5.4 [Señal EMG Bíceps Limitado](#señal-4-emg-bíceps-limitado)
8. [Conclusiones](#conclusiones)
9. [Bibliografía](#bibliografía)

---

## Introducción

En el procesamiento de señales biomédicas, como ECG, EEG o EMG, el ruido y los artefactos pueden interferir con la interpretación clínica y la recuperación de parámetros diagnósticos. El filtrado digital es actualmente el método principal para eliminar la señal no deseada causada por interferencias externas, como el ruido de la línea eléctrica, la contracción muscular o la deriva de baja frecuencia [1].

Los filtros están diseñados para preservar las características deseadas de la señal y mejorar la relación señal-ruido (SNR), lo que facilita la visualización y el procesamiento automático. Además, el filtrado computacional ofrece una solución mejorada en comparación con los métodos analógicos convencionales, puesto que es más adaptable al ajustar la frecuencia de corte, la pendiente y el orden del filtro sin necesidad de modificar el hardware [4]. Esto produce un procesamiento más preciso y reproducible, especialmente ventajoso en entornos clínicos y de investigación, donde la calidad de la señal influye directamente en la precisión del diagnóstico y el desarrollo de nuevos dispositivos biomédicos.

En el caso específico de este laboratorio, se procesaron dos señales ECG y dos señales EMG superficiales, evaluando el desempeño de cuatro tipos de filtros digitales diferentes.

---

## Señales Biomédicas

### Electrocardiograma (ECG)

El ECG es una señal biomédica que registra la actividad eléctrica del corazón desde la superficie de la piel. La señal ECG típicamente contiene ondas características denominadas P, QRS y T, que representan diferentes fases del ciclo cardíaco [7]. El rango de frecuencias de interés en señales ECG se encuentra entre 0.5 Hz y 150 Hz, siendo el complejo QRS el componente de mayor amplitud y contenido en alta frecuencia [8].

**Fuentes de ruido en ECG:**

Las señales ECG están sujetas a diversos tipos de ruido y artefactos que pueden comprometer su calidad [7]:

- **Deriva de línea base (Baseline Wander):** Ruido de baja frecuencia (0.5-0.6 Hz) causado por la respiración y movimientos del paciente
- **Interferencia de línea eléctrica (Powerline Interference - PLI):** Ruido de 50/60 Hz proveniente de la red eléctrica
- **Artefactos musculares (Muscle Artifacts):** Señales EMG de alta frecuencia (>100 Hz) generadas por contracciones musculares involuntarias
- **Artefactos de movimiento de electrodos:** Señales transitorias de alta amplitud causadas por contacto deficiente entre el electrodo y la piel

Para el filtrado de señales ECG, se recomienda el uso de filtros de duración finita (FIR) con ventana tipo Hamming, debido a su fase lineal que preserva la morfología de las ondas características [1, 2].

### Electromiografía (EMG)

La electromiografía superficial (sEMG) registra la actividad eléctrica generada por la contracción muscular desde la superficie de la piel. La señal EMG es el resultado de la suma de potenciales de acción de múltiples unidades motoras activas durante la contracción muscular [9]. El espectro de frecuencias de las señales EMG superficiales se encuentra típicamente entre 10 Hz y 500 Hz, con la mayor parte de la energía concentrada entre 20 Hz y 400 Hz [8, 9].

**Fuentes de ruido en EMG:**

Las señales EMG de superficie están contaminadas por diversos tipos de ruido [9]:

- **Ruido de baja frecuencia:** Artefactos de movimiento y deriva de línea base (<20 Hz)
- **Interferencia de línea eléctrica:** Ruido a 50/60 Hz de fuentes de alimentación
- **Ruido blanco gaussiano:** Ruido de alta frecuencia (>500 Hz) proveniente de la instrumentación electrónica
- **Crosstalk:** Interferencia de músculos adyacentes
- **Ruido de interfaz electrodo-piel:** Causado por cambios en la impedancia del contacto

Para el procesamiento de señales EMG de superficie, se emplean filtros pasa banda con frecuencias de corte de 20 Hz a 400-450 Hz [3]. De igual manera que en el caso de las señales ECG, también se opta por el uso de ventanas Hamming para filtros FIR.

---

## Fundamentos del Filtrado Digital

### 1. FIR con Ventana

**Diseño:** A partir de la respuesta ideal se debe truncarla con una ventana como Hamming, Hann o Blackman para obtener coeficientes finitos. La ventana Hamming es ampliamente utilizada debido a su capacidad para reducir los lóbulos laterales en la respuesta en frecuencia [2].

**Parámetros típicos:** 
- Orden N, dependiendo de la transición deseada
- Tipo de ventana (Hamming, Hann, Blackman)
- Frecuencias de corte normalizadas respecto a la frecuencia de Nyquist

**Características:**
- **Fase lineal:** Preserva la morfología temporal de la señal
- **Estabilidad:** Siempre estable por ser no recursivo
- **Costo computacional:** Mayor número de operaciones que filtros IIR

**Aplicación para ECG:** Muy bueno, la fase lineal preserva la morfología de las ondas P, QRS y T, crucial para análisis clínico [1].

**Aplicación para EMG:** Bueno también, especialmente para evitar distorsión de fase. Para EMG de bandas altas se puede requerir orden mayor para transiciones nítidas [3].

### 2. Butterworth

**Diseño:** Filtro IIR diseñado mediante transformación bilineal para llevarlo al dominio discreto. Se caracteriza por tener una respuesta maximamente plana en la banda pasante [4].

**Parámetros típicos:** 
- Orden n, comúnmente 2–6
- Frecuencias de corte según la aplicación
- Tipo de filtro (pasa-bajo, pasa-alto, pasa-banda)

**Características:**
- **Respuesta en frecuencia:** Suave transición, sin ondulaciones en banda pasante
- **Fase:** No lineal (puede distorsionar la morfología)
- **Eficiencia:** Requiere menos operaciones que FIR para pendientes similares

**Aplicación para ECG:** Bueno si se busca un filtro eficiente y con pocas operaciones o baja latencia. Puede distorsionar la morfología si se aplica causalmente, pero el uso de `filtfilt` (filtrado bidireccional) mitiga este problema [8].

**Aplicación para EMG:** Adecuado por su eficiencia computacional. Filtrar EMG en tiempo real conviene con IIR de orden bajo-medio [8].

### 3. Chebyshev Tipo I

**Diseño:** Filtro IIR que permite ondulación (ripple) en la banda pasante a cambio de una transición más abrupta entre banda pasante y de rechazo [4].

**Parámetros típicos:** 
- Orden n y ripple en dB
- Lo común es 0.5–1 dB de ripple
- Frecuencias de corte

**Características:**
- **Pendiente:** Más pronunciada que Butterworth para el mismo orden
- **Ondulación:** Presenta ripple en banda pasante
- **Selectividad:** Mayor rechazo en banda de atenuación

**Aplicación para ECG:** Se debe usar con precaución, ya que la ondulación puede alterar la morfología. Si se aplica `filtfilt` y ripple muy pequeño, puede ser aceptable.

**Aplicación para EMG:** Útil cuando se necesita mayor rechazo fuera de banda con orden bajo, como para separar componentes cercanas en frecuencia. La distorsión de fase debe considerarse [9].

### 4. Notch

**Diseño:** Filtro resonante con atenuación en 50 Hz o 60 Hz y ancho determinado. El factor de calidad Q = 30–50 permite obtener una atenuación estrecha y selectiva [7].

**Parámetros típicos:** 
- Frecuencia notch de 50 o 60 Hz (según región)
- Factor de calidad Q o ancho de banda en Hz
- Profundidad de atenuación

**Características:**
- **Selectividad:** Alta atenuación en frecuencia específica
- **Ancho de banda:** Estrecho para preservar frecuencias adyacentes
- **Aplicación:** Específica para interferencia de línea eléctrica

**Aplicación para ECG:** Frecuentemente imprescindible para eliminar 50-60 Hz. Preferible usar notch con cuidado para no eliminar contenido útil si la señal tiene componentes en esa banda [7, 8].

**Aplicación para EMG:** Igualmente útil, ya que la señal EMG suele contener energía en banda 50–300 Hz, así que un notch estrecho es mejor para no eliminar demasiada información [9].

---

## Metodología

Para este laboratorio se procesaron cuatro señales biomédicas:
- **ECG_basal:** Señal ECG en estado de reposo
- **ECG_agitado:** Señal ECG durante actividad física
- **EMG_bicep_libre:** Señal EMG del bíceps sin resistencia
- **EMG_bicep_limitado:** Señal EMG del bíceps con resistencia

Todas las señales fueron adquiridas con una frecuencia de muestreo de **fs = 1000 Hz**.

**Parámetros de filtrado utilizados:**

Para señales ECG:
- Filtro pasa-banda: 0.5 - 40 Hz
- Orden FIR: 101
- Orden Butterworth/Chebyshev: 4
- Ripple Chebyshev: 0.5 dB

Para señales EMG:
- Filtro pasa-banda: 20 - 450 Hz
- Orden FIR: 101
- Orden Butterworth/Chebyshev: 4
- Ripple Chebyshev: 0.5 dB

Para filtro Notch (ambas señales):
- Frecuencia central: 60 Hz
- Factor de calidad Q: 30

Se aplicó filtrado bidireccional mediante la función `filtfilt` para todos los filtros IIR con el objetivo de eliminar la distorsión de fase.

---

## Ploteo en Python

El código de procesamiento se encuentra en el archivo `Laboratorios/Laboratorio 6 - Filtrado/plot.py` y fue desarrollado en Python utilizando las bibliotecas `numpy`, `pandas`, `matplotlib` y `scipy.signal`.

### Estructura del Script

El script implementa un procesamiento secuencial de las cuatro señales biomédicas, aplicando automáticamente los cuatro tipos de filtros a cada una. La estructura general sigue el siguiente flujo:

1. **Lectura de datos:** Las señales se cargan desde archivos `.txt` con formato tabular separado por tabulaciones. Se extraen específicamente los valores de la columna `A1` que contiene la señal analógica de interés.

2. **Detección automática de tipo de señal:** El script identifica si la señal es ECG o EMG mediante el nombre del archivo, ajustando automáticamente las frecuencias de corte del filtrado pasa-banda:
   - **ECG:** 0.5 - 40 Hz
   - **EMG:** 20 - 450 Hz

3. **Aplicación de filtros:** Para cada señal, se aplican secuencialmente los cuatro filtros:

   - **FIR con ventana Hamming:** Se utiliza `signal.firwin()` con orden 101 y configuración pasa-banda (`pass_zero=False`)
   
   - **Butterworth:** Se diseña con `signal.butter()` de orden 4 y tipo pasa-banda
   
   - **Chebyshev Tipo I:** Se implementa con `signal.cheby1()` de orden 4 y ripple de 0.5 dB
   
   - **Notch:** Se diseña con `signal.iirnotch()` con frecuencia central de 60 Hz y factor de calidad Q=30

4. **Filtrado bidireccional:** Todos los filtros se aplican mediante `signal.filtfilt()`, que realiza un filtrado hacia adelante y hacia atrás, eliminando la distorsión de fase y resultando en un filtro de fase cero.

5. **Visualización y almacenamiento:** Para cada combinación señal-filtro, se genera un gráfico de dos subplots:
   - **Subplot superior:** Señal original (primeros 5 segundos)
   - **Subplot inferior:** Señal filtrada (primeros 5 segundos)
   
   Los gráficos se guardan automáticamente como archivos `.png` con nomenclatura `{nombre_señal}_{nombre_filtro}.png` en el directorio especificado.

### Consideraciones de Implementación

El uso de `filtfilt()` es crucial para aplicaciones biomédicas offline, ya que duplica el orden efectivo del filtro (por ejemplo, un Butterworth de orden 4 se convierte en orden 8) y elimina el retardo de grupo, preservando la alineación temporal de los eventos fisiológicos en la señal.

La normalización de frecuencias respecto a la frecuencia de Nyquist (fs/2 = 500 Hz) es necesaria para el diseño correcto de los filtros digitales en `scipy.signal`.

---

## Resultados y Análisis

### Señal 1: ECG Basal

#### Comparación de Filtros

![ECG Basal - FIR](/Otros/ECG_basal_FIR.png)

![ECG Basal - Butterworth](/Otros/ECG_basal_Butter.png)

![ECG Basal - Chebyshev](/Otros/ECG_basal_Cheby.png)

![ECG Basal - Notch](/Otros/ECG_basal_Notch.png)

#### Análisis

**Filtro seleccionado:** FIR con ventana Hamming

**Justificación:**

- **vs. Butterworth:** Aunque el filtro Butterworth es computacionalmente más eficiente, el filtro FIR ofrece fase lineal que preserva mejor la morfología de las ondas P, QRS y T. En análisis clínico de ECG en reposo, la preservación exacta de la forma de onda es crucial para detectar anomalías sutiles.

- **vs. Chebyshev:** El filtro Chebyshev presenta ondulaciones en la banda pasante que pueden introducir distorsiones en la amplitud de las ondas características del ECG. Para señales en estado basal donde se requiere alta fidelidad, estas ondulaciones son indeseables.

- **vs. Notch:** El filtro Notch solo elimina la interferencia de 60 Hz pero no atenúa el ruido de baja frecuencia (deriva de línea base) ni el ruido muscular de alta frecuencia. Es útil como complemento pero insuficiente por sí solo.

---

### Señal 2: ECG Agitado

#### Comparación de Filtros

![ECG Agitado - FIR](/Otros/ECG_agitado_FIR.png)

![ECG Agitado - Butterworth](/Otros/ECG_agitado_Butter.png)

![ECG Agitado - Chebyshev](/Otros/ECG_agitado_Cheby.png)

![ECG Agitado - Notch](/Otros/ECG_agitado_Notch.png)

#### Análisis

**Filtro seleccionado:** FIR con ventana Hamming

**Justificación:**

- **vs. Butterworth:** En señales ECG durante actividad física, los artefactos de movimiento y ruido muscular son más prominentes. El filtro FIR, al tener fase lineal y ser no recursivo, maneja mejor estos artefactos transitorios sin introducir oscilaciones (ringing) que los filtros IIR podrían generar.

- **vs. Chebyshev:** La transición más abrupta del Chebyshev podría ser ventajosa para rechazar ruido fuera de banda, pero las ondulaciones en banda pasante pueden amplificar componentes de ruido que coincidan con las frecuencias de ripple, lo cual es problemático en señales con alto contenido de artefactos.

- **vs. Notch:** Similar al caso anterior, elimina solo la componente de 60 Hz pero no es suficiente para manejar el ruido de movimiento y artefactos musculares presentes durante la actividad física.

---

### Señal 3: EMG Bíceps Libre

#### Comparación de Filtros

![EMG Bíceps Libre - FIR](/Otros/EMG_bicep_libre_FIR.png)

![EMG Bíceps Libre - Butterworth](/Otros/EMG_bicep_libre_Butter.png)

![EMG Bíceps Libre - Chebyshev](/Otros/EMG_bicep_libre_Cheby.png)

![EMG Bíceps Libre - Notch](/Otros/EMG_bicep_libre_Notch.png)

#### Análisis

**Filtro seleccionado:** Butterworth

**Justificación:**

- **vs. FIR:** Para señales EMG, donde el análisis se centra principalmente en características espectrales (frecuencia media, frecuencia mediana) y de amplitud (RMS) en lugar de morfología temporal precisa, la fase lineal no es tan crítica. El filtro Butterworth ofrece mejor eficiencia computacional con desempeño aceptable, especialmente útil para aplicaciones en tiempo real.

- **vs. Chebyshev:** Aunque el Chebyshev proporciona mejor rechazo fuera de banda, las ondulaciones en banda pasante pueden afectar la estimación de parámetros espectrales de la señal EMG. En contracciones libres sin mayor contaminación, la respuesta plana del Butterworth es más adecuada.

- **vs. Notch:** El filtro Notch aislado no proporciona el filtrado pasa-banda necesario para eliminar artefactos de movimiento de baja frecuencia (<20 Hz) y ruido electrónico de alta frecuencia (>450 Hz). Una combinación Notch + Butterworth pasa-banda sería ideal, pero Butterworth pasa-banda solo es suficiente si la interferencia de 60 Hz no es dominante.

---

### Señal 4: EMG Bíceps Limitado

#### Comparación de Filtros

![EMG Bíceps Limitado - FIR](/Otros/EMG_bicep_limitado_FIR.png)

![EMG Bíceps Limitado - Butterworth](/Otros/EMG_bicep_limitado_Butter.png)

![EMG Bíceps Limitado - Chebyshev](/Otros/EMG_bicep_limitado_Cheby.png)

![EMG Bíceps Limitado - Notch](/Otros/EMG_bicep_limitado_Notch.png)

#### Análisis

**Filtro seleccionado:** Butterworth

**Justificación:**

- **vs. FIR:** Al igual que en la señal EMG libre, la fase lineal no es crítica para el análisis de parámetros de fatiga muscular. El Butterworth ofrece un balance óptimo entre rendimiento y eficiencia computacional, lo cual es valioso en estudios de resistencia donde se procesan largos segmentos de señal.

- **vs. Chebyshev:** En condiciones de contracción con resistencia, donde la señal EMG tiene mayor amplitud y mejor SNR, el Butterworth es suficiente. El Chebyshev sería más útil en escenarios con fuerte interferencia externa que requiera mayor rechazo en banda de atenuación.

- **vs. Notch:** Similar al caso anterior, el filtro Notch es insuficiente por sí solo. Sin embargo, en ambientes con fuerte interferencia de línea eléctrica, una cascada de Notch + Butterworth pasa-banda sería la configuración óptima.

---

## Conclusiones

El presente estudio evaluó cuatro tipos de filtros digitales aplicados a señales ECG y EMG, demostrando que la elección del filtro óptimo depende del tipo de señal y la aplicación específica:

1. **Para señales ECG:** Los filtros FIR con ventana Hamming son preferibles debido a su fase lineal, que preserva la morfología de las ondas características (P, QRS, T) esencial para el diagnóstico clínico. Esto se confirma tanto en condiciones basales como durante actividad física.

2. **Para señales EMG:** Los filtros Butterworth ofrecen el mejor compromiso entre eficiencia computacional y calidad de filtrado, siendo adecuados para análisis de fatiga muscular y control de prótesis donde la fase lineal no es crítica.

3. **Filtros Chebyshev:** Útiles en escenarios específicos donde se requiere mayor selectividad en frecuencia, pero deben usarse con cuidado debido a las ondulaciones en banda pasante que pueden afectar la interpretación de parámetros clínicos.

4. **Filtros Notch:** Indispensables como complemento para eliminar interferencia de línea eléctrica (50/60 Hz), pero insuficientes como solución única. Se recomienda su uso en cascada con filtros pasa-banda.

5. **Consideraciones prácticas:** 
   - Para análisis offline: FIR (ECG) y Butterworth con `filtfilt` (EMG)
   - Para procesamiento en tiempo real: Butterworth o Chebyshev de orden bajo
   - En ambientes con alta interferencia eléctrica: Combinación de Notch + filtro pasa-banda

Los resultados obtenidos demuestran la importancia de seleccionar el filtro apropiado según los requisitos específicos de cada aplicación biomédica, balanceando entre preservación de características de la señal, eficiencia computacional y rechazo de ruido.

---

## Bibliografía

[1] O. Ondráček, J. Púčik, and E. Cocherová, "Filters for ECG digital signal processing," *Trends in Biomedical Engineering*, pp. 91–96, 2005. Available: https://www.researchgate.net/publication/234047548_FILTERS_FOR_ECG_DIGITAL_SIGNAL_PROCESSING

[2] I. A. Sulaiman, H. M. Hassan, M. Danish, M. Singh, P. K. Singh, and M. Rajoriya, "Design, comparison and analysis of low pass FIR filter using window techniques method," *Materials Today: Proceedings*, Dec. 2020, doi: https://doi.org/10.1016/j.matpr.2020.10.952

[3] "EMG Signal Processing: Key Techniques and Practical Recommendations," Noraxon.com, 2025. Available: https://www.noraxon.com/article/emg-signal-processing-key-techniques-and-practical-recommendations/

[4] A. S. Bhat, *Biomedical Signal Processing: Principles and Techniques*. CRC Press, 2017.

[5] J. G. Webster, *Medical Instrumentation: Application and Design*, 4th ed. Hoboken, NJ, USA: Wiley, 2010.

[6] P. Laguna, R. G. Mark, A. Goldberg, and G. B. Moody, "A database for evaluation of algorithms for measurement of QT and other waveform intervals in the ECG," *Computers in Cardiology*, vol. 24, pp. 673–676, 1997.

[7] L. Sörnmo and P. Laguna, *Bioelectrical Signal Processing in Cardiac and Neurological Applications*. Burlington, MA: Elsevier Academic Press, 2005.

[8] C. J. De Luca, L. D. Gilmore, M. Kuznetsov, and S. H. Roy, "Filtering the surface EMG signal: Movement artifact and baseline noise contamination," *Journal of Biomechanics*, vol. 43, no. 8, pp. 1573–1579, 2010.

[9] M. Boyer, L. Bouyer, J. S. Roy, and A. Campeau-Lecours, "Reducing Noise, Artifacts and Interference in Single-Channel EMG Signals: A Review," *Sensors*, vol. 23, no. 6, p. 2927, 2023.


## Contribución:
##### - Leon Achata 33.33%
##### - Nicolas Arango 33.33%
##### - Hans Navarro 33.33%
