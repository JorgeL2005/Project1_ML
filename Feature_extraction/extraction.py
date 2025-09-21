import h5py

# Abrir para lectura (modo por defecto)

with h5py.File('train.h5', 'r') as f:
    print("Archivo abierto correctamente")
    print("Contenido:", list(f.keys()))