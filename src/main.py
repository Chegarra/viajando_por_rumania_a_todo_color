from data.grafo import grafo

import heapq
import argparse


def dijkstra(inicio: str, destino: str, grafo: dict) -> tuple[float, list[str]]:
    """
    Calcula la ruta más corta desde un nodo de inicio a un nodo de destino
    usando el algoritmo de Dijkstra.

    :param inicio: El nodo de inicio.
    :param destino: El nodo de destino.
    :param grafo: El grafo representado como un diccionario de adyacencia.
    :return: Una tupla con la distancia total y la lista de nodos en la ruta.
             Si no hay ruta, la distancia es infinita y la ruta está vacía.
    """

    distancias = {nodo: float("inf") for nodo in grafo}
    predecesores = {nodo: None for nodo in grafo}
    distancias[inicio] = 0
    cola_prioridad = [(0, inicio)]
    num_iteraciones = 0

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        # Si encontramos el destino, podemos reconstruir la ruta y terminar.
        if nodo_actual == destino:
            ruta = []
            paso = destino
            while paso is not None:
                ruta.append(paso)
                paso = predecesores[paso]

            print(f"Número de pasos realizados: {num_iteraciones}")
            return distancia_actual, ruta[::-1]  # Devolver la ruta en orden correcto

        if distancia_actual > distancias[nodo_actual]:
            continue

        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                predecesores[vecino] = nodo_actual # type: ignore
                heapq.heappush(cola_prioridad, (distancia, vecino))
            num_iteraciones += 1

        num_iteraciones += 1

    return float("inf"), []


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="VIAJANDO POR RUMANIA EN COLOR - VER. DIJKSTRA",
        description="Calcula la ruta más corta entre dos nodos usando Dijkstra.",
        epilog="Programación realizada por Chema Segarra"
        )

    parser.add_argument("inicio", type=str, default="Lugoj", help="Ciudad de partida (ver mapa)")
    parser.add_argument("destino", type=str, default="Bucharest", help="Ciudad de destino (ver mapa)")
    args = parser.parse_args()

    inicio = args.inicio
    destino = args.destino

    distancia_total, ruta_corta = dijkstra(inicio, destino, grafo)

    if distancia_total != float("inf"):
        print(f"La ruta más corta desde {inicio.upper()} hasta {destino.upper()} es:")
        print(f"Ruta: {' -> '.join(ruta_corta)}")
        print(f"Distancia total: {distancia_total}")
    else:
        print(f"No se encontró una ruta desde {inicio.upper()} hasta {destino.upper()}.")