## Introducción 
##### En el procesamiento de señales biomédicas, como ECG, EEG o EMG, el ruido y los artefactos pueden interferir con la interpretación clínica y la recuperación de parámetros. El filtrado digital es actualmente el método principal para eliminar la señal no deseada causada por interferencias externas, como el ruido de la línea eléctrica, la contracción muscular o la deriva de baja frecuencia. Los filtros están diseñados para preservar las características deseadas de la señal y mejorar la relación señal-ruido, lo que facilita la visualización y el procesamiento automático. Además, el filtrado computacional ofrece una solución mejorada en comparación con los métodos analógicos convencionales, puesto que es más adaptable. Sea al ajustar la frecuencia de corte, la pendiente y el orden del filtro sin necesidad de modificar el hardware. Esto produce un procesamiento más preciso y reproducible, especialmente ventajoso en entornos clínicos y de investigación, donde la calidad de la señal influye directamente en la precisión del diagnóstico y el desarrollo de nuevos dispositivos biomédicos. En el caso específico de este laboratorio se van a procesar dos señales EMG y dos ECG:


### ECG:
##### Se suele empelar filtros de duración finita (FIR) [1]. Para el uso de ventanas se recomienda el uso del tipo Hamming [2].

### EMG: 
##### Al tratarse de EMG de superficie, se usan filtros pasa banda de 20Hz a 400-450 Hz [3]. De igual manera que en el caso de las señales ECG, también se opta por el uso de ventanas Hamming.

### FILTROS

#### 1. FIR con ventana

- Diseño: Apartir de la respuesta ideal se debe truncarla con una ventana como Hamming, Hann o Blackman para obtener coeficientes finitos.

- Parámetros típicos: Orden N, dependiendo de la transición deseada; por ejemplo, la ventana Hamming reduce lóbulos laterales.

- Resultado esperado: Respuesta en frecuencia controlada, posible fase lineal, útil cuando se requiere conservación de la morfología de la señal.

- Para filtrar ECG: Muy bueno, fase lineal preserva morfología de P, QRS y T.

- Para filtrar EMG: Bueno también, especialmente para evitar distorsión de fase, para EMG de bandas altas se puede requerir orden mayor para transiciones nítidas.

#### 2. Butterworth

- Diseño: Transformación bilineal para llevarlo a dominio discreto. Utilizando el concepto de diseño IIR y la transformada. 

- Parámetros típicos: Orden n, comúnmente 2–6, frecuencias de corte según la aplicación.

- Resultado esperado: Buena atenuación fuera de banda con pendiente moderada, sin oscilaciones en la banda pasante.

- Para filtrar ECG: Bueno si se busca un filtro eficiente y con pocas operaciones o baja latencia. No tiene fase lineal, ya que puede distorsionar la morfología si se aplica causalmente.

- Para filtrar EMG: Adecuado por su eficiencia computacional, filtrar EMG en tiempo real conviene con IIR de orden bajo-medio.

#### 3. Chebyshev Tipo I

- Diseño: Se eligen orden y ripple (dB) para controlar la ondulación y la pendiente.

- Parámetros típicos: Orden n y ripple en dB, lo cumún es 0.5–1 dB.

- Resultado esperado: Para un mismo orden, ofrece pendiente más pronunciada que Butterworth, pero con ondulación en la banda pasante.

- Para filtrar ECG: Se debe usar con precaución, ya que la ondulación puede alterar la morfología, si se aplica filtfilt y ripple muy pequeño, puede ser aceptable.

- Para filtrar EMG: Útil cuando se necesita mayor rechazo fuera de banda con orden bajo como separar componentes cercanas en frecuencia, pero la distorsión de fase peligraría.

#### 4. Notch

- Diseño: Diseño de un filtro resonante con atenuación en 50 Hz o 60 Hz y ancho determinado como Q = 30–50 para obtener una lámina angosta.

- Parámetros típicos: Frecuencia notch de 50 o 60 Hz, factor de calidad Q o ancho en Hz.

- Resultado esperado: Atenuación fuerte en la frecuencia de la red sin afectar mucho las frecuencias adyacentes si Q alto.

- Para filtrar ECG: Frecuentemente imprescindible para eliminar 50-60 Hz, preferible usar notch con cuidado para no eliminar contenido útil si la señal tiene componentes en esa banda.

- Para filtrar EMG: Igualmente útil, ya que la señal EMG suele contener energía en banda 50–300 Hz, así que un notch estrecho es mejor para no eliminar demasiada información.

### Razonamiento para la elección del mejor filtro para las señales

- Preservación de morfología entonces es preferinle elegir un filtro FIR lineal de fase o aplicar filtfilt con IIR en análisis offline.

- Recursos computacionales o latencia entonces IIR como Butterworth o Chebyshev, ya que ofrecen mayor eficiencia, es una buena elección para procesamiento en tiempo real.

- Rechazo de banda específica como línea eléctrica entonces Notch o combinación notch + bandpass.

- Necesidad de transición muy abrupta entonces Chebyshev o Ellíptico si es que se tolera la ondulación.

### Filtrado de las señales

### BORRA ESTE MENSAJE XD, describí 4 filtros, puedes usar esos 4, pero normal si usas otros, si es que los cambias tmb deberas cambiar la descripción y poner los 4 filtros que estarás usando.

#### Señal 1 ECG 

| FILTRO IDEAL | FILTRO 2 | FILTRO 3| FILTRO 4|
|------|-----------------|-----------------|------|
| XD   | XD | XD | XD |

#### Resultados

##### El filtro ideal escogido fue...... en comparación al filtro 2 es mejor porque, en comparación al firltro 3 es mejor porque....., en comparación al firltro 4 es mejor porque

#### Señal 2 ECG 

| FILTRO IDEAL | FILTRO 2 | FILTRO 3| FILTRO 4|
|------|-----------------|-----------------|------|
| XD   | XD | XD | XD |

#### Resultados

##### El filtro ideal escogido fue...... en comparación al filtro 2 es mejor porque, en comparación al firltro 3 es mejor porque....., en comparación al firltro 4 es mejor porque

#### Señal 3 EMG

| FILTRO IDEAL | FILTRO 2 | FILTRO 3| FILTRO 4|
|------|-----------------|-----------------|------|
| XD   | XD | XD | XD |

#### Resultados

##### El filtro ideal escogido fue...... en comparación al filtro 2 es mejor porque, en comparación al firltro 3 es mejor porque....., en comparación al firltro 4 es mejor porque

#### Señal 4 EMG

| FILTRO IDEAL | FILTRO 2 | FILTRO 3| FILTRO 4|
|------|-----------------|-----------------|------|
| XD   | XD | XD | XD |

#### Resultados

##### El filtro ideal escogido fue...... en comparación al filtro 2 es mejor porque, en comparación al firltro 3 es mejor porque....., en comparación al firltro 4 es mejor porque

## Bibliografía:
##### [1] Oldřich Ondráček, Jozef Púčik, and E. Cocherová, “FILTERS FOR ECG DIGITAL SIGNAL PROCESSING,” Trends in Biomedical Engineering” Setiembre 7 - 9, 2005, University of ZilinaTrends in Biomedical Engineering” September 7 - 9, 2005, University of Zilina, pp. 91–96, En. 2005, Available: https://www.researchgate.net/publication/234047548_FILTERS_FOR_ECG_DIGITAL_SIGNAL_PROCESSING

##### [2] I. A. Sulaiman, H. M. Hassan, M. Danish, M. Singh, P. K. Singh, and M. Rajoriya, “Design, comparison and analysis of low pass FIR filter using window techniques method,” Materials Today: Proceedings, Dic. 2020, doi: https://doi.org/10.1016/j.matpr.2020.10.952.

##### [3] “EMG Signal Processing: Key Techniques and Practical Recommendations – Noraxon,” Noraxon.com, 2025. https://www.noraxon.com/article/emg-signal-processing-key-techniques-and-practical-recommendations/

##### [4] A. S. Bhat, Biomedical Signal Processing: Principles and Techniques. CRC Press, 2017.

##### [5] J. G. Webster, Medical Instrumentation: Application and Design, 4th ed. Hoboken, NJ, USA: Wiley, 2010.

##### [6] P. Laguna, R. G. Mark, A. Goldberg, and G. B. Moody, “A database for evaluation of algorithms for measurement of QT and other waveform intervals in the ECG,” Computers in Cardiology, vol. 24, pp. 673–676, 1997.
‌
