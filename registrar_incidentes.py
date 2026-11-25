#registrar_incidentes

PRIORIDADES = ["Baja", "Media", "Alta"]
ESTADOS = ["Abierto", "En proceso", "Resuelto"]

incidentes = []  # acá se guardan los incidentes registrados


def validar_incidente(titulo, descripcion, prioridad, estado):
    """Devuelve un mensaje de error, o None si los datos son válidos."""
    if titulo.strip() == "" or descripcion.strip() == "":
        return "Complete el título y la descripción del incidente."
    if prioridad not in PRIORIDADES:
        return "La prioridad debe ser Baja, Media o Alta."
    if estado not in ESTADOS:
        return "El estado debe ser Abierto, En proceso o Resuelto."
    return None
