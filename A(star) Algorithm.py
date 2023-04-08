# Algoritma A* bekerja dengan mengevaluasi setiap node dalam graf, di mana node-node ini diurutkan berdasarkan 
# nilai f(n) = g(n) + h(n), di mana g(n) adalah jarak terpendek saat ini dari node awal ke node n dan h(n) adalah 
# fungsi heuristik yang memberikan estimasi jarak terpendek dari node n ke node tujuan.
# Setelah ditemukan jalur terpendek, kode ini mencetak jalur dan jaraknya menggunakan fungsi print_shortest_path().

# Fungsi heuristik untuk goal Surabaya
heuristic = {
    'Magetan': 162,
    'Surabaya': 0,
    'Ngawi': 130,
    'Ponorogo': 128,
    'Madiun': 126,
    'Bojonegoro': 60,
    'Nganjuk': 70,
    'Jombang': 36,
    'Lamongan': 36,
    'Gresik': 12,
    'Sidoarjo': 22,
    'Probolinggo': 70,
    'Situbondo': 146,
    'Bangkalan': 140,
    'Sampang': 90,
    'Pamekasan': 104,
    'Sumenep': 150
}

# Definisikan graf sebagai dictionary of dictionary
graf = {
    'Magetan': {'Ngawi': 32, 'Ponorogo': 34, 'Madiun': 22},
    'Ngawi': {'Magetan': 32, 'Bojonegoro': 44, 'Madiun': 30, 'Nganjuk': 50},
    'Ponorogo': {'Magetan': 34, 'Madiun': 29},
    'Madiun': {'Magetan': 22, 'Ngawi': 30, 'Ponorogo': 29, 'Nganjuk': 48},
    'Bojonegoro': {'Ngawi': 44, 'Lamongan': 42, 'Jombang': 70, 'Nganjuk': 33},
    'Nganjuk': {'Madiun': 48, 'Ngawi': 50, 'Bojonegoro': 33, 'Jombang': 24},
    'Jombang': {'Bojonegoro': 70, 'Nganjuk': 24, 'Surabaya': 72},
    'Lamongan': {'Bojonegoro': 42, 'Gresik': 14},
    'Gresik': {'Lamongan': 14, 'Surabaya': 12},
    'Surabaya': {'Gresik': 12, 'Bangkalan': 44, 'Sidoarjo': 25},
    'Bangkalan': {'Surabaya': 44, 'Sampang': 52},
    'Sampang': {'Bangkalan': 52, 'Pamekasan': 31},
    'Pamekasan': {'Sampang': 31, 'Sumenep': 54},
    'Sumenep': {'Pamekasan': 54},
    'Sidoarjo': {'Surabaya': 25, 'Probolinggo': 78},
    'Probolinggo': {'Sidoarjo': 78, 'Situbondo': 99},
    'Situbondo': {'Probolinggo': 99}
}

def heuristic_distance(current, heuristic_dict):
    return heuristic_dict[current]

def astar(graph, start, goal, heuristic_func):
    # initialize the starting values
    g = {start: 0}
    f = {start: heuristic_func(start, heuristic)}
    visited = set()
    parent = {}
    # search for the shortest path
    while f:
        current_node = min(f, key=f.get)
        if current_node == goal:
            path = []
            while current_node in parent:
                path.append(current_node)
                current_node = parent[current_node]
            path.append(start)
            path.reverse()
            return path

        visited.add(current_node)
        del f[current_node]

        for neighbor, cost in graph[current_node].items():
            if neighbor in visited:
                continue
            tentative_g = g[current_node] + cost
            if neighbor not in f or tentative_g + heuristic_func(neighbor, heuristic) < f[neighbor]:
                g[neighbor] = tentative_g
                f[neighbor] = tentative_g + heuristic_func(neighbor, heuristic)
                parent[neighbor] = current_node

    # no path found
    return None

def print_shortest_path(graph, start, goal, heuristic_func):
    path = astar(graph, start, goal, heuristic_func)
    if path is not None:
        print(f"The shortest path from {start} to {goal} is:")
        print(" -> ".join(path))
        distance = 0
        for i in range(len(path) - 1):
            distance += graph[path[i]][path[i + 1]]
        print(f"The distance is: {distance}")
    else:
        print(f"No path found from {start} to {goal}.")

print_shortest_path(graf, "Magetan", "Surabaya", heuristic_distance)