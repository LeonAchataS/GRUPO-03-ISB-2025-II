# Laboratorio ECG con Bitalino: Detección y Procesamiento de Señales Electrocardiográficas

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Formación de la Señal ECG](#formación-de-la-señal-ecg)
3. [Bitalino para Adquisición de ECG](#bitalino-para-adquisición-de-ecg)
4. [Procesamiento y Filtrado de Señales](#procesamiento-y-filtrado-de-señales)
5. [Objetivos](#objetivos)
6. [Materiales](#materiales)
7. [Metodología](#metodología)
8. [Resultados](#resultados)
9. [Bibliografía](#Bibliografía)

## Introducción

La señal electrocardiográfica (ECG) refleja la actividad eléctrica del corazón generada por la despolarización y repolarización de las fibras miocárdicas. Este registro no invasivo constituye una herramienta fundamental en el diagnóstico cardiovascular, permitiendo evaluar el ritmo, la conducción eléctrica y la función cardíaca en tiempo real.

El análisis de señales ECG requiere un procesamiento cuidadoso debido a la presencia de artefactos y ruido que pueden interferir con la interpretación clínica. En este laboratorio utilizamos el sistema Bitalino, una plataforma de bajo costo diseñada para la adquisición de bioseñales, combinada con técnicas de procesamiento digital para obtener registros de calidad diagnóstica.

## Formación de la Señal ECG

### Fundamentos Electrofisiológicos

La actividad eléctrica cardíaca se origina en células especializadas que poseen la capacidad de generar y conducir impulsos eléctricos de manera autónoma. El proceso se inicia en el nodo sinoauricular (SA), ubicado en la aurícula derecha, que actúa como el marcapasos fisiológico del corazón.

### Ciclo Cardíaco y Ondas Características

Cada ciclo cardíaco produce un patrón eléctrico característico que se refleja en el ECG:

- **Onda P**: Representa la despolarización auricular. Su duración normal es menor a 120 ms y su amplitud no debe exceder 2.5 mV en las derivaciones de miembros.

- **Complejo QRS**: Refleja la despolarización ventricular. Su duración normal oscila entre 80-120 ms. La onda Q es la primera deflexión negativa, la onda R es la primera deflexión positiva, y la onda S es la deflexión negativa posterior a R.

- **Onda T**: Representa la repolarización ventricular. Su morfología y polaridad proporcionan información sobre la recuperación eléctrica del miocardio ventricular.

<div align="center">

![Onda PQRST](https://lamochiladelresi.wordpress.com/wp-content/uploads/2018/05/captura-de-pantalla-2017-10-11-a-las-9-25-03-p-m.png)

</div>

### Sistema de Derivaciones

El registro electrocardiográfico se obtiene mediante electrodos colocados en posiciones específicas del cuerpo, generando diferentes derivaciones que representan distintas "miradas" de la actividad eléctrica cardíaca:

**Derivaciones de Miembros (Plano Frontal):**
- Bipolares: I, II, III
- Unipolares aumentadas: aVR, aVL, aVF

**Derivaciones Precordiales (Plano Horizontal):**
- V1 a V6: Colocadas en posiciones específicas sobre el tórax

Esta configuración permite una evaluación tridimensional de la actividad eléctrica cardíaca, facilitando la localización de alteraciones regionales del miocardio.

## Bitalino para Adquisición de ECG

### Características del Sistema Bitalino

Bitalino es una plataforma de hardware y software diseñada específicamente para la adquisición de bioseñales. Sus características principales incluyen:

- **Conectividad Bluetooth**: Permite transmisión inalámbrica de datos hasta 10 metros de distancia
- **Frecuencia de muestreo**: Configurable hasta 1000 Hz para ECG
- **Resolución**: 10 bits (1024 niveles de cuantización)
- **Canales analógicos**: Hasta 6 canales simultáneos
- **Alimentación**: Batería de litio recargable de 3.7V

### Configuración para ECG

Para la adquisición de señales ECG con Bitalino se requiere:

1. **Configuración del canal ECG**: Activar el canal analógico específico para ECG
2. **Frecuencia de muestreo**: 1000 Hz (recomendada para análisis detallado)
3. **Ganancia**: Ajustada automáticamente por el amplificador integrado
4. **Colocación de electrodos**: Configuración bipolar usando tres electrodos
   - Electrodo positivo: Muñeca izquierda o región precordial
   - Electrodo negativo: Muñeca derecha
   - Electrodo de referencia (tierra): Tobillo derecho o zona neutra

### Ventajas del Sistema Bitalino

- **Portabilidad**: Diseño compacto que facilita mediciones en diferentes entornos
- **Costo-efectividad**: Alternativa accesible para investigación y educación
- **Facilidad de uso**: Interfaz intuitiva con el software OpenSignals
- **Versatilidad**: Capacidad para adquirir múltiples bioseñales simultáneamente

## Procesamiento y Filtrado de Señales

### Necesidad del Filtrado

Las señales ECG adquiridas contienen diversos tipos de ruido y artefactos que pueden interferir con el análisis:

- **Ruido de línea de potencia**: Interferencia de 50/60 Hz de la red eléctrica
- **Deriva de línea base**: Variaciones lentas debido a respiración y movimientos
- **Ruido muscular (EMG)**: Artefactos de alta frecuencia por actividad muscular
- **Artefactos de movimiento**: Distorsiones causadas por movimientos del sujeto

### Filtros Implementados

#### 1. Filtro Pasa-Alto (HPF) - 0.5 Hz

**Propósito**: Eliminación de la deriva de línea base y componentes de muy baja frecuencia.

**Características**:
- Frecuencia de corte: 0.5 Hz
- Tipo: Butterworth de 2° orden
- Respuesta: Preserva las componentes de frecuencia relevantes del ECG (>0.5 Hz)

**Justificación**: Las componentes útiles del ECG se encuentran principalmente entre 0.5-40 Hz. El filtro pasa-alto elimina derivas lentas causadas por respiración y movimientos del paciente sin afectar la morfología de las ondas P, QRS y T.

#### 2. Filtro Pasa-Bajo (LPF) - 130 Hz

**Propósito**: Eliminación del ruido de alta frecuencia y artefactos musculares.

**Características**:
- Frecuencia de corte: 130 Hz
- Tipo: Butterworth de 4° orden
- Respuesta: Permite el paso de componentes espectrales del ECG mientras elimina ruido de alta frecuencia

**Justificación**: Aunque la mayor energía del ECG se concentra por debajo de 40 Hz, componentes hasta 130 Hz pueden contener información clínicamente relevante, especialmente en el análisis de arritmias y conducción intraventricular.

#### 3. Filtro Notch - 60 Hz

**Propósito**: Eliminación específica de la interferencia de la red eléctrica.

**Características**:
- Frecuencia central: 60 Hz (50 Hz en sistemas europeos)
- Ancho de banda: ±1 Hz (Q = 30)
- Tipo: Filtro rechaza-banda (notch) de 2° orden

**Justificación**: La interferencia de 60 Hz es ubicua en entornos clínicos y de laboratorio. Este filtro elimina específicamente esta interferencia sin afectar significativamente las componentes adyacentes del ECG.

### Cadena de Procesamiento

La señal ECG se procesa secuencialmente:

1. **Filtro Pasa-Alto (0.5 Hz)**: Eliminación de deriva de línea base
2. **Filtro Pasa-Bajo (130 Hz)**: Eliminación de ruido de alta frecuencia
3. **Filtro Notch (60 Hz)**: Eliminación de interferencia de red eléctrica
4. **Normalización**: Ajuste de amplitud para análisis posterior

## Objetivos

- Adquirir señales ECG de calidad utilizando el sistema Bitalino en diferentes condiciones fisiológicas
- Implementar y evaluar técnicas de filtrado digital para mejorar la calidad de la señal
- Analizar las variaciones electrocardiográficas asociadas con diferentes estados metabólicos y respiratorios
- Correlacionar los hallazgos electrocardiográficos con los mecanismos fisiológicos subyacentes

## Materiales

- Sistema Bitalino con módulo ECG
- Computadora con conectividad Bluetooth y software OpenSignals instalado
- Tres electrodos desechables con gel conductor
- Cables de conexión para ECG
- Cronómetro
- Cámara para documentación

## Metodología

### Preparación del Sujeto

1. **Limpieza de la piel**: Aplicar alcohol isopropílico en las zonas de colocación de electrodos
2. **Colocación de electrodos**:
   - Electrodo positivo: Muñeca izquierda (Lead I) o precordial V1
   - Electrodo negativo: Muñeca derecha
   - Electrodo de referencia: Tobillo derecho o zona neutra
3. **Verificación de impedancia**: Confirmar buena conductividad (<10 kΩ)

### Protocolo de Adquisición

1. **Calibración del sistema**: Verificar ganancia y offset
2. **Registro basal**: 5 minutos en reposo supino
3. **Maniobra de apnea**: 30-60 segundos manteniendo la respiración
4. **Período de recuperación**: 2 minutos post-apnea
5. **Ejercicio físico**: 2 minutos de actividad física moderada
6. **Recuperación post-ejercicio**: 5 minutos de monitoreo continuo

### Condiciones de Registro

- Ambiente silencioso y con temperatura controlada
- Minimización de fuentes de interferencia electromagnética
- Sujeto relajado y en posición cómoda
- Registro continuo con anotación de eventos

## Resultados

### Análisis en Reposo

<div align="center">

<a href="https://www.youtube.com/watch?v=xW7y7veXIAQ"><img src="https://img.youtube.com/vi/xW7y7veXIAQ/0.jpg" width="250" height="140"></a>

</div>

**Características esperadas del ECG en reposo:**

- **Ritmo sinusal normal**: Originado en el nodo sinoauricular, con regularidad en los intervalos R-R
- **Morfología de ondas**: 
  - Onda P: Duración <120 ms, amplitud <2.5 mV
  - Complejo QRS: Duración 80-120 ms, morfología característica
  - Onda T: Polaridad concordante con QRS
- **Intervalos**:
  - PR: 120-200 ms
  - QT: Corregido según frecuencia cardíaca (QTc <440 ms en hombres, <460 ms en mujeres)
- **Artefactos mínimos**: Debido a la ausencia de movimiento y respiración regular

### Plot ECG Basal
![Plot ECG basal](/Otros/ECG%20basal.png)

### Conteo de picos R y cálculo BPM
![BPM Basal](/Otros/Conteo%20Basal.png)

### Maniobra de Apnea (Mantenimiento de Respiración)

**Respuesta fisiológica durante la apnea:**

- **Fase inicial (0-15 segundos)**: 
  - Ligera bradicardia por estimulación vagal
  - Mantenimiento de la morfología normal de ondas
- **Fase intermedia (15-45 segundos)**:
  - Variabilidad en la amplitud de ondas R
  - Posibles cambios sutiles en frecuencia cardíaca
  - Activación del reflejo de buceo (dive reflex)
- **Fase tardía (>45 segundos)**:
  - Si se acompaña de maniobra de Valsalva: cambios más marcados
  - Variaciones en la morfología por cambios en el retorno venoso

### Plot ECG manteniendo la respiración
![Plot ECG resp](/Otros/ECG%20Apnea.png)

### Conteo de picos R y cálculo BPM
![BPM resp](/Otros/Conteo%20Apnea.png)

### Actividad Física Inmediata

<div align="center">

<a href="https://www.youtube.com/watch?v=9ZFO6JZfvcw"><img src="https://img.youtube.com/vi/9ZFO6JZfvcw/0.jpg" width="250" height="140"></a>

</div>

**Adaptaciones electrocardiográficas al ejercicio:**

- **Taquicardia fisiológica**: Frecuencia cardíaca >100 lpm, proporcional a la intensidad del ejercicio
- **Acortamiento de intervalos**:
  - Intervalo R-R reducido (reflejando aceleración)
  - Intervalo PR ligeramente acortado
  - QT dinámicamente adaptado (QTc puede mantenerse normal)
- **Cambios morfológicos**:
  - Onda T más prominente por repolarización acelerada
  - Posible aumento de amplitud de QRS por incremento del gasto cardíaco
- **Artefactos de movimiento**: Mayor presencia si el registro no se realiza en reposo post-ejercicio
- **Recuperación**: Patrón de desaceleración gradual en los minutos posteriores

### Plot ECG agitado
![Plot ECG agitado](/Otros/ECG%20Agitado.png)

### Conteo de picos R y cálculo BPM
![BPM Agitado](/Otros/Conteo%20Agitado.png)

### Análisis Comparativo

**Variabilidad de frecuencia cardíaca:**
- Reposo: Baja variabilidad, ritmo regular
- Apnea: Variabilidad inicial seguida de estabilización
- Post-ejercicio: Alta variabilidad durante recuperación

**Activación del sistema nervioso autónomo:**
- Reposo: Equilibrio simpático-parasimpático
- Apnea: Predominio vagal inicial
- Ejercicio: Activación simpática marcada

**Calidad de la señal:**
- Mejor calidad en reposo
- Posibles artefactos durante maniobras respiratorias
- Artefactos de movimiento post-ejercicio

## Bibliografía

#### [1] J. Malmivuo and R. Plonsey, Bioelectromagnetism: Principles and Applications of Bioelectric and Biomagnetic Fields. Oxford, U.K.: Oxford Univ. Press, 1995, ch. 15, pp. 308–342.
#### [2] D. Batista, H. Silva, A. Fred, C. Moreira, M. Reis, and H. A. Ferreira, “Benchmarking of the BITalino biomedical toolkit against an established gold standard,” Healthcare Technology Letters, vol. 6, no. 2, pp. 32–36, 2019, doi: 10.1049/htl.2018.5037.
#### [3] H. P. da Silva, J. Guerreiro, A. Lourenço, A. L. Fred, and R. Martins, “BITalino: A novel hardware framework for physiological computing,” in Proc. Int. Conf. Physiological Computing Systems, 2014, pp. 246–253, doi: 10.5220/0004727802460253.
#### [4] L. Sörnmo and P. Laguna, Bioelectrical Signal Processing in Cardiac and Neurological Applications. Burlington, MA, USA: Academic Press, 2005, ch. 3, pp. 453–566.
#### [5] G. D. Clifford, F. Azuaje, and P. E. McSharry, Advanced Methods and Tools for ECG Data Analysis. Boston, MA, USA: Artech House, 2006, ch. 2, pp. 55–99.
#### [6] Task Force of the European Society of Cardiology and the North American Society of Pacing and Electrophysiology, “Heart rate variability: Standards of measurement, physiological interpretation and clinical use,” Circulation, vol. 93, no. 5, pp. 1043–1065, 1996, doi: 10.1161/01.CIR.93.5.1043.

### Contribución:
##### - Leon Achata 33.33%
##### - Nicolas Arango 33.33%
##### - Hans Navarro 33.33%
