import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
import os

# Configuración
ruta_datos = r"C:\Users\Lenovo\OneDrive\Desktop\PUCP\ISB\Lab6"
ruta_guardar = r"C:\Users\Lenovo\OneDrive\Desktop\PUCP\ISB\Lab6\Imagenes"
fs = 1000  # Hz
nyq = fs / 2

archivos = [
    "ECG_agitado.txt",
    "ECG_basal.txt",
    "EMG_bicep_libre.txt",
    "EMG_bicep_limitado.txt"
]

# Procesar cada señal
for archivo in archivos:
    nombre_señal = archivo.replace(".txt", "")
    print("=" * 60)
    print(f"Procesando: {nombre_señal}")
    print("=" * 60)
    
    # Leer datos
    df = pd.read_csv(os.path.join(ruta_datos, archivo),
                     sep="\t", comment="#", header=None)
    df.columns = ["nSeq", "I1", "I2", "O1", "O2", "A1", "extra"]
    raw = df["A1"].values
    N = len(raw)
    t = np.arange(N) / fs
    
    # Determinar frecuencias de corte según tipo de señal
    if "ECG" in nombre_señal:
        fc_low = 0.5  # Hz
        fc_high = 40  # Hz
    else:  # EMG
        fc_low = 20  # Hz
        fc_high = 450  # Hz
    
    # ========== FILTRO 1: FIR con ventana Hamming ==========
    print("Aplicando filtro FIR con ventana Hamming...")
    orden_fir = 101
    coef_fir = signal.firwin(orden_fir, [fc_low/nyq, fc_high/nyq], 
                             window='hamming', pass_zero=False)
    filtrada_fir = signal.filtfilt(coef_fir, 1, raw)
    
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(t[:5000], raw[:5000], 'b-', linewidth=0.5)
    plt.title(f'Señal Original - {nombre_señal}')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.subplot(2, 1, 2)
    plt.plot(t[:5000], filtrada_fir[:5000], 'r-', linewidth=0.5)
    plt.title('Filtro FIR con ventana Hamming')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(ruta_guardar, f"{nombre_señal}_FIR.png"), dpi=150)
    plt.close()
    
    # ========== FILTRO 2: Butterworth ==========
    print("Aplicando filtro Butterworth...")
    orden_butter = 4
    b_butter, a_butter = signal.butter(orden_butter, [fc_low/nyq, fc_high/nyq], 
                                       btype='band')
    filtrada_butter = signal.filtfilt(b_butter, a_butter, raw)
    
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(t[:5000], raw[:5000], 'b-', linewidth=0.5)
    plt.title(f'Señal Original - {nombre_señal}')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.subplot(2, 1, 2)
    plt.plot(t[:5000], filtrada_butter[:5000], 'g-', linewidth=0.5)
    plt.title('Filtro Butterworth')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(ruta_guardar, f"{nombre_señal}_Butter.png"), dpi=150)
    plt.close()
    
    # ========== FILTRO 3: Chebyshev Tipo I ==========
    print("Aplicando filtro Chebyshev Tipo I...")
    orden_cheby = 4
    ripple = 0.5  # dB
    b_cheby, a_cheby = signal.cheby1(orden_cheby, ripple, [fc_low/nyq, fc_high/nyq], 
                                     btype='band')
    filtrada_cheby = signal.filtfilt(b_cheby, a_cheby, raw)
    
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(t[:5000], raw[:5000], 'b-', linewidth=0.5)
    plt.title(f'Señal Original - {nombre_señal}')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.subplot(2, 1, 2)
    plt.plot(t[:5000], filtrada_cheby[:5000], 'm-', linewidth=0.5)
    plt.title('Filtro Chebyshev Tipo I')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(ruta_guardar, f"{nombre_señal}_Cheby.png"), dpi=150)
    plt.close()
    
    # ========== FILTRO 4: Notch (60 Hz) ==========
    print("Aplicando filtro Notch...")
    f0 = 60.0  # Hz - Frecuencia a eliminar
    Q = 30.0   # Factor de calidad
    b_notch, a_notch = signal.iirnotch(f0, Q, fs)
    filtrada_notch = signal.filtfilt(b_notch, a_notch, raw)
    
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(t[:5000], raw[:5000], 'b-', linewidth=0.5)
    plt.title(f'Señal Original - {nombre_señal}')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.subplot(2, 1, 2)
    plt.plot(t[:5000], filtrada_notch[:5000], 'c-', linewidth=0.5)
    plt.title('Filtro Notch (60 Hz)')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(ruta_guardar, f"{nombre_señal}_Notch.png"), dpi=150)
    plt.close()
    
    print(f"✓ Completado: {nombre_señal}\n")

print("=" * 60)
print("PROCESAMIENTO COMPLETO")
print("=" * 60)