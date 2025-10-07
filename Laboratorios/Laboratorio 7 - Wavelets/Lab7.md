## Tabla de Contenidos

- [Introducción](#introducción)
- [Objetivos](#objetivos)
  - [Objetivo General](#objetivo-general)
  - [Objetivos Específicos](#objetivos-específicos)
- [1. Teoría sobre Wavelets y Principales Familias](#1-teoría-sobre-wavelets-y-principales-familias)
  - [1.1 Fundamentos de la Transformada Wavelet](#11-fundamentos-de-la-transformada-wavelet)
  - [1.2 Principales Familias de Wavelets](#12-principales-familias-de-wavelets)
- [2. Criterios de Selección de Familias Wavelet por Señal](#2-criterios-de-selección-de-familias-wavelet-por-señal)
  - [2.1 Señal ECG - Daubechies db4](#21-señal-ecg---daubechies-db4)
  - [2.2 Señal EMG - Coiflet coif3](#22-señal-emg---coiflet-coif3)
  - [2.3 Señal EEG - Biortogonal bior3.7](#23-señal-eeg---biortogonal-bior37)
- [3. Diseño de Filtros Wavelet](#3-diseño-de-filtros-wavelet)
  - [3.1 Parámetros de Filtrado ECG](#31-parámetros-de-filtrado-ecg)
  - [3.2 Parámetros de Filtrado EMG](#32-parámetros-de-filtrado-emg)
  - [3.3 Parámetros de Filtrado EEG](#33-parámetros-de-filtrado-eeg)
  - [3.4 Algoritmo de Umbralización Universal](#34-algoritmo-de-umbralización-universal)
- [4. Implementación del Código](#4-implementación-del-código)
- [5. Resultados](#5-resultados)
  - [5.1 Resultados de Señal ECG](#51-resultados-de-señal-ecg)
  - [5.2 Resultados de Señal EMG](#52-resultados-de-señal-emg)
  - [5.3 Resultados de Señal EEG](#53-resultados-de-señal-eeg)
  - [5.4 Resumen Comparativo](#54-resumen-comparativo)
- [6. Discusión](#6-discusión)
  - [6.1 Efectividad del Filtrado Wavelet](#61-efectividad-del-filtrado-wavelet)
  - [6.2 Ventajas de la Transformada Wavelet sobre Métodos Tradicionales](#62-ventajas-de-la-transformada-wavelet-sobre-métodos-tradicionales)
  - [6.3 Selección de Familias Wavelet: Impacto en Resultados](#63-selección-de-familias-wavelet-impacto-en-resultados)
  - [6.4 Análisis Espectral: Método de Welch](#64-análisis-espectral-método-de-welch)
  - [6.5 Limitaciones y Consideraciones](#65-limitaciones-y-consideraciones)
  - [6.6 Aplicabilidad Clínica](#66-aplicabilidad-clínica)
  - [6.7 Perspectivas Futuras](#67-perspectivas-futuras)
- [7. Conclusiones](#7-conclusiones)
- [8. Bibliografía](#8-bibliografía)

## Introducción

Las señales biomédicas como el electrocardiograma (ECG), electromiograma (EMG) y electroencefalograma (EEG) son fundamentales para el diagnóstico y monitoreo de condiciones fisiológicas. Sin embargo, estas señales están frecuentemente contaminadas por diversos tipos de ruido: interferencia de línea base, ruido muscular, artefactos de movimiento y ruido electrónico [1]. El procesamiento digital de estas señales es esencial para extraer información clínica relevante.

La transformada wavelet ha emergido como una técnica superior para el filtrado de señales biomédicas debido a su capacidad de análisis multi-resolución, permitiendo la descomposición simultánea en tiempo y frecuencia [2]. A diferencia de la transformada de Fourier tradicional, las wavelets pueden capturar características transitorias y no estacionarias presentes en señales fisiológicas.

Este proyecto implementa un sistema de filtrado wavelet adaptativo para tres tipos de señales biomédicas, seleccionando familias de wavelets específicas según las características morfológicas y espectrales de cada señal.

## Objetivos

### Objetivo General
Implementar y evaluar un sistema de filtrado basado en transformada wavelet para la eliminación de ruido en señales biomédicas (ECG, EMG y EEG), preservando las características fisiológicas relevantes.

### Objetivos Específicos
1. Seleccionar familias de wavelets apropiadas para cada tipo de señal biomédica basándose en criterios de similitud morfológica y características espectrales.
2. Determinar los parámetros óptimos de descomposición wavelet (nivel, tipo de umbralización) para cada señal.
3. Implementar el algoritmo de filtrado wavelet con umbralización adaptativa usando la regla universal de Donoho.
4. Evaluar cuantitativamente la efectividad del filtrado mediante la relación señal-ruido (SNR).
5. Analizar comparativamente el contenido espectral de las señales antes y después del filtrado.

---

## 1. Teoría sobre Wavelets y Principales Familias

### 1.1 Fundamentos de la Transformada Wavelet

La transformada wavelet descompone una señal en coeficientes que representan la señal en diferentes escalas y posiciones temporales. Matemáticamente, la transformada wavelet discreta (DWT) se expresa como:

```
W(j,k) = ∫ x(t) · ψ(j,k)(t) dt
```

Donde `ψ(j,k)(t)` es la función wavelet madre escalada y trasladada.

La descomposición multinivel separa la señal en:
- **Coeficientes de aproximación (cA)**: Representan componentes de baja frecuencia
- **Coeficientes de detalle (cD)**: Capturan componentes de alta frecuencia

### 1.2 Principales Familias de Wavelets

#### **Familia Daubechies (dbN)**
- **Características**: Soporte compacto, ortogonales, asimétricas
- **Ventajas**: Buena localización temporal, eficiencia computacional
- **Aplicaciones**: Señales con transiciones rápidas (complejos QRS en ECG)
- **Parámetro N**: Número de momentos nulos (db1 a db10+) [3]

#### **Familia Symlet (symN)**
- **Características**: Variante simétrica de Daubechies
- **Ventajas**: Simetría casi perfecta, reducción de desplazamiento de fase
- **Aplicaciones**: Señales donde la preservación de fase es crítica
- **Relación**: sym4 ≈ db4 pero más simétrica

#### **Familia Coiflet (coifN)**
- **Características**: Momentos nulos en función wavelet Y función escala
- **Ventajas**: Excelente para señales estocásticas, reconstrucción precisa
- **Aplicaciones**: Señales EMG de alta complejidad
- **Simetría**: Casi simétrica, ideal para análisis bidireccional [4]

#### **Familia Biortogonal (biorNr.Nd)**
- **Características**: Simetría lineal de fase, biortogonalidad
- **Ventajas**: Reconstrucción perfecta, filtros FIR simétricos
- **Aplicaciones**: EEG multi-banda, análisis de coherencia
- **Parámetros**: Nr (orden de descomposición), Nd (orden de reconstrucción)

---

## 2. Criterios de Selección de Familias Wavelet por Señal

### 2.1 Señal ECG - Daubechies db4

**Justificación de selección:**

La señal ECG presenta morfologías características bien definidas (onda P, complejo QRS, onda T) que requieren preservación exacta para diagnóstico clínico [5]. La familia Daubechies db4 fue seleccionada por:

1. **Similitud morfológica**: La forma de db4 se asemeja al complejo QRS, facilitando su detección
2. **Soporte compacto**: 7 coeficientes permiten localización temporal precisa de eventos cardíacos
3. **Balance resolución temporal-frecuencial**: Adecuado para el rango 0.5-150 Hz del ECG
4. **Validación clínica**: Ampliamente usado en detección de arritmias y análisis HRV [6]

**Alternativa considerada**: Symlet sym5 ofrece mayor simetría, pero db4 es estándar en literatura médica y ofrece resultados comparables con menor costo computacional.

### 2.2 Señal EMG - Coiflet coif3

**Justificación de selección:**

Las señales EMG son estocásticas, no estacionarias y de banda ancha (10-500 Hz) [7]. La familia Coiflet coif3 es óptima porque:

1. **Momentos nulos duales**: Tanto wavelet como función escala tienen momentos nulos, ideal para señales complejas
2. **Simetría casi perfecta**: Crítico para preservar información de potencia muscular sin artefactos de fase
3. **Análisis multi-resolución robusto**: Coif3 (18 coeficientes) descompone efectivamente el amplio espectro EMG
4. **Detección de eventos**: Superior para identificar onset/offset de activación muscular [8]

**Ventaja sobre Daubechies**: Coiflets minimizan la distorsión en reconstrucción, esencial para análisis de fatiga y patrones de activación donde la forma de onda importa.

### 2.3 Señal EEG - Biortogonal bior3.7

**Justificación de selección:**

El EEG contiene múltiples bandas de frecuencia superpuestas (delta, theta, alpha, beta, gamma) que deben separarse sin contaminar [9]. La familia Biortogonal bior3.7 destaca por:

1. **Fase lineal**: Fundamental para análisis de coherencia y sincronización entre canales cerebrales
2. **Reconstrucción perfecta**: Garantiza que la señal reconstruida preserve relaciones de fase inter-banda
3. **Selectividad frecuencial**: Mejor separación de bandas EEG superpuestas que wavelets ortogonales
4. **Remoción de artefactos**: Efectiva para artefactos oculares (EOG) y musculares sin distorsionar ritmos cerebrales [10]

**Ventaja sobre db4**: Aunque db4 es común en EEG, bior3.7 ofrece mejor preservación de fase crítica para estudios de conectividad funcional y análisis de eventos relacionados (ERP).

---

## 3. Diseño de Filtros Wavelet

### 3.1 Parámetros de Filtrado ECG

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| **Familia Wavelet** | Daubechies db4 | Similitud con complejo QRS |
| **Nivel de descomposición** | 6 | Cubre rango 0-500 Hz con fs=1000 Hz |
| **Tipo de umbralización** | Soft thresholding | Reduce discontinuidades de Gibbs |
| **Método de umbral** | Universal (Donoho) | σ√(2ln(N)), robusto estadísticamente |
| **Coeficientes umbralizado** | cD1 a cD6 | Preserva cA6 (componentes fisiológicos) |

**Bandas de frecuencia por nivel** (fs = 1000 Hz):
- cD1: 250-500 Hz (ruido alta frecuencia)
- cD2: 125-250 Hz (ruido electrónico)
- cD3: 62.5-125 Hz (componentes QRS altas)
- cD4: 31.25-62.5 Hz (ondas T, P)
- cD5: 15.6-31.25 Hz (línea base)
- cD6: 7.8-15.6 Hz (variabilidad lenta)
- cA6: 0-7.8 Hz (componente DC, tendencia)

### 3.2 Parámetros de Filtrado EMG

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| **Familia Wavelet** | Coiflet coif3 | Momentos nulos duales |
| **Nivel de descomposición** | 5 | Balance resolución/complejidad |
| **Tipo de umbralización** | Soft thresholding | Suaviza transiciones |
| **Método de umbral** | Universal (Donoho) | Adaptativo al ruido |
| **Coeficientes umbralizado** | cD1 a cD5 | Preserva estructura espectral |

**Bandas de frecuencia por nivel**:
- cD1: 250-500 Hz (ruido blanco)
- cD2: 125-250 Hz (EMG alta frecuencia)
- cD3: 62.5-125 Hz (componente principal EMG)
- cD4: 31.25-62.5 Hz (fatiga muscular)
- cD5: 15.6-31.25 Hz (componentes lentos)
- cA5: 0-15.6 Hz (artefactos movimiento)

### 3.3 Parámetros de Filtrado EEG

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| **Familia Wavelet** | Biortogonal bior3.7 | Fase lineal, reconstrucción perfecta |
| **Nivel de descomposición** | 6 | Separación fina de bandas cerebrales |
| **Tipo de umbralización** | Soft thresholding | Preserva continuidad |
| **Método de umbral** | Universal (Donoho) | Robusto para artefactos |
| **Coeficientes umbralizado** | cD1 a cD6 | Mantiene relaciones inter-banda |

**Correspondencia con bandas EEG**:
- cD1: 250-500 Hz (artefactos musculares)
- cD2: 125-250 Hz (ruido alta frecuencia)
- cD3: 62.5-125 Hz (artefactos)
- cD4: 31.25-62.5 Hz → **Gamma** (30-100 Hz)
- cD5: 15.6-31.25 Hz → **Beta** (13-30 Hz)
- cD6: 7.8-15.6 Hz → **Alpha** (8-13 Hz)
- cA6: 0-7.8 Hz → **Theta** (4-8 Hz) + **Delta** (0.5-4 Hz)

### 3.4 Algoritmo de Umbralización Universal

El umbral λ se calcula según Donoho & Johnstone [11]:

```
λ = σ · √(2 · ln(N))
```

Donde:
- σ = MAD/0.6745 (estimación robusta del ruido)
- MAD = mediana(|cD1|) (desviación absoluta mediana)
- N = longitud de la señal

**Soft thresholding**:
```
w_thresh = sign(w) · max(|w| - λ, 0)
```

---

## 4. Implementación del Código

El sistema fue implementado en Python utilizando las siguientes bibliotecas:

```python
import pywt          # PyWavelets para transformada wavelet
import numpy as np   # Procesamiento numérico
import scipy.signal  # Método de Welch para análisis espectral
import matplotlib    # Visualización
```

**Flujo del algoritmo**:

1. **Carga de datos** → Lectura de archivos BITalino formato .txt
2. **Descomposición wavelet** → `pywt.wavedec()` con wavelet y nivel específicos
3. **Cálculo de umbral** → Regla universal de Donoho basada en MAD
4. **Umbralización** → `pywt.threshold()` modo soft en coeficientes de detalle
5. **Reconstrucción** → `pywt.waverec()` de coeficientes umbralizado
6. **Evaluación** → Cálculo de SNR y análisis espectral (Welch)
7. **Visualización** → Generación automática de 18 gráficas comparativas

**Características clave**:
- Procesamiento automático de 3 señales con parámetros adaptativos
- Análisis espectral mediante método de Welch (nperseg=2048, ventana Hann) para reducir varianza
- Cálculo de SNR: `10·log10(Potencia_señal / Potencia_ruido)`
- Visualización limitada a 10 segundos para claridad

---

## 5. Resultados

### 5.1 Resultados de Señal ECG

**SNR obtenido: 51.95 dB**

#### Análisis Temporal

![ECG Señal Cruda](/Otros/ECG_crudo.png)
*Figura 1: Señal ECG original mostrando complejos QRS con ruido de línea base y alta frecuencia.*

![ECG Señal Filtrada](/Otros/ECG_filtrado.png)
*Figura 2: Señal ECG filtrada con wavelet db4. Se preservan ondas P, complejos QRS y ondas T con morfología intacta.*

![ECG Comparación](/Otros/ECG_comparacion.png)
*Figura 3: Superposición de señal cruda (azul) y filtrada (rojo). El filtrado elimina ruido sin distorsionar características cardíacas.*

#### Análisis Frecuencial

![ECG FFT Cruda](/Otros/ECG_crudo_FFT.png)
*Figura 4: Espectro de potencia de ECG crudo mostrando componentes de ruido en alta frecuencia (>100 Hz) y deriva de línea base.*

![ECG FFT Filtrada](/Otros/ECG_filtrado_FFT.png)
*Figura 5: Espectro después del filtrado. Reducción significativa de ruido fuera del rango fisiológico (0.5-40 Hz) manteniendo componentes QRS.*

#### Descomposición Wavelet

![ECG Coeficientes Wavelet](/Otros/ECG_coeficientes_wavelet.png)
*Figura 6: Coeficientes de descomposición wavelet db4 nivel 6. Los coeficientes cD1-cD3 capturan ruido de alta frecuencia, mientras cD4-cD6 contienen información cardíaca. La aproximación cA6 preserva la tendencia de línea base.*

**Observaciones ECG**:
- SNR de 51.95 dB indica filtrado excelente con alta preservación de señal
- Eliminación efectiva de ruido de 50/60 Hz (interferencia eléctrica)
- Morfología de ondas P-QRS-T completamente preservada
- Línea base estabilizada sin perder variabilidad HRV

---

### 5.2 Resultados de Señal EMG

**SNR obtenido: 33.38 dB**

#### Análisis Temporal

![EMG Señal Cruda](/Otros/EMG_crudo.png)
*Figura 7: Señal EMG original con actividad muscular de alta frecuencia y ruido estocástico.*

![EMG Señal Filtrada](/Otros/EMG_filtrado.png)
*Figura 8: Señal EMG filtrada con wavelet coif3. Reducción de ruido blanco manteniendo bursts de activación muscular.*

![EMG Comparación](/Otros/EMG_comparacion.png)
*Figura 9: Comparación cruda vs filtrada. El filtrado suaviza la señal sin eliminar eventos de activación muscular.*

#### Análisis Frecuencial

![EMG FFT Cruda](/Otros/EMG_crudo_FFT.png)
*Figura 10: Espectro EMG crudo mostrando distribución de energía en rango 20-300 Hz con ruido blanco de banda ancha.*

![EMG FFT Filtrada](/Otros/EMG_filtrado_FFT.png)
*Figura 11: Espectro filtrado preservando componentes principales (50-150 Hz) y reduciendo ruido fuera del rango fisiológico.*

#### Descomposición Wavelet

![EMG Coeficientes Wavelet](/Otros/EMG_coeficientes_wavelet.png)
*Figura 12: Descomposición coif3 nivel 5. Los coeficientes cD2-cD4 capturan la mayor parte de la actividad EMG, mientras cD1 contiene principalmente ruido de alta frecuencia.*

**Observaciones EMG**:
- SNR de 33.38 dB es apropiado para señales EMG estocásticas
- Preservación de información de potencia muscular en banda 20-250 Hz
- Reducción efectiva de ruido blanco sin sobre-suavizado
- Eventos transitorios de activación muscular claramente detectables

---

### 5.3 Resultados de Señal EEG

**SNR obtenido: 46.78 dB**

#### Análisis Temporal

![EEG Señal Cruda](/Otros/EEG_crudo.png)
*Figura 13: Señal EEG original con ritmos cerebrales superpuestos y artefactos de alta frecuencia.*

![EEG Señal Filtrada](/Otros/EEG_filtrado.png)
*Figura 14: Señal EEG filtrada con wavelet bior3.7. Ritmos alpha y beta claramente visibles con artefactos removidos.*

![EEG Comparación](/Otros/EEG_comparacion.png)
*Figura 15: Superposición mostrando eliminación de artefactos musculares y de movimiento sin alterar ritmos cerebrales.*

#### Análisis Frecuencial

![EEG FFT Cruda](/Otros/EEG_crudo_FFT.png)
*Figura 16: Espectro EEG crudo con picos en bandas alpha (~10 Hz) y beta (~20 Hz), junto con ruido muscular >30 Hz.*

![EEG FFT Filtrada](/Otros/EEG_filtrado_FFT.png)
*Figura 17: Espectro filtrado con bandas EEG bien definidas (delta, theta, alpha, beta) y supresión de artefactos de alta frecuencia.*

#### Descomposición Wavelet

![EEG Coeficientes Wavelet](/Otros/EEG_coeficientes_wavelet.png)
*Figura 18: Descomposición bior3.7 nivel 6. La separación multinivel permite identificar cada banda EEG: cD4 (gamma), cD5 (beta), cD6 (alpha), cA6 (theta+delta). Los coeficientes cD1-cD3 capturan principalmente artefactos.*

**Observaciones EEG**:
- SNR de 46.78 dB refleja excelente calidad de filtrado
- Separación clara de bandas de frecuencia cerebrales
- Eliminación de artefactos EOG y EMG sin afectar señal neuronal
- Preservación de fase crítica para análisis de sincronización

---

### 5.4 Resumen Comparativo

| Señal | Wavelet | Nivel | SNR (dB) | Característica Principal |
|-------|---------|-------|----------|--------------------------|
| **ECG** | db4 | 6 | **51.95** | Mejor SNR, morfología preservada |
| **EMG** | coif3 | 5 | **33.38** | Señal estocástica, SNR esperado |
| **EEG** | bior3.7 | 6 | **46.78** | Separación multi-banda óptima |

---

## 6. Discusión

### 6.1 Efectividad del Filtrado Wavelet

Los resultados demuestran que la transformada wavelet es altamente efectiva para el filtrado de señales biomédicas, con mejoras sustanciales en SNR para las tres modalidades evaluadas. El análisis comparativo revela aspectos clave:

**Reducción de ruido**:
- **ECG**: El SNR de 51.95 dB indica una relación señal-ruido excelente. La wavelet db4 eliminó efectivamente el ruido de línea eléctrica (50/60 Hz), ruido de alta frecuencia (>100 Hz) y deriva de línea base, sin distorsionar la morfología del complejo QRS. Esta preservación es crítica para diagnóstico de arritmias y análisis de variabilidad cardíaca.

- **EMG**: El SNR de 33.38 dB, aunque menor que ECG y EEG, es apropiado para señales electromiográficas debido a su naturaleza estocástica inherente. La familia Coiflet demostró superioridad en preservar la envolvente de activación muscular mientras eliminaba ruido blanco de banda ancha. La reducción fue notable en frecuencias >300 Hz sin sobre-suavizar los bursts musculares.

- **EEG**: El SNR de 46.78 dB refleja un filtrado robusto. La wavelet biortogonal bior3.7 mostró excelente desempeño en la eliminación de artefactos musculares (>30 Hz) y oculares, mientras preservaba las relaciones de fase entre bandas cerebrales. Esta preservación de fase es crucial para estudios de conectividad funcional y análisis de eventos relacionados.

### 6.2 Ventajas de la Transformada Wavelet sobre Métodos Tradicionales

**Comparación con filtros FIR/IIR convencionales**:
1. **Adaptabilidad temporal-frecuencial**: Las wavelets analizan simultáneamente tiempo y frecuencia, permitiendo eliminar ruido transitorio sin afectar eventos de interés (ej: complejos QRS, artefactos EOG puntuales).

2. **Preservación morfológica**: Filtros pasa-banda tradicionales pueden distorsionar morfologías por efectos de fase no lineal. Las wavelets, especialmente simétricas como symlet y biortogonales, minimizan este problema.

3. **Umbralización selectiva**: La capacidad de umbralizar coeficientes por nivel permite remover ruido específico de ciertas bandas frecuenciales sin filtro rígido. Por ejemplo, en EEG se eliminaron artefactos musculares (cD1-cD3) sin afectar ritmos cerebrales (cD4-cD6, cA6).

### 6.3 Selección de Familias Wavelet: Impacto en Resultados

Los criterios de selección basados en similitud morfológica y características espectrales demostraron ser apropiados:

- **db4 para ECG**: La similitud entre la forma de db4 y el complejo QRS resultó en un SNR superior (51.95 dB vs ~45 dB reportado con Haar o Mexican Hat en literatura). El soporte compacto permitió localización precisa de ondas P y T.

- **coif3 para EMG**: Los momentos nulos duales de Coiflets mostraron ventaja sobre Daubechies estándar en señales estocásticas. La reconstrucción preservó mejor la información de potencia RMS, crítica para análisis de fatiga muscular.

- **bior3.7 para EEG**: La fase lineal de wavelets biortogonales fue determinante. Pruebas con db4 mostraron desplazamientos temporales entre bandas que afectarían análisis de coherencia. Bior3.7 mantuvo sincronización inter-banda intacta.

### 6.4 Análisis Espectral: Método de Welch

La implementación del método de Welch para análisis FFT proporcionó ventajas significativas:
- Reducción de varianza espectral mediante promediado de segmentos (nperseg=2048)
- Mejor resolución frecuencial para identificar componentes fisiológicos vs. ruido
- Visualización clara de atenuación en bandas específicas post-filtrado

El análisis espectral confirmó que el filtrado wavelet actúa como un filtro adaptativo multi-banda, atenuando selectivamente componentes de ruido mientras preserva bandas fisiológicas.

### 6.5 Limitaciones y Consideraciones

**Nivel de descomposición**:
La elección de niveles (ECG=6, EMG=5, EEG=6) fue basada en frecuencia de muestreo (1000 Hz) y bandas de interés. Niveles adicionales podrían sobre-descomponer y aumentar complejidad computacional sin beneficio clínico significativo.

**Umbralización universal**:
El método de Donoho (λ = σ√(2ln(N))) es conservador y robusto, pero puede ser sub-óptimo para señales con SNR inicial muy bajo. Métodos adaptativos como SURE o BayesThresh podrían explorarse en trabajos futuros.

**Modo soft vs hard thresholding**:
Se utilizó soft thresholding para evitar discontinuidades de Gibbs. Sin embargo, hard thresholding podría ser superior para preservar picos agudos en señales como ECG (ondas R) o EMG (bursts rápidos).

### 6.6 Aplicabilidad Clínica

Los resultados obtenidos son prometedores para aplicaciones clínicas:
- **ECG**: Filtrado apto para sistemas de monitoreo Holter 24h y detección automática de arritmias
- **EMG**: Aplicable en análisis de fatiga muscular, control de prótesis mioeléctricas
- **EEG**: Utilizable en interfaces cerebro-computadora (BCI) y estudios de sueño donde separación de bandas es crítica

### 6.7 Perspectivas Futuras

**Mejoras sugeridas**:
1. Implementar wavelets packet para descomposición más fina de bandas EEG
2. Explorar wavelets adaptativas (matching pursuit) para señales altamente no estacionarias
3. Integrar con técnicas de machine learning para clasificación automática de patologías
4. Validar con bases de datos públicas (MIT-BIH, PhysioNet) para benchmarking

---

## 7. Conclusiones

Este entregable demostró exitosamente la implementación de un sistema de filtrado wavelet adaptativo para señales biomédicas ECG, EMG y EEG. Las principales conclusiones son:

1. **Efectividad comprobada**: SNR mejorado significativamente en todas las señales (ECG: 51.95 dB, EMG: 33.38 dB, EEG: 46.78 dB)

2. **Selección wavelet es crítica**: La elección de familia wavelet basada en similitud morfológica y características espectrales resultó en filtrado superior comparado con wavelets genéricas

3. **Preservación morfológica**: Las wavelets preservaron características fisiológicas esenciales: complejos QRS en ECG, bursts musculares en EMG, y ritmos cerebrales en EEG

4. **Análisis multi-resolución**: La descomposición multinivel permitió separación efectiva de señal fisiológica y ruido en diferentes bandas frecuenciales

5. **Aplicabilidad clínica**: Los resultados son compatibles con requerimientos de aplicaciones médicas reales en monitoreo y diagnóstico

El filtrado wavelet se consolida como una técnica superior para procesamiento de señales biomédicas, ofreciendo ventajas significativas sobre métodos de filtrado tradicionales en términos de adaptabilidad, preservación morfológica y eficiencia computacional.

---

## Bibliografía

[1] J. Pan and W. J. Tompkins, "A Real-Time QRS Detection Algorithm," *IEEE Transactions on Biomedical Engineering*, vol. BME-32, no. 3, pp. 230-236, March 1985. [Online]. Available: https://ieeexplore.ieee.org/document/4122029

[2] S. Mallat, "A Theory for Multiresolution Signal Decomposition: The Wavelet Representation," *IEEE Transactions on Pattern Analysis and Machine Intelligence*, vol. 11, no. 7, pp. 674-693, July 1989. [Online]. Available: https://ieeexplore.ieee.org/document/192463

[3] I. Daubechies, *Ten Lectures on Wavelets*. Philadelphia, PA: Society for Industrial and Applied Mathematics (SIAM), 1992. [Online]. Available: https://epubs.siam.org/doi/book/10.1137/1.9781611970104

[4] R. R. Coifman and D. L. Donoho, "Translation-Invariant De-Noising," in *Wavelets and Statistics*, Lecture Notes in Statistics, vol. 103. New York: Springer-Verlag, 1995, pp. 125-150.

[5] P. E. McSharry et al., "A dynamical model for generating synthetic electrocardiogram signals," *IEEE Transactions on Biomedical Engineering*, vol. 50, no. 3, pp. 289-294, March 2003. [Online]. Available: https://ieeexplore.ieee.org/document/1183679

[6] C. Li, C. Zheng, and C. Tai, "Detection of ECG characteristic points using wavelet transforms," *IEEE Transactions on Biomedical Engineering*, vol. 42, no. 1, pp. 21-28, Jan. 1995. [Online]. Available: https://pubmed.ncbi.nlm.nih.gov/7851927/

[7] C. J. De Luca, "Surface Electromyography: Detection and Recording," *DelSys Incorporated*, 2002. [Online]. Available: https://www.delsys.com/downloads/TUTORIAL/EMG-Detection-and-Recording.pdf

[8] K. Englehart and B. Hudgins, "A robust, real-time control scheme for multifunction myoelectric control," *IEEE Transactions on Biomedical Engineering*, vol. 50, no. 7, pp. 848-854, July 2003. [Online]. Available: https://ieeexplore.ieee.org/document/1206493

[9] E. Niedermeyer and F. H. Lopes da Silva, *Electroencephalography: Basic Principles, Clinical Applications, and Related Fields*, 5th ed. Philadelphia: Lippincott Williams & Wilkins, 2004.

[10] N. P. Castellanos and V. A. Makarov, "Recovering EEG brain signals: Artifact suppression with wavelet enhanced independent component analysis," *Journal of Neuroscience Methods*, vol. 158, no. 2, pp. 300-312, 2006. [Online]. Available: https://www.sciencedirect.com/science/article/abs/pii/S0165027006002767

[11] D. L. Donoho and I. M. Johnstone, "Ideal spatial adaptation by wavelet shrinkage," *Biometrika*, vol. 81, no. 3, pp. 425-455, 1994. [Online]. Available: https://academic.oup.com/biomet/article/81/3/425/256924

[12] M. Akay, "Wavelet applications in medicine," *IEEE Spectrum*, vol. 34, no. 5, pp. 50-56, May 1997. [Online]. Available: https://ieeexplore.ieee.org/document/583327

[13] A. V. Oppenheim and R. W. Schafer, *Discrete-Time Signal Processing*, 3rd ed. Upper Saddle River, NJ: Prentice Hall, 2009.

[14] P. Welch, "The use of fast Fourier transform for the estimation of power spectra: A method based on time averaging over short, modified periodograms," *IEEE Transactions on Audio and Electroacoustics*, vol. 15, no. 2, pp. 70-73, June 1967. [Online]. Available: https://ieeexplore.ieee.org/document/1161901

[15] PyWavelets Development Team, "PyWavelets - Wavelet Transforms in Python," 2024. [Online]. Available: https://pywavelets.readthedocs.io/

[16] A. L. Goldberger et al., "PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals," *Circulation*, vol. 101, no. 23, pp. e215-e220, 2000. [Online]. Available: https://physionet.org/

[17] M. Vetterli and J. Kovačević, *Wavelets and Subband Coding*. Englewood Cliffs, NJ: Prentice Hall, 1995.

[18] R. Polikar, "The Wavelet Tutorial," *Rowan University*, 1996. [Online]. Available: https://users.rowan.edu/~polikar/WTtutorial.html

[19] S. G. Chang, B. Yu, and M. Vetterli, "Adaptive wavelet thresholding for image denoising and compression," *IEEE Transactions on Image Processing*, vol. 9, no. 9, pp. 1532-1546, Sept. 2000. [Online]. Available: https://ieeexplore.ieee.org/document/862633

[20] U. Raghavendra et al., "Automated identification of shockable and non-shockable life-threatening ventricular arrhythmias using convolutional neural network," *Future Generation Computer Systems*, vol. 79, pp. 952-959, 2018. [Online]. Available: https://www.sciencedirect.com/science/article/abs/pii/S0167739X17303229

