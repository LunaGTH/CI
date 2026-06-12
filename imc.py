def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC).

    Args:
        peso (float): Peso en kilogramos.
        altura (float): Altura en metros.

    Returns:
        float: Valor del IMC.

    Raises:
        ValueError: Si peso o altura son menores o iguales a cero.
        TypeError: Si los parámetros no son numéricos.
    """

    if not isinstance(peso, (int, float)):
        raise TypeError("El peso debe ser numérico")

    if not isinstance(altura, (int, float)):
        raise TypeError("La altura debe ser numérica")

    if peso <= 0:
        raise ValueError("El peso debe ser mayor que cero")

    if altura <= 0:
        raise ValueError("La altura debe ser mayor que cero")

    return peso / (altura ** 2)


if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    peso = float(input("Ingrese su peso (kg): "))
    altura = float(input("Ingrese su altura (m): "))

    resultado = calcular_imc(peso, altura)

    print(f"\nNombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"IMC: {resultado:.2f}")