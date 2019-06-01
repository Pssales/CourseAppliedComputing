# -*- coding: utf-8 -*-
import numpy as np
import waipy

nome = 'S3 ' # nome da série para plotagem
nomeArquivo = 's3.txt'		
data = np.genfromtxt(nomeArquivo, delimiter = '\n',dtype = 'float32',filling_values = 0)
time = np.linspace(0, len(data), len(data))

# Data normalization
data_norm = waipy.normalize(data)

# Continuous wavelet transform
result = waipy.cwt(data_norm, dt=0.25, pad=1, dj=0.25, s0=2*0.25, j1=7/0.25, lag1=0.72, param=6, mother='Morlet', name=nome)

# Plotting the result
waipy.wavelet_plot(var=nome, time=time, data=data_norm, dtmin=0.03125, result=result)