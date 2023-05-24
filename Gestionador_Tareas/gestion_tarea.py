import click
import json

# Ruta del archivo de tareas
archivo_tareas = 'tareas.json'

def guardar_tareas():
    """Guarda las tareas en el archivo"""
    with open(archivo_tareas, 'w') as archivo:
        json.dump(tareas, archivo)

def cargar_tareas():
    """Carga las tareas desde el archivo"""
    try:
        with open(archivo_tareas, 'r') as archivo:
            tareas_cargadas = json.load(archivo)
            return tareas_cargadas
    except FileNotFoundError:
        return []

@click.group()
def gestion_tareas():
    pass

@gestion_tareas.command()
@click.argument('tarea')
def agregar(tarea):
    """Agrega una nueva tarea"""
    tareas.append(tarea)
    guardar_tareas()
    click.echo('Tarea agregada con éxito.')

@gestion_tareas.command()
@click.argument('indice', type=int)
def completar(indice):
    """Marca una tarea como completada"""
    if indice >= 0 and indice < len(tareas):
        tareas.pop(indice)
        guardar_tareas()
        click.echo('Tarea marcada como completada.')
    else:
        click.echo('Índice de tarea inválido.')

@gestion_tareas.command()
def ver():
    """Muestra la lista de tareas"""
    if len(tareas) > 0:
        click.echo('Lista de tareas:')
        for i, tarea in enumerate(tareas):
            click.echo(f'{i}. {tarea}')
    else:
        click.echo('No hay tareas.')

if __name__ == '__main__':
    tareas = cargar_tareas()
    gestion_tareas()
