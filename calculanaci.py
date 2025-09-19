import datetime

def calc_dia_semana(fecha_str):
    try:
        fecha = datetime.datetime.strptime(fecha_str, "%d.%m.%Y")
        dias_semana = ["lunes", "martes", "miércoles","jueves","viernes","sábado", "domingo"]
        dia = dias_semana[fecha.weekday()]
        return f"Naciste un {dia}"
    except ValueError:
        return "Formato inválido. Usa dd.mm.aaaa (por ejemplo; 26.01.1989)."

if __name__ == "__main__":
    fecha_input = input("Ingresa tu fecha de nacimiento (dd.mm.aaaa):")
    result = calc_dia_semana(fecha_input)
print(f"Naciste un día: {result}")


