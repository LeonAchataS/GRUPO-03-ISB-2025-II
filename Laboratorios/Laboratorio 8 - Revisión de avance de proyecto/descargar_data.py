import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mne
import os
import urllib.request

# Carpeta base de destino
base_dir = "./eeg_data"
os.makedirs(base_dir, exist_ok=True)

# Número de pacientes
num_pacientes = 1
pacientes = [f"S{str(i).zfill(3)}" for i in range(1, num_pacientes+1)]

# Descagarmos los runs que necesitamos
runs = ["R04", "R06", "R08","R10","R12","R14"]

# Base URL de PhysioNet
base_url = "https://physionet.org/files/eegmmidb/1.0.0/"

for paciente in pacientes:
    paciente_dir = os.path.join(base_dir, paciente)
    os.makedirs(paciente_dir, exist_ok=True)

    for run in runs:
        for ext in [".edf", ".edf.event"]:
            filename = f"{paciente}{run}{ext}"
            url = f"{base_url}{paciente}/{filename}"
            filepath = os.path.join(paciente_dir, filename)
            
            # Verificar si el archivo ya existe
            if os.path.exists(filepath):
                print(f"El archivo ya existe: {filename}")
                continue
            
            print(f"Descargando: {url}")
            try:
                urllib.request.urlretrieve(url, filepath)
                print(f"✓ Descargado exitosamente: {filename}")
            except Exception as e:
                print(f"✗ Error al descargar {filename}: {e}")