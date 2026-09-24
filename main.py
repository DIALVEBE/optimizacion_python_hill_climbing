import plotext as plt


# =====================
# 1. Funcion objetivo
# =====================
def altura(x):
    return -(x - 7)**2 + 50


# =====================
# 2. Posicion inicial
# =====================
posicion = 0

recorrido = [posicion]


# =====================
# 3. Optimizacion
# =====================
while True:

    actual = altura(posicion)

    izquierda = altura(posicion - 1)
    derecha = altura(posicion + 1)

    print(
        f"x={posicion:2} | "
        f"altura={actual:2}"
    )

    if derecha > actual:
        posicion += 1

    elif izquierda > actual:
        posicion -= 1

    else:
        break

    recorrido.append(posicion)


# =====================
# 4. Resultado
# =====================
print("\n🏆 Mejor solucion encontrada")

print(f"x = {posicion}")
print(f"altura = {altura(posicion)}")


# =====================
# 5. Grafica en consola
# =====================

x = list(range(0, 15))
y = [altura(valor) for valor in x]


# Obtener figura
fig = plt.figure

# Limpiar figura
fig.clear()


# =====================
# Dibujar montaña
# =====================

montana = fig.signal(x, y)

# Conectar puntos con líneas
montana.lines()

# Dibujar
fig.draw(montana)


# =====================
# Dibujar recorrido
# =====================

x_recorrido = recorrido
y_recorrido = [
    altura(valor)
    for valor in recorrido
]

camino = fig.signal(
    x_recorrido,
    y_recorrido
)

fig.draw(camino)


# =====================
# Titulos
# =====================

fig.title(
    "Optimizacion con Hill Climbing"
)

fig.label(
    "Posicion",
    axis="x"
)

fig.label(
    "Altura",
    axis="y"
)


# =====================
# Mostrar
# =====================

fig.show()
