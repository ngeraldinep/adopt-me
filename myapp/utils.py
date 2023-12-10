from datetime import timedelta
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Fechas, Turno

def es_dia_laborable(fecha):
    # Verifica si la fecha es un día laborable (lunes a sábado)
    return 0 <= fecha.weekday() <= 5

def generar_fechas_automaticas(usuario, fecha_inicio, fecha_fin):
    # Obtén la lista de turnos disponibles
    turnos_disponibles = Turno.objects.filter(disponible=True)
    
    # Obtén el usuario actual
    usuario_actual = User.objects.get(username=usuario)

    # Lista para almacenar los datos generados
    ids = []
    fechas = []
    id_turnos = []
    disponibles = []
    info_adicional = []
    usuarios = []

    # Genera las fechas para cada turno en el rango especificado
    fecha_iterativa = fecha_inicio
    while fecha_iterativa <= fecha_fin:
        # Verifica si la fecha es un día laborable
        if es_dia_laborable(fecha_iterativa):
            for turno in turnos_disponibles:
                # Agrega los datos a las listas
                ids.append(None)
                fechas.append(fecha_iterativa)
                id_turnos.append(turno.id)
                disponibles.append(True)
                info_adicional.append('')
                usuarios.append(usuario_actual)

        # Incrementa la fecha para el siguiente día
        fecha_iterativa += timedelta(days=1)

    # Crea los objetos Fechas en la base de datos
    fechas_generadas = Fechas.objects.bulk_create([
        Fechas(
            fecha=fecha,
            id_turno_id=id_turno,
            disponible=disponible,
            info_adicional=info,
            usuario=usuario
        ) for fecha, id_turno, disponible, info, usuario in zip(
            fechas, id_turnos, disponibles, info_adicional, usuarios
        )
    ])

    return fechas_generadas