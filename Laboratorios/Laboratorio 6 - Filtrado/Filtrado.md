## Introducción 
##### En el procesamiento de señales biomédicas, como ECG, EEG o EMG, el ruido y los artefactos pueden interferir con la interpretación clínica y la recuperación de parámetros. El filtrado digital es actualmente el método principal para eliminar la señal no deseada causada por interferencias externas, como el ruido de la línea eléctrica, la contracción muscular o la deriva de baja frecuencia. Los filtros están diseñados para preservar las características deseadas de la señal y mejorar la relación señal-ruido, lo que facilita la visualización y el procesamiento automático. Además, el filtrado computacional ofrece una solución mejorada en comparación con los métodos analógicos convencionales, puesto que es más adaptable. Sea al ajustar la frecuencia de corte, la pendiente y el orden del filtro sin necesidad de modificar el hardware. Esto produce un procesamiento más preciso y reproducible, especialmente ventajoso en entornos clínicos y de investigación, donde la calidad de la señal influye directamente en la precisión del diagnóstico y el desarrollo de nuevos dispositivos biomédicos. En el caso específico de este laboratorio se van a procesar dos señales EMG y dos ECG:


### ECG:
##### Se suele empelar filtros de duración finita (FIR) [1]. Para el uso de ventanas se recomienda el uso del tipo Hamming [2].

### EMG: 
##### Al tratarse de EMG de superficie, se usan filtros pasa banda de 20Hz a 400-450 Hz [3]. De igual manera que en el caso de las señales ECG, también se opta por el uso de ventanas Hamming.

## Bibliografía:
##### [1] Oldřich Ondráček, Jozef Púčik, and E. Cocherová, “FILTERS FOR ECG DIGITAL SIGNAL PROCESSING,” Trends in Biomedical Engineering” Setiembre 7 - 9, 2005, University of ZilinaTrends in Biomedical Engineering” September 7 - 9, 2005, University of Zilina, pp. 91–96, En. 2005, Available: https://www.researchgate.net/publication/234047548_FILTERS_FOR_ECG_DIGITAL_SIGNAL_PROCESSING

##### [2] I. A. Sulaiman, H. M. Hassan, M. Danish, M. Singh, P. K. Singh, and M. Rajoriya, “Design, comparison and analysis of low pass FIR filter using window techniques method,” Materials Today: Proceedings, Dic. 2020, doi: https://doi.org/10.1016/j.matpr.2020.10.952.

##### [3] “EMG Signal Processing: Key Techniques and Practical Recommendations – Noraxon,” Noraxon.com, 2025. https://www.noraxon.com/article/emg-signal-processing-key-techniques-and-practical-recommendations/

‌
