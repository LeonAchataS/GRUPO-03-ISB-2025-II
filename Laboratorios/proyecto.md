# Temática del proyecto

## Título tentativo
"Interfaz Cerebro-Computadora para el control de dispositivos mediante detección en tiempo real de imaginación motora"

## Problemática a abordar
<div align="justify">
Las personas con discapacidades motoras severas, como aquellas que presentan parálisis por lesiones medulares o enfermedades neuromusculares, enfrentan grandes limitaciones para interactuar con dispositivos electrónicos y realizar tareas básicas de la vida diaria. Los sistemas de control convencionales (botones, pantallas táctiles, controles manuales) no son accesibles para todos y, en algunos casos, las lesiones son tan graves que los pacientes no pueden, incluso, mover sus extremidades como las manos o pies.
Entonces se necesita un método no invasivo, económico y en tiempo real que permita a estos pacientes controlar dispositivos básicos a través de señales cerebrales, sin depender del movimiento muscular residual.

Según la Organización Mundial de la Salud (OMS), en 2021 había más de 15 millones de personas con lesiones medulares en el mundo [1]. A nivel Perú, entre enero y mayo del 2024, el Instituto Nacional de Rehabilitación (INR) reportó más de 1500 atenciones por lesión medular [2]. Estas cifras reflejan la urgencia de desarrollar soluciones tecnológicas que mejoren la calidad de vida de estos pacientes.
</div>

## Propuesta de solución
### Detección de intención o acción motora mediante EEG utilizando BCI
<div align="justify">
El proyecto propone utilizar electroencefalografía (EEG) para detectar imaginación motora; es decir, la actividad cerebral asociada a pensar en abrir o cerrar la mano derecha, la mano izquierda, ambas manos o los pies, sin realizar realmente el movimiento.

La señal EEG será procesada y clasificada en tiempo real mediante algoritmos de procesamiento digital y técnicas de machine learning para mapear cada clase de imaginación motora a una acción de control, como encender o apagar una luz, mover un cursor, o accionar un dispositivo simple.[3]
</div>

### Interfaz cerebro-computadora 
Una interfaz cerebro-computadora (BCI) es un sistema que permite traducir la actividad cerebral en comandos para controlar dispositivos externos sin necesidad de movimientos musculares.

En este proyecto:

+ Se emplearán electrodos EEG ubicados en regiones motoras (C3, Cz, C4) que captan ritmos sensorimotor mu (8–12 Hz) y beta (13–30 Hz), los cuales cambian su potencia cuando el usuario imagina movimientos de extremidades.[4]
+ Se aplicará un preprocesamiento de señales (filtrado, normalización, eliminación de artefactos) para extraer características relevantes.
+ La clasificación en tiempo real permitirá mapear la imaginación de abrir/cerrar extremidades a comandos específicos.


## Objetivos a alcanzar

+ Implementar un programa capaz de detectar y clasificar la imaginación motora en tiempo real utilizando EEG.
+ Realizar un proceso de filtrado y extracción de características adecuado (por ejemplo, CSP, FFT, o PSD) para identificar patrones de imaginación motora.
+ Validar los algoritmos utilizando bases de datos abiertas de EEG, sin necesidad de desarrollar hardware propio.

## Herramientas a utilizar

+ Base de datos physionet de tipo open access
+ Microsoft Visual Studio Code (GitHub y Python 3.12)
+ Plataformas de ejecución alternativa: Google Colab para correr notebooks sin configurar entorno local.

## Referencias Bibliográficas: 
- [1]World Health Organization: WHO, “Spinal cord injury,” World Health Organization: WHO, Apr. 16, 2024. Fecha de Acceso: Ago. 25, 2025. [En linea]. Recuperado de: https://www.who.int/news-room/fact-sheets/detail/spinal-cord-injury
- [2]MINSA, “Instituto Nacional de Rehabilitación brindó más de 1500 atenciones en consulta médica a pacientes con diagnóstico de lesión medular,” Gob.pe. Fecha de Acceso: Ago. 25, 2025. [En línea]. Recuperado de: https://www.gob.pe/institucion/minsa/noticias/975047-instituto-nacional-de-rehabilitacion-brindo-mas-de-1500-atenciones-en-consulta-medica-a-pacientes-con-diagnostico-de-lesion-medular
- [3]He, H., & Wu, D. “Transfer learning for brain–computer interfaces: A Euclidean space data alignment approach” IEEE Trans Biomed Eng, 2019. Fecha de Acceso: Sep. 01, 2025. [En línea]. Recuperado de: https://pubmed.ncbi.nlm.nih.gov/31034407/
- [4]Lotte, F., et al. “A review of classification algorithms for EEG-based brain–computer interfaces” Journal of Neural Engineering, 2018. Fecha de Acceso: Sep. 01, 2025. [En línea]. Recuperado de: https://pubmed.ncbi.nlm.nih.gov/17409472/
  
## Aportes al entrgable 1
- Leon Achate 33.33 %
- Nicolas Arango 33.33 %
- Hans Navarro 33.33 %
