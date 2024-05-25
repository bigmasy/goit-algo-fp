import networkx as nx
import heapq

transport_network = nx.Graph()

stops = ['Зупинка 1', 'Зупинка 2','Зупинка 3', 'Зупинка 4',
         'Зупинка 5', 'Зупинка 6', 'Зупинка 7', 'Зупинка 8',
         'Зупинка 9', 'Зупинка 10', 'Зупинка 11', 'Зупинка 12']

transport_network.add_nodes_from(stops)

routes_1 = [
    ('Зупинка 2', 'Зупинка 1', {'route':'1'}),
    ('Зупинка 1', 'Зупинка 11', {'route':'1'}),
    ('Зупинка 11', 'Зупинка 4', {'route':'1'}),
    ('Зупинка 4', 'Зупинка 10', {'route':'1'}),
    ('Зупинка 10', 'Зупинка 12', {'route':'1'}),
]

routes_2 = [
    ('Зупинка 1', 'Зупинка 6', {'route':'2'}),
    ('Зупинка 6', 'Зупинка 11', {'route':'2'}),
    ('Зупинка 11', 'Зупинка 2', {'route':'2'}),
    ('Зупинка 2', 'Зупинка 3', {'route':'2'}),
    ('Зупинка 3', 'Зупинка 9', {'route':'2'}),
    ('Зупинка 9', 'Зупинка 4', {'route':'2'}),
    ('Зупинка 4', 'Зупинка 12', {'route':'2'}),
]

routes_3 = [
    ('Зупинка 1', 'Зупинка 7', {'route':'3'}),
    ('Зупинка 7', 'Зупинка 8', {'route':'3'}),
    ('Зупинка 8', 'Зупинка 9', {'route':'3'}),
    ('Зупинка 9', 'Зупинка 11', {'route':'3'}),
    ('Зупинка 11', 'Зупинка 3', {'route':'3'}),
]

routes_4 = [
    ('Зупинка 5', 'Зупинка 6', {'route':'4'}),
    ('Зупинка 6', 'Зупинка 7', {'route':'4'}),
    ('Зупинка 7', 'Зупинка 11', {'route':'4'}),
    ('Зупинка 11', 'Зупинка 10', {'route':'4'}),
    ('Зупинка 10', 'Зупинка 3', {'route':'4'}),
]
transport_network.add_edges_from(routes_1)
transport_network.add_edges_from(routes_2)
transport_network.add_edges_from(routes_3)
transport_network.add_edges_from(routes_4)

# Функція для знаходження найкоротших шляхів з використанням алгоритму Дейкстри
def dijkstra(graph, start_vertex):
    distances = {vertex: float('inf') for vertex in graph.nodes}
    distances[start_vertex] = 0
    min_heap = [(0, start_vertex)]

    while min_heap:
        current_distance, current_vertex = heapq.heappop(min_heap)

        for neighbor in graph.neighbors(current_vertex):
            distance = current_distance + graph[current_vertex][neighbor].get('weight', 1)

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances

# Викликаємо функцію і виводимо результат
start_stop = 'Зупинка 12'
shortest_paths = dijkstra(transport_network, start_stop)
print(f"Найкоротші шляхи з {start_stop}:")
for stop, distance in shortest_paths.items():
    print("До {}: {}".format(stop, distance))
