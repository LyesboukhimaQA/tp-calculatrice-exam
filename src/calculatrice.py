
def division(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Division par zéro impossible")
    return float(a / b)


def puissance(a: float, n: int) -> float:
    if n < 0:
        raise ValueError("L'exposant ne peut pas être négatif")
    return float(a ** n)


def moyenne(notes: list[float]) -> float:
    if not notes:
        raise ValueError("La liste des notes ne peut pas être vide")
    return float(sum(notes) / len(notes))