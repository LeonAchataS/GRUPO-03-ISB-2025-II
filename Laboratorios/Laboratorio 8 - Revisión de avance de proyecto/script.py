"""
EDA Simple para S001 - Proyecto BCI
"""

import mne
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Rutas
base_path = Path(r"C:\Users\Desktop\Documents\Pipelines\GRUPO-03-ISB-2025-II\Laboratorios\Laboratorio 8 - Revisión de avance de proyecto")
data_path = base_path / "eeg_data" / "S001"
img_path = base_path / "imagenes"
img_path.mkdir(exist_ok=True)

# Runs de interés (imaginación motora)
runs = ["R04", "R06", "R08", "R10", "R12", "R14"]

# Mapeo de tareas
task_map = {
    'R04': {'T1': 'Mano Izq', 'T2': 'Mano Der'},
    'R06': {'T1': 'Ambas Manos', 'T2': 'Ambos Pies'},
    'R08': {'T1': 'Mano Izq', 'T2': 'Mano Der'},
    'R10': {'T1': 'Ambas Manos', 'T2': 'Ambos Pies'},
    'R12': {'T1': 'Mano Izq', 'T2': 'Mano Der'},
    'R14': {'T1': 'Ambas Manos', 'T2': 'Ambos Pies'}
}

print("="*60)
print("EDA - Sujeto S001")
print("="*60)

# Almacenar resultados
resultados = []

for run in runs:
    print(f"\n--- Analizando {run} ---")
    
    # Cargar archivo
    file_path = data_path / f"S001{run}.edf"
    raw = mne.io.read_raw_edf(file_path, preload=True, verbose=False)
    
    # Metadatos
    info = raw.info
    fs = int(info['sfreq'])
    duracion = raw.n_times / fs
    n_canales = info['nchan']
    
    print(f"Duración: {duracion:.1f}s | Frecuencia: {fs}Hz | Canales: {n_canales}")
    print(f"Nombres de canales (primeros 10): {raw.ch_names[:10]}")
    
    # Extraer datos
    data, times = raw[:, :]
    data_uV = data * 1e6
    
    # Eventos
    events, event_id = mne.events_from_annotations(raw)
    unique, counts = np.unique(events[:, 2], return_counts=True)
    
    print(f"Eventos: T0={counts[0]}, T1={counts[1]}, T2={counts[2]}")
    print(f"Tareas: T1={task_map[run]['T1']}, T2={task_map[run]['T2']}")
    
    # Guardar para resumen
    resultados.append({
        'Run': run,
        'Duracion_s': duracion,
        'N_T0': counts[0],
        'N_T1': counts[1],
        'N_T2': counts[2],
        'Tarea_T1': task_map[run]['T1'],
        'Tarea_T2': task_map[run]['T2']
    })
    
    # Encontrar índices de canales motores (buscar con diferentes formatos)
    canales_interes = ['C3', 'Cz', 'C4']
    canales_motor = []
    indices_motor = []
    
    for ch in canales_interes:
        # Buscar variaciones del nombre
        posibles = [ch, f"{ch}.", f"{ch}..", f"{ch}..."]
        for variacion in posibles:
            if variacion in raw.ch_names:
                canales_motor.append(variacion)
                indices_motor.append(raw.ch_names.index(variacion))
                break
    
    print(f"Canales motores encontrados: {canales_motor}")
    
    # --- GRÁFICO 1: Señal cruda (30s) ---
    segundos = 30
    muestras = fs * segundos
    
    fig, axes = plt.subplots(3, 1, figsize=(14, 8))
    
    for i, (ch, idx) in enumerate(zip(canales_motor, indices_motor)):
        axes[i].plot(times[:muestras], data_uV[idx, :muestras], linewidth=0.7, color='blue')
        axes[i].set_ylabel(f'{ch}\n(µV)', fontsize=10)
        axes[i].grid(True, alpha=0.3)
        axes[i].set_xlim(0, segundos)
        
        # Marcar eventos en los primeros 30s
        events_30s = events[events[:, 0] < muestras]
        for event in events_30s:
            time_s = event[0] / fs
            event_code = event[2]
            if event_code == 1:
                color, label = 'green', 'T0'
            elif event_code == 2:
                color, label = 'blue', 'T1'
            else:
                color, label = 'red', 'T2'
            axes[i].axvline(time_s, color=color, alpha=0.5, linestyle='--', linewidth=1.5)
    
    axes[-1].set_xlabel('Tiempo (s)', fontsize=11)
    fig.suptitle(f'S001 - {run}: {task_map[run]["T1"]} vs {task_map[run]["T2"]}', 
                 fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.savefig(img_path / f'S001_{run}_señal.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  ✓ Gráfico de señal guardado")
    
    # --- GRÁFICO 2: PSD ---
    fig, axes = plt.subplots(1, 3, figsize=(14, 4))
    
    for i, (ch, idx) in enumerate(zip(canales_motor, indices_motor)):
        # Calcular PSD manualmente con Welch
        from scipy import signal as sp_signal
        freqs, psd = sp_signal.welch(data_uV[idx], fs=fs, nperseg=min(512, len(data_uV[idx])//4))
        
        # Filtrar hasta 50 Hz
        mask = freqs <= 50
        freqs_plot = freqs[mask]
        psd_plot = psd[mask]
        
        axes[i].plot(freqs_plot, 10*np.log10(psd_plot), linewidth=1.5, color='blue')
        axes[i].set_xlabel('Frecuencia (Hz)', fontsize=10)
        axes[i].set_ylabel('Potencia (dB)', fontsize=10)
        axes[i].set_title(ch, fontsize=11, fontweight='bold')
        axes[i].axvspan(8, 13, alpha=0.2, color='blue', label='Mu (8-13 Hz)')
        axes[i].axvspan(13, 30, alpha=0.2, color='red', label='Beta (13-30 Hz)')
        axes[i].legend(fontsize=8)
        axes[i].grid(True, alpha=0.3)
        axes[i].set_xlim(1, 50)
    
    fig.suptitle(f'S001 - {run}: Densidad Espectral de Potencia', 
                 fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.savefig(img_path / f'S001_{run}_psd.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  ✓ Gráfico PSD guardado")
    
    # --- GRÁFICO 3: ERP ---
    events_task = events[events[:, 2] != 1]  # Excluir T0
    
    if len(events_task) > 0:
        epochs = mne.Epochs(raw, events_task, event_id={'T1': 2, 'T2': 3},
                           tmin=-1, tmax=4, baseline=(-1, 0), preload=True, verbose=False)
        
        fig, axes = plt.subplots(1, 3, figsize=(14, 4))
        
        for i, ch in enumerate(canales_motor):
            picks = mne.pick_channels(epochs.ch_names, [ch])
            
            if len(epochs['T1']) > 0:
                evoked_t1 = epochs['T1'].average(picks=picks)
                times_erp = evoked_t1.times
                axes[i].plot(times_erp, evoked_t1.data[0]*1e6, 
                           label=f"T1: {task_map[run]['T1']}", linewidth=2, color='blue')
            
            if len(epochs['T2']) > 0:
                evoked_t2 = epochs['T2'].average(picks=picks)
                times_erp = evoked_t2.times
                axes[i].plot(times_erp, evoked_t2.data[0]*1e6, 
                           label=f"T2: {task_map[run]['T2']}", linewidth=2, color='red')
            
            axes[i].axvline(0, color='k', linestyle='--', label='Inicio tarea', linewidth=1.5)
            axes[i].axhline(0, color='gray', linestyle='-', alpha=0.3)
            axes[i].set_xlabel('Tiempo (s)', fontsize=10)
            axes[i].set_ylabel('Amplitud (µV)', fontsize=10)
            axes[i].set_title(ch, fontsize=11, fontweight='bold')
            axes[i].legend(fontsize=8, loc='best')
            axes[i].grid(True, alpha=0.3)
        
        fig.suptitle(f'S001 - {run}: Event-Related Potentials', 
                     fontsize=13, fontweight='bold')
        plt.tight_layout()
        plt.savefig(img_path / f'S001_{run}_erp.png', dpi=150, bbox_inches='tight')
        plt.close()
        print(f"  ✓ Gráfico ERP guardado")

print("\n" + "="*60)

# Resumen
df_resumen = pd.DataFrame(resultados)
print("\nRESUMEN S001:")
print(df_resumen.to_string(index=False))

# Guardar resumen
df_resumen.to_csv(img_path / 'S001_resumen.csv', index=False)

print(f"\n✅ Análisis completo. Imágenes guardadas en: {img_path}")
print("="*60)