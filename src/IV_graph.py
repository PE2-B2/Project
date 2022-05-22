from IVAnalysis import *

# IV raw data graph
plt.subplot(234)

plt.plot(v[0], abs(np.asarray(v[1])), 'k-o')
plt.title('IV-Analysis')
plt.xlabel('Voltage [V]')
plt.ylabel('Current [A]')
plt.yscale('logit')


# IV fitting graph
plt.subplot(235)
line1, = plt.plot(polyline, model1(polyline), color='red')

plt.scatter(v[0], np.abs(v[1]), s=70, c='red', lw=2, label="IV data")
plt.plot(v[0][9:11], np.abs(v[1][9:11]), c='red', lw=2, label="fitted graph")
plt.plot(V2, fittedDiagram, c='red', lw=2, label="R²:0.999999")

plt.title("IV-Analysis", size=15)
plt.xlabel('Voltage [V]', size=15)
plt.ylabel('Current [A]', size=15)
plt.yscale('logit')
plt.legend()
plt.grid(True)