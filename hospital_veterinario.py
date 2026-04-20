from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class Persona(ABC):
    def __init__(self, nombre: str, documento: str) -> None:
        self.nombre = nombre
        self.documento = documento

    @abstractmethod
    def mostrar_rol(self) -> str:
        pass


class Veterinario(Persona):
    def __init__(self, nombre: str, documento: str, especialidad: str) -> None:
        super().__init__(nombre, documento)
        self.especialidad = especialidad

    def mostrar_rol(self) -> str:
        return f"Soy veterinario: {self.nombre}, especialista en {self.especialidad}."

    def atender_mascota(self, mascota: "Mascota") -> str:
        return f"{self.nombre} está atendiendo a {mascota.nombre}."


class Recepcionista(Persona):
    def mostrar_rol(self) -> str:
        return f"Soy recepcionista: {self.nombre}."

    def registrar_cliente(self, cliente: "Cliente") -> str:
        return f"{self.nombre} registró al cliente {cliente.nombre}."


class Cliente(Persona):
    def __init__(self, nombre: str, documento: str, telefono: str) -> None:
        super().__init__(nombre, documento)
        self.telefono = telefono
        self.mascotas: List[Mascota] = []

    def mostrar_rol(self) -> str:
        return f"Soy cliente: {self.nombre}."

    def agregar_mascota(self, mascota: "Mascota") -> str:
        self.mascotas.append(mascota)
        return f"Se agregó a {mascota.nombre} a las mascotas de {self.nombre}."

    def mostrar_mascotas(self) -> str:
        if not self.mascotas:
            return f"{self.nombre} no tiene mascotas registradas."
        lista = ", ".join(m.nombre for m in self.mascotas)
        return f"Mascotas de {self.nombre}: {lista}."


class Mascota:
    def __init__(self, nombre: str, especie: str, edad: int, peso: float) -> None:
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def mostrar_info(self) -> str:
        return (
            f"Mascota: {self.nombre}, especie: {self.especie}, "
            f"edad: {self.edad}, peso: {self.peso} kg."
        )


class Tratamiento:
    def __init__(self, nombre: str, costo: float, duracion_dias: int) -> None:
        self.nombre = nombre
        self.costo = costo
        self.duracion_dias = duracion_dias

    def mostrar_tratamiento(self) -> str:
        return (
            f"Tratamiento: {self.nombre}, costo: ${self.costo:.2f}, "
            f"duración: {self.duracion_dias} días."
        )


class Consulta:
    def __init__(self, mascota: Mascota, veterinario: Veterinario, motivo: str, diagnostico: str = "") -> None:
        self.mascota = mascota
        self.veterinario = veterinario
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.tratamientos: List[Tratamiento] = []

    def crear_tratamiento(self, nombre: str, costo: float, duracion_dias: int) -> Tratamiento:
        tratamiento = Tratamiento(nombre, costo, duracion_dias)
        self.tratamientos.append(tratamiento)
        return tratamiento

    def mostrar_resumen(self) -> str:
        resumen = [
            f"Consulta de {self.mascota.nombre} con el veterinario {self.veterinario.nombre}.",
            f"Motivo: {self.motivo}.",
            f"Diagnóstico: {self.diagnostico or 'Pendiente'}.",
        ]
        if self.tratamientos:
            tratamientos = " | ".join(t.mostrar_tratamiento() for t in self.tratamientos)
            resumen.append(f"Tratamientos: {tratamientos}.")
        else:
            resumen.append("Tratamientos: ninguno.")
        return "\n".join(resumen)

    def calcular_costo_consulta(self) -> float:
        return sum(tratamiento.costo for tratamiento in self.tratamientos)


class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto: float) -> str:
        pass


class PagoEfectivo(MetodoPago):
    def procesar_pago(self, monto: float) -> str:
        return f"Pago en efectivo procesado por ${monto:.2f}."


class PagoTarjeta(MetodoPago):
    def procesar_pago(self, monto: float) -> str:
        return f"Pago con tarjeta procesado por ${monto:.2f}."


class PagoTransferencia(MetodoPago):
    def procesar_pago(self, monto: float) -> str:
        return f"Pago por transferencia procesado por ${monto:.2f}."


class Factura:
    def __init__(self, consulta: Consulta, impuesto: float = 0.19) -> None:
        self.consulta = consulta
        self.subtotal = 0.0
        self.impuesto = impuesto
        self.total = 0.0

    def calcular_total(self) -> float:
        self.subtotal = self.consulta.calcular_costo_consulta()
        self.total = self.subtotal + (self.subtotal * self.impuesto)
        return self.total

    def pagar(self, metodo_pago: MetodoPago) -> str:
        total = self.calcular_total()
        return metodo_pago.procesar_pago(total)


def demostrar_sistema() -> None:
    cliente = Cliente("Felipe Rodriguez", "100200300", "3001234567")
    mascota1 = Mascota("Luna", "Perro", 4, 12.5)
    mascota2 = Mascota("Milo", "Gato", 2, 4.2)

    print(cliente.mostrar_rol())
    print(cliente.agregar_mascota(mascota1))
    print(cliente.agregar_mascota(mascota2))
    print(cliente.mostrar_mascotas())
    print(mascota1.mostrar_info())
    print(mascota2.mostrar_info())

    veterinario = Veterinario("Dr. Carlos Ruiz", "900800700", "Medicina interna")
    print(veterinario.mostrar_rol())
    print(veterinario.atender_mascota(mascota1))

    consulta = Consulta(mascota1, veterinario, "Vómito y falta de apetito")
    consulta.diagnostico = "Gastritis leve"
    tratamiento1 = consulta.crear_tratamiento("Suero intravenoso", 45000, 1)
    tratamiento2 = consulta.crear_tratamiento("Protector gástrico", 30000, 5)

    print(tratamiento1.mostrar_tratamiento())
    print(tratamiento2.mostrar_tratamiento())
    print(consulta.mostrar_resumen())

    factura = Factura(consulta)
    print(f"Subtotal: ${factura.consulta.calcular_costo_consulta():.2f}")
    print(f"Total con impuesto: ${factura.calcular_total():.2f}")

    pago_efectivo = PagoEfectivo()
    pago_tarjeta = PagoTarjeta()
    pago_transferencia = PagoTransferencia()

    print(factura.pagar(pago_efectivo))
    print(factura.pagar(pago_tarjeta))
    print(factura.pagar(pago_transferencia))


if __name__ == "__main__":
    demostrar_sistema()