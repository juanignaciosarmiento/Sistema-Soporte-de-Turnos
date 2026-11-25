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

def registrar_incidente(titulo, descripcion, prioridad, estado):
    """Valida y agrega el incidente a la lista. Devuelve (ok, mensaje)."""
    error = validar_incidente(titulo, descripcion, prioridad, estado)
    if error:
        return False, error

    incidente = {
        "titulo": titulo.strip(),
        "descripcion": descripcion.strip(),
        "prioridad": prioridad,
        "estado": estado,
    }
    incidentes.append(incidente)
    return True, "Incidente registrado correctamente."


def listar_incidentes():
    return incidentes

def elegir_opcion(texto, opciones):
    """Muestra las opciones numeradas y devuelve la elegida (o None si es inválida)."""
    print(texto)
    for i, opcion in enumerate(opciones, start=1):
        print(f"  {i}. {opcion}")
    eleccion = input("Elija una opción: ").strip()
    if eleccion.isdigit() and 1 <= int(eleccion) <= len(opciones):
        return opciones[int(eleccion) - 1]
    return None
