import matplotlib.pyplot as plt

def graficar_diagrama_de_lineas(x, y, etiqueta_x, etiqueta_y, titulo):
    plt.plot(x, y)
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)
    plt.title(titulo)
    plt.show()

def graficar_diagrama_de_barras(x, y, etiqueta_x, etiqueta_y, titulo):
    plt.bar(x, y)
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)
    plt.title(titulo)
    plt.show()

def graficar_diagrama_de_pastel(etiquetas, valores, titulo):
    plt.pie(valores, labels=etiquetas, autopct='%1.1f%%')
    plt.title(titulo)
    plt.show()
