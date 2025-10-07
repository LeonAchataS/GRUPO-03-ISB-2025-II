import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pywt
from scipy import signal
import os

# ============================================
# CONFIGURACIÓN DE RUTAS
# ============================================
base_path = r"C:\Users\Lenovo\OneDrive\Desktop\PUCP\ISB\Lab7"
img_path = os.path.join(base_path, "imagenes")

# Crear carpeta de imágenes si no existe
os.makedirs(img_path, exist_ok=True)

# ============================================
# CONFIGURACIÓN DE MATPLOTLIB
# ============================================
plt.rcParams['figure.figsize'] = (14, 6)
plt.rcParams['font.size'] = 10
plt.rcParams['axes.grid'] = True

# ============================================
# FUNCIONES AUXILIARES
# ============================================

def calcular_snr(señal_original, señal_filtrada):
    """
    Calcula la relación señal-ruido (SNR) en dB
    SNR = 10 * log10(Potencia_señal / Potencia_ruido)
    """
    ruido = señal_original - señal_filtrada
    potencia_señal = np.sum(señal_filtrada ** 2)
    potencia_ruido = np.sum(ruido ** 2)
    
    if potencia_ruido == 0:
        return float('inf')
    
    snr = 10 * np.log10(potencia_señal / potencia_ruido)
    return snr

def aplicar_filtro_wavelet(señal, wavelet, nivel, modo='soft'):
    """
    Aplica filtrado wavelet a una señal
    
    Parámetros:
    - señal: array de datos
    - wavelet: tipo de wavelet (ej: 'db4', 'coif3', 'bior3.7')
    - nivel: nivel de descomposición
    - modo: tipo de umbralización ('soft' o 'hard')
    
    Retorna:
    - señal_filtrada: señal reconstruida
    - coeficientes: coeficientes wavelet originales
    - coeficientes_thresh: coeficientes después de umbralización
    """
    # Descomposición wavelet
    coeficientes = pywt.wavedec(señal, wavelet, level=nivel)
    
    # Calcular umbral usando regla universal de Donoho
    sigma = np.median(np.abs(coeficientes[-1])) / 0.6745
    umbral = sigma * np.sqrt(2 * np.log(len(señal)))
    
    # Aplicar umbralización (threshold)
    coeficientes_thresh = list(coeficientes)
    coeficientes_thresh[1:] = [pywt.threshold(c, umbral, mode=modo) for c in coeficientes[1:]]
    
    # Reconstrucción
    señal_filtrada = pywt.waverec(coeficientes_thresh, wavelet)
    
    # Ajustar longitud si es necesario
    if len(señal_filtrada) > len(señal):
        señal_filtrada = señal_filtrada[:len(señal)]
    
    return señal_filtrada, coeficientes, coeficientes_thresh

def calcular_fft(señal, fs):
    """
    Calcula la FFT de una señal usando el método de Welch para reducir ruido
    
    Retorna:
    - frecuencias: array de frecuencias
    - psd_dB: densidad espectral de potencia en dB
    """
    # FFT usando método de Welch para minimizar ruido
    freqs_welch, psd_welch = signal.welch(señal, fs, nperseg=2048, window='hann')
    
    # Convertir a dB (PSD usa 10*log10)
    psd_dB = 10 * np.log10(psd_welch + 1e-12)
    
    return freqs_welch, psd_dB

# ============================================
# FUNCIÓN PRINCIPAL DE PROCESAMIENTO
# ============================================

def procesar_señal(archivo, nombre_señal, wavelet, nivel, fs=1000, color_crudo='blue', color_filtrado='red'):
    """
    Procesa una señal biomédica y genera todas las gráficas
    """
    print(f"\n{'='*60}")
    print(f"PROCESANDO SEÑAL: {nombre_señal}")
    print(f"{'='*60}")
    print(f"Wavelet seleccionada: {wavelet}")
    print(f"Nivel de descomposición: {nivel}")
    
    # Cargar archivo
    df = pd.read_csv(archivo, sep="\t", comment="#", header=None)
    df.columns = ["nSeq", "I1", "I2", "O1", "O2", "A1", "extra"]
    
    # Extraer señal
    señal_cruda = df["A1"].values
    N = len(señal_cruda)
    t = np.arange(N) / fs
    
    print(f"Duración de la señal: {N/fs:.2f} segundos ({N} muestras)")
    
    # Aplicar filtro wavelet
    señal_filtrada, coefs_orig, coefs_thresh = aplicar_filtro_wavelet(
        señal_cruda, wavelet, nivel
    )
    
    # Calcular SNR
    snr_value = calcular_snr(señal_cruda, señal_filtrada)
    print(f"SNR después del filtrado: {snr_value:.2f} dB")
    
    # Calcular FFT
    freq_crudo, mag_crudo = calcular_fft(señal_cruda, fs)
    freq_filt, mag_filt = calcular_fft(señal_filtrada, fs)
    
    # ============================================
    # GRÁFICA 1: SEÑAL CRUDA
    # ============================================
    plt.figure(figsize=(14, 6))
    plt.plot(t, señal_cruda, color=color_crudo, linewidth=0.5, alpha=0.8)
    plt.title(f'{nombre_señal} - Señal Cruda (Original)', fontsize=14, fontweight='bold')
    plt.xlabel('Tiempo (s)', fontsize=12)
    plt.ylabel('Amplitud', fontsize=12)
    plt.xlim([0, 10])  # Mostrar solo primeros 10 segundos
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(img_path, f'{nombre_señal}_crudo.png'), dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Guardada: {nombre_señal}_crudo.png")
    
    # ============================================
    # GRÁFICA 2: SEÑAL FILTRADA
    # ============================================
    plt.figure(figsize=(14, 6))
    plt.plot(t, señal_filtrada, color=color_filtrado, linewidth=0.8)
    plt.title(f'{nombre_señal} - Señal Filtrada (Wavelet {wavelet})', fontsize=14, fontweight='bold')
    plt.xlabel('Tiempo (s)', fontsize=12)
    plt.ylabel('Amplitud', fontsize=12)
    plt.xlim([0, 10])  # Mostrar solo primeros 10 segundos
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(img_path, f'{nombre_señal}_filtrado.png'), dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Guardada: {nombre_señal}_filtrado.png")
    
    # ============================================
    # GRÁFICA 3: COMPARACIÓN
    # ============================================
    plt.figure(figsize=(14, 6))
    plt.plot(t, señal_cruda, color=color_crudo, linewidth=0.5, alpha=0.6, label='Señal Cruda')
    plt.plot(t, señal_filtrada, color=color_filtrado, linewidth=1, label='Señal Filtrada')
    plt.title(f'{nombre_señal} - Comparación: Cruda vs Filtrada', fontsize=14, fontweight='bold')
    plt.xlabel('Tiempo (s)', fontsize=12)
    plt.ylabel('Amplitud', fontsize=12)
    plt.xlim([0, 10])  # Mostrar solo primeros 10 segundos
    plt.legend(loc='upper right', fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(img_path, f'{nombre_señal}_comparacion.png'), dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Guardada: {nombre_señal}_comparacion.png")
    
    # ============================================
    # GRÁFICA 4: FFT SEÑAL CRUDA
    # ============================================
    plt.figure(figsize=(14, 6))
    plt.plot(freq_crudo, mag_crudo, color=color_crudo, linewidth=0.8)
    plt.title(f'{nombre_señal} - Espectro de Frecuencia (Señal Cruda) - Método de Welch', fontsize=14, fontweight='bold')
    plt.xlabel('Frecuencia (Hz)', fontsize=12)
    plt.ylabel('PSD (dB/Hz)', fontsize=12)
    plt.xlim([0, fs/2])  # Mostrar hasta frecuencia de Nyquist
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(img_path, f'{nombre_señal}_crudo_FFT.png'), dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Guardada: {nombre_señal}_crudo_FFT.png")
    
    # ============================================
    # GRÁFICA 5: FFT SEÑAL FILTRADA
    # ============================================
    plt.figure(figsize=(14, 6))
    plt.plot(freq_filt, mag_filt, color=color_filtrado, linewidth=0.8)
    plt.title(f'{nombre_señal} - Espectro de Frecuencia (Señal Filtrada) - Método de Welch', fontsize=14, fontweight='bold')
    plt.xlabel('Frecuencia (Hz)', fontsize=12)
    plt.ylabel('PSD (dB/Hz)', fontsize=12)
    plt.xlim([0, fs/2])
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(img_path, f'{nombre_señal}_filtrado_FFT.png'), dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Guardada: {nombre_señal}_filtrado_FFT.png")
    
    # ============================================
    # GRÁFICA 6: COEFICIENTES WAVELET
    # ============================================
    fig, axes = plt.subplots(nivel + 1, 1, figsize=(14, 2*(nivel+1)))
    
    # Coeficientes de aproximación (cA)
    axes[0].plot(coefs_orig[0], color='green', linewidth=0.5)
    axes[0].set_title(f'Coeficientes de Aproximación (cA{nivel})', fontsize=11, fontweight='bold')
    axes[0].grid(True, alpha=0.3)
    
    # Coeficientes de detalle (cD)
    for i in range(1, nivel + 1):
        axes[i].plot(coefs_orig[i], color='orange', linewidth=0.5)
        axes[i].set_title(f'Coeficientes de Detalle (cD{nivel-i+1})', fontsize=11, fontweight='bold')
        axes[i].grid(True, alpha=0.3)
    
    axes[-1].set_xlabel('Índice', fontsize=12)
    fig.suptitle(f'{nombre_señal} - Descomposición Wavelet ({wavelet})', 
                 fontsize=14, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig(os.path.join(img_path, f'{nombre_señal}_coeficientes_wavelet.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Guardada: {nombre_señal}_coeficientes_wavelet.png")
    
    print(f"\n✓ Procesamiento de {nombre_señal} completado exitosamente")
    return snr_value

# ============================================
# PROGRAMA PRINCIPAL
# ============================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("SISTEMA DE FILTRADO WAVELET PARA SEÑALES BIOMÉDICAS")
    print("="*60)
    
    # Configuración de señales
    configuraciones = [
        {
            'archivo': os.path.join(base_path, 'ECG.txt'),
            'nombre': 'ECG',
            'wavelet': 'db4',  # Daubechies 4
            'nivel': 6,
            'color_crudo': 'blue',
            'color_filtrado': 'red'
        },
        {
            'archivo': os.path.join(base_path, 'EMG.txt'),
            'nombre': 'EMG',
            'wavelet': 'coif3',  # Coiflet 3
            'nivel': 5,
            'color_crudo': 'green',
            'color_filtrado': 'darkgreen'
        },
        {
            'archivo': os.path.join(base_path, 'EEG.txt'),
            'nombre': 'EEG',
            'wavelet': 'bior3.7',  # Biortogonal 3.7
            'nivel': 6,
            'color_crudo': 'purple',
            'color_filtrado': 'darkviolet'
        }
    ]
    
    # Procesar cada señal
    resultados_snr = {}
    
    for config in configuraciones:
        try:
            snr = procesar_señal(
                archivo=config['archivo'],
                nombre_señal=config['nombre'],
                wavelet=config['wavelet'],
                nivel=config['nivel'],
                color_crudo=config['color_crudo'],
                color_filtrado=config['color_filtrado']
            )
            resultados_snr[config['nombre']] = snr
        except Exception as e:
            print(f"\n✗ Error procesando {config['nombre']}: {str(e)}")
    
    # Resumen final
    print("\n" + "="*60)
    print("RESUMEN DE RESULTADOS - SNR")
    print("="*60)
    for señal, snr in resultados_snr.items():
        print(f"{señal:10s}: {snr:8.2f} dB")
    
    print("\n" + "="*60)
    print(f"✓ PROCESO COMPLETADO")
    print(f"✓ Imágenes guardadas en: {img_path}")
    print("="*60 + "\n")