from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def HolaMundo(request):
    fecha_hora = datetime.now()
    #doc_platilla = open("/home/jose/Escritorio/Proyectos_Django/my_web/my_web/Plantillas/mensaje.html")
    #doc_platilla = loader.get_template('mensaje.html')
    #plt = Template(doc_platilla.read())
    #doc_platilla.close()
    #ctx = Context({"Hora": fecha_hora.hour, "Minutos": fecha_hora.minute, "Segundos": fecha_hora.second})
    #mensaje = doc_platilla.render({"Hora": fecha_hora.hour, "Minutos": fecha_hora.minute, "Segundos": fecha_hora.second})
    return render(request, 'mensaje.html', {"Hora": fecha_hora.hour, "Minutos": fecha_hora.minute, "Segundos": fecha_hora.second})
