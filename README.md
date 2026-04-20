# Sistema Veterinario en Python

Este proyecto modela el funcionamiento básico de una clínica veterinaria usando programación orientada a objetos.

## Cómo ejecutar

1. Abrir una terminal en esta carpeta.
2. Ejecutar:

```bash
python hospital_veterinario.py
```

## Explicación oral breve de los conceptos de POO

### Herencia
Se ve en `Persona`, que es la clase base, y en `Veterinario`, `Recepcionista` y `Cliente`, que heredan de ella. También se ve en `MetodoPago`, que es la clase base de `PagoEfectivo`, `PagoTarjeta` y `PagoTransferencia`.

### Abstracción
Se ve en `Persona` y `MetodoPago`, porque son clases abstractas que obligan a implementar métodos como `mostrar_rol()` y `procesar_pago()`.

### Encapsulación
Se ve en cada clase porque cada una maneja sus propios atributos y comportamientos. Por ejemplo, `Cliente` controla su lista de `mascotas` mediante `agregar_mascota()` y `mostrar_mascotas()`.

### Asociación
Se ve en `Consulta`, que se relaciona con `Mascota` y `Veterinario`. La consulta conecta a ambos, porque un veterinario atiende a una mascota en un momento específico.

### Agregación
Se ve en `Cliente` y `Mascota`. El cliente tiene una lista de mascotas, pero la mascota puede existir aunque el cliente deje de existir en el sistema.

### Composición
Se ve en `Consulta` y `Tratamiento`. Los tratamientos se crean dentro de la consulta con `crear_tratamiento()`, por eso dependen de ella.

### Polimorfismo
Se ve en `MetodoPago` y sus hijas. La clase `Factura` usa cualquier método de pago con `pagar(metodo_pago)`, y cada tipo de pago responde de forma distinta.

## Flujo de prueba

El programa crea un cliente, registra dos mascotas, atiende una mascota con un veterinario, crea una consulta, agrega dos tratamientos, calcula el total y realiza pagos con diferentes métodos.# PythonHospital
