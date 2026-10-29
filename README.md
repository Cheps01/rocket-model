# Modelo MIMO de un cohete: análisis de estabilidad, respuesta y control

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Cheps01/rocket-model/blob/main/analysis.ipynb)

Código y cuaderno de análisis que acompañan al artículo **«TÍTULO DEL PAPER»** (AUTORES, AÑO).
El repositorio modela un cohete como un sistema **MIMO lineal de 4 estados, 2 entradas y 2 salidas**, y calcula su función de transferencia, estabilidad, respuesta temporal y en frecuencia, observabilidad y controlabilidad, en función de dos ganancias de control (K1, K2).

> **Cómo citar:** ver [Citación](#citación). Para reproducir los resultados del artículo, ir directo a [Reproducir los resultados](#reproducir-los-resultados).

---

## Índice

1. [Contenido del repositorio](#contenido-del-repositorio)
2. [El modelo en una página](#el-modelo-en-una-página)
3. [Mapa artículo ↔ cuaderno](#mapa-artículo--cuaderno)
4. [Reproducir los resultados](#reproducir-los-resultados)
5. [Limitaciones conocidas](#limitaciones-conocidas)
6. [Citación y licencia](#citación)

---

## Contenido del repositorio

| Ruta | Qué contiene | Se usa en |
|------|--------------|-----------|
| [`analysis.ipynb`](analysis.ipynb) | Todo el análisis, secciones (A) a (F), con salidas ya guardadas (se puede leer sin ejecutar) | Artículo, secciones X–Y |
| [`simulation-diagram.jpeg`](simulation-diagram.jpeg) | Diagrama de simulación del lazo de control | Artículo, Fig. N |
| [`src/system_rep.py`](src/system_rep.py) | Extracción simbólica de las matrices A, B, C, D desde las ecuaciones (SymPy), sustitución numérica e impresión de las ecuaciones | Cuaderno, secciones 3–4 |
| [`src/properties.py`](src/properties.py) | `SystemProps`: pruebas de estabilidad, controlabilidad y observabilidad por rango | Cuaderno, secciones 11–12 |
| `requirements.txt` | Dependencias con versiones fijadas | — |

---

## El modelo en una página

**Estados** `x = [a, θ, ω, δ]ᵀ`, **entradas** `u = [u₁, u₂]ᵀ`, **salidas** `y = [a, θ]ᵀ`.

```
da/dt = -(1 + K1·ka)/Tm · a  -  cθ · θ  +  (K1·ka/Tm) · u1
dθ/dt = ω
dω/dt = kε · a  +  μ · θ  -  ad · ω  +  kδ · δ
dδ/dt = -(1/Ts) · δ  -  (K2/Ts) · θ  -  (λ·K2/Ts) · ω  +  (K2/Ts) · u2
```

| Símbolo en el artículo / diagrama | Variable en el código | Significado | Valor |
|---|---|---|---|
| `a` (`α` en el diagrama) | `acc` | Aceleración axial | estado |
| `θ` | `theta` | Ángulo de cabeceo | estado |
| `ω` | `omega` | Velocidad angular de cabeceo | estado |
| `δ` | `delta` | Deflexión de la tobera | estado |
| `u₁`, `u₂` | `u1`, `u2` | Comando de empuje, comando de tobera | entradas |
| `K1`, `K2` | `k1`, `k2` | Ganancias de los canales de empuje y de dirección | parámetros de diseño |
| `ka` | `ka` | Ganancia del actuador | 0.0655 |
| `1/Tm` | `inv_tm` | Ancho de banda del motor | 1.0672 |
| `cθ` | `c0` | Acoplamiento gravitatorio | 9.81 |
| `μ` | `mu` | Rigidez aerodinámica | 1.20 |
| `ad` | `ad` | Amortiguamiento aerodinámico | 0.35 |
| `kδ` | `kd` | Efectividad de la tobera | 8.5 |
| `kε` | `ke` | Acoplamiento por desalineación | 0.12 |
| `Ts` (`1/Ts` = 20) | `ts` | Constante de tiempo del servo | 0.05 |
| `λ` | `lmd` | Proporción velocidad/posición de la IMU | 0.6 |

Punto de operación nominal usado en el artículo: **K1 = 1.00, K2 = 0.50**.

---

## Mapa artículo ↔ cuaderno

| Artículo | Sección del cuaderno | Qué se calcula |
|---|---|---|
| Sec. X | **(A)** 1–2. Análisis y diagrama de simulación | Descripción física de bloques y parámetros |
| Sec. X | **(A)** 3–5. Ecuación de estados, función de transferencia, ecuación de salida | Matrices A, B, C, D simbólicas; `G(p) = C(pI − A)⁻¹B` con `G₁₁, G₁₂, G₂₁, G₂₂` |
| Sec. X | **(B)** 6. Estabilidad | Polinomio característico, polos y mapa de estabilidad en el plano (K1, K2) |
| Sec. X | **(B)** 7. Respuesta temporal | Escalón, senoidal e impulso, por canal y simultáneos, para varios pares (K1, K2) |
| Sec. X | **(B)** 8. Acoplamiento | Respuesta de u₁→y y u₂→y por separado |
| Sec. X | **(C)** 9–10. Respuesta en frecuencia | Magnitud de los 4 canales al variar K2 de 0.10 a 1.00; ancho de banda a −3 dB, ganancia DC, pico de resonancia |
| Sec. X | **(D)** 11. Observabilidad | Rango de `[C; CA; CA²; CA³]` con solo acelerómetro, solo ángulo y ambos (los tres: rango 4) |
| Sec. X | **(D)** 12. Controlabilidad | Rango de `[B, AB, A²B, A³B]` con solo empuje, solo tobera y ambos (K2 = 0.5: rango 4; K2 = 0: rango 3, el estado δ deja de ser alcanzable) |
| Sec. X | **(E)** Selección de ganancias | Rangos de operación propuestos: 1.00 ≤ K1 ≤ 1.50 y 0.40 ≤ K2 ≤ 0.68 |
| Sec. X | **(F)** Conclusiones | Resumen del efecto de K1 y K2 |

> Completar la columna «Artículo» con los números de sección y figura del paper.

---

## Reproducir los resultados

Requisitos: Python 3.10 o superior.

**Opción 1: Google Colab (sin instalar nada).** Abrir el cuaderno con el botón *Abrir en Colab* de arriba y, antes de ejecutar nada, correr esta celda para traer el código de `src/` y las dependencias:

```python
!git clone https://github.com/Cheps01/rocket-model.git
%cd rocket-model
!pip install -q -r requirements.txt
```

Luego usar **Runtime → Run all**. El cuaderno busca `src/__init__.py` desde el directorio de trabajo, así que el directorio actual debe ser la raíz del repositorio.

**Opción 2: local.**

```bash
git clone https://github.com/Cheps01/rocket-model.git
cd rocket-model
python -m venv .venv && source .venv/bin/activate   # en Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook analysis.ipynb
```

**Opción 3: ejecutar sin abrir Jupyter.**

```bash
jupyter nbconvert --to notebook --execute analysis.ipynb --output analysis_ejecutado.ipynb
```

El cuaderno tarda unos minutos por los barridos sobre la malla de ganancias y las gráficas de respuesta temporal.

---

## Limitaciones conocidas

- Modelo **lineal e invariante en el tiempo**, linealizado alrededor de un punto de operación; no incluye saturaciones ni perturbaciones.
- El período de muestreo `T` está definido como parámetro, pero el análisis se hace en tiempo continuo; el diseño del controlador discreto queda fuera del alcance de este repositorio.

---

## Citación

```bibtex
@misc{rocket-model,
  author = {AUTORES},
  title  = {rocket-model: análisis MIMO de un cohete},
  year   = {AÑO},
  url    = {https://github.com/Cheps01/rocket-model},
  note   = {Versión vX.Y, DOI: 10.5281/zenodo.XXXXXXX}
}
```

Licencia: ver [`LICENSE`](LICENSE).