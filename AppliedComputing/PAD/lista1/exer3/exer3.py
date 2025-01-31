# 3) Plote agora o speedup em função da fração paralelizável (f) de um programa, para o
# intervalo 0 ˂ f ˂ 1, supondo um sistema com:
# SP=1/(1-f+f/P)
# (a) 8 processadores
import matplotlib.pyplot

results = []
for i in range(1,100):
    results.append(1/(1-(i/100)+(i/100)/8))

print(len(results))

matplotlib.pyplot.plot(results)
matplotlib.pyplot.show()


# (b) 128 processadores

resultsb = []
for i in range(1,100):
    resultsb.append(1/(1-(i/100)+(i/100)/128))

matplotlib.pyplot.plot(resultsb)
matplotlib.pyplot.show()
resultsb = []
