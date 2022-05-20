import pyperclip as pc

estudios = "Primaria | Secundaria | Preparatoria o bachillerato | Carrera técnica | Profesional | Maestría o Doctorado | Ninguno"
profesion = "Tecnología de Información | Ciencias naturales y exactas | Filosofía, idioma y letras | Ciencias sociales, administración y derecho | Ingenierías, manufactura y construcción | Artes y Humanidades | Agronomía y veterinaria | Salud | Servicios | Estudiante | Hogar | Servidor Público | Consultor | Otra Área"
ingresos = "No trabajo | $1 - $15,000 | $16,000 - $30,000 | $31,000 - $55,000 | >$50,000"


def process(text):
    return ", ".join(['"' + x.strip() + '"' for x in text.split("|")])

def form_len(text):
    return len(text.split("|"))

def format(text):
    return f"=ELEGIR(ALEATORIO.ENTRE(1,{form_len(text)}),{process(text)})"
    
pc.copy(format(ingresos))