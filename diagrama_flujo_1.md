```mermaid
flowchart TD

A[Inicio] --> B[Mostrar bienvenida]
B --> C[Ingresar nombre del producto]

C --> D[precio = -1]

D --> E{¿precio <= 0?}
E -->|Sí| F[Ingresar costo como texto]
F --> G{¿Es número válido?}

G -->|No| H[Mostrar error]
H --> E

G -->|Sí| I[Convertir a float]
I --> J{¿precio <= 0?}

J -->|Sí| K[Mostrar error]
K --> E

J -->|No| L[Continuar]

E -->|No| L

L --> M[cantidad = -1]

M --> N{¿cantidad <= 0?}
N -->|Sí| O[Ingresar cantidad como texto]
O --> P{¿Es número entero?}

P -->|No| Q[Mostrar error]x|
Q --> N

P -->|Sí| R[Convertir a int]
R --> S{¿cantidad <= 0?}

S -->|Sí| T[Mostrar error]
T --> N

S -->|No| U[Continuar]

N -->|No| U

U --> V[Calcular costo_total = precio * cantidad]

V --> W[Mostrar resultados]

W --> X[Fin]
```