# Forest Fire Detection based on Color Spaces Combination
## Abstract
Utilizan una técnica híbrida en donde mezclan varios espacios de color.

## Introducción:
Hablan de porque el problema que están tratando de resolver.
Pros de usar imágenes:
- Barato
- Es "fácil" de mantener

Usan una combinación de HSV, HSL y HWB.

## Related work

Hablan de que hay métodos usando ML pero necesitan un paso de aprendizaje.
El problema es que tienden a hacer overfit.

Hay otros algoritmos y dan sus referencias. TODO Agregar esas referencias aquí.

## The method

### Preprocesamiento

Cargan una imágen: $I_{RGB}$ y le aplican un *blur* de $7x7$ que genera $I_{b}$.

La imágen se pasa a $I_{HSV}$, $I_{HSL}$ y $I_{HWB}$. Los componentes de las imágenes
se separan y se caculan los promedios de $W$ y $B$.

DUDA: COMO QUE SE PROMEDIAN? PROMEDIO TOTAL?

### Nuevo criterio de segmentación
Este criterio son 6 reglas.

$$
C = (S > 35) \land ((H \geq 330 \land H \leq 65) \land ((L > 70) \lor (B < B_{avg} \land W < W_{avg}) \lor (W > \text{Wavg} \land S > \text{Savg})) \lor (W \geq 98 \land B \leq 2))
$$

- $(S > 35)$: Esta parte asegura que los valores saturados y brillantes se seleccionen.
- $(H \geq 330 \land H \leq 65)$: Estos colors representan el rojo, naranja y amarillo para los incendios forestales.
- $(L > 70)$: DUDA. Es para seleccionar los colores de los límites. 
- $(B < B_{avg} \land W < W_{avg})$: Esta condición sirve para seleccionar los límites del fuego.
- $(W \geq 98 \land B \leq 2)$: Es para seleccionar los centros de las flamas.

Con esta regla, lo que haces es pasar a $0$ o a $255$ dependiendo si pasa la regla o no. Se evalua pixel a pixel y te produce $I_{\text{hybrid}}$

$$
I_{\text{hybrid}(x, y)} =
\begin{cases}
255 & \text{if } C \text{ is true} \\
0 & \text{otherwise}
\end{cases}
$$

### Post procesamiento

Quitan los cachos que tengan un tamaño menor a 150 (150 que)
y fue elegido de forma empírica para el dataset.

## Resultados

Usaron F1 y Accuracy.

Los mejores resultados que encontraron son dos grupos: 

1. Cuando hay mucho contraste.
2. Cuando el fuego está cerca de partes obscuras (cuando tiene humo o es de noche).

## Conclusión

### Cuando no funciona
- Cuando el humo está entre la cámara y el fuego.
- Su método no funciona si la imágen usa cámara infrarojas porque el fuego sale de color
  azul.
- Cuando no hay mucha calidad en la imágen el blur hace que se vuelva loco.
- Cuando la imágen tiene bajo contraste. Porque toma el humo como parte del fuego.
- Es mejor no tener ya que tienden a falsos positivos:
  - Nubes
  - Lugares con mucho pasto seco
  - Piedras con mucho colro.
  - Terreno con grava o arena.

### Cuando mejor funciona
- Cuando el fuego es más del 40% de la imágen.
- Es ideal para bosques.
- Cuando la imágen es predominantemente saturada por naranja.

