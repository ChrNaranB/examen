distancias = {
    'santiago': {
        'buenos aires': 1400,
    },
}

def calcular_distancia(ciudad_origen, ciudad_destino):
    ciudad_origen = ciudad_origen.lower()
    ciudad_destino = ciudad_destino.lower()

    if ciudad_origen in distancias and ciudad_destino in distancias[ciudad_origen]:
        return distancias[ciudad_origen][ciudad_destino]
    else:
        return None

def calcular_duracion(distancia):
    velocidad_promedio = 80
    return distancia / velocidad_promedio

def calcular_combustible(distancia):
    consumo_combustible = 10  # 10 km/litro
    return distancia / consumo_combustible

ciudad_origen = input("Ciudad de Origen: ")
ciudad_destino = input("Ciudad de Destino: ")

distancia = calcular_distancia(ciudad_origen, ciudad_destino)

if distancia is not None:
    duracion = calcular_duracion(distancia)
    combustible = calcular_combustible(distancia)

    print("Distancia:", round(distancia, 3), "kms")
    print("Duración del viaje:", round(duracion, 3), "horas")
    print("Combustible requerido:", round(combustible, 3), "litros")

