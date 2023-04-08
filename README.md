## Daftar Anggota :
1. Gabrielle Immanuel Osvaldo Kurniawan - 5025211135
3. Victor Gustinova                     - 5025211159

## Soal :

<img width="723" alt="image" src="https://user-images.githubusercontent.com/108170210/230701716-7a61383a-e7a6-41c2-9de7-c6e83910db5a.png">

## Jawab :

### Apa itu Greedy BFS ?

Greedy Best First Search adalah algoritma search jalur terpendek yang memilih node dengan heuristik terkecil (yang dianggap paling dekat dengan tujuan) sebagai node yang akan dieksplorasi berikutnya. Algoritma ini tidak mempertimbangkan biaya sebenarnya dari node yang dieksplorasi, namun hanya memperhatikan estimasi heuristik. Metode ini menggunakan priority queue untuk menyimpan himpunan node yang belum dieksplorasi.

### Implementasi 
```
from collections import defaultdict
import heapq 

#nilai heuristic
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

class Graph:
    #inisialisasi graf
    def __init__(self):
        self.graph = defaultdict(list)

    #menambahkan edge
    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))
    
    #fungsi gbfs, bekerja dengan melihat nilai heuristic terkecil dari neighbor yang ada. 
    #menggunakan heap1 (priority queue) untuk mencari nilai heuristic terkecil
    def gbfs(self, start, goal, heuristic):
        visited = set() 
        queue = [] 
        heapq.heappush(queue, (heuristic[start], start)) 
        while queue:
            (h, current) = heapq.heappop(queue)
            if current == goal: 
                print(f"Goal '{goal}' reached")
                return
            if current not in visited: 
                visited.add(current)
                print(f"Visited '{current}' with h={h}") 
                for neighbor, weight in self.graph[current]:
                    if neighbor not in visited:
                        heapq.heappush(queue, (heuristic[neighbor], neighbor))

g = Graph()
g.addEdge('Magetan', 'Ngawi', 32)
g.addEdge('Magetan', 'Madiun', 34)
g.addEdge('Magetan', 'Ponorogo', 22)
g.addEdge('Ngawi', 'Madiun', 30)
g.addEdge('Ngawi', 'Bojonegoro', 44)
g.addEdge('Madiun', 'Ponorogo', 29)
g.addEdge('Madiun', 'Nganjuk', 48)
g.addEdge('Bojonegoro', 'Nganjuk', 33)
g.addEdge('Bojonegoro', 'Lamongan', 42)
g.addEdge('Bojonegoro', 'Jombang', 70)
g.addEdge('Nganjuk', 'Jombang', 40)
g.addEdge('Jombang', 'Surabaya', 72)
g.addEdge('Lamongan', 'Gresik', 14)
g.addEdge('Gresik', 'Surabaya', 12)
g.addEdge('Surabaya', 'Sidoarjo', 25)
g.addEdge('Surabaya', 'Bangkalan', 44)
g.addEdge('Sidoarjo', 'Probolinggo', 78)
g.addEdge('Probolinggo', 'Situbondo', 99)
g.addEdge('Bangkalan', 'Sampang', 52)
g.addEdge('Sampang', 'Pamekasan', 31)
g.addEdge('Pamekasan', 'Sumenep', 54)

start = 'Magetan'
goal = 'Surabaya'

g.gbfs(start, goal, heuristic)
```

### Alur Greedy BFS
<img width="314" alt="image" src="https://user-images.githubusercontent.com/108170210/230701913-3ab905f9-6abf-4ad2-bcde-5d88c6285840.png">

### Berikut adalah output dari implementasi Greedy BFS
<img width="407" alt="image" src="https://user-images.githubusercontent.com/108170210/230701996-1376a225-cedc-4b3b-96e4-4d34eb7f3e1c.png">

### Referensi greedy BFS :
- PPT KB Informed Search
- Bahan asistensi 1 KB (Sabtu, 11/03/2023)
- https://www.javatpoint.com/ai-informed-search-algorithms

### Apa itu A* ?

Metode A* adalah algoritma search jalur terpendek yang menggabungkan cost dan heuristik untuk menentukan node yang paling menjanjikan untuk dieksplorasi. Pada pengevaluasian node, digunakan fungsi evaluasi f(n) = g(n) + h(n), di mana g(n) adalah biaya dari node sumber ke node saat ini dan h(n) adalah heuristik yang memperkirakan biaya tersisa ke node tujuan. Algoritma ini mengeksplorasi node dengan nilai f(n) terkecil terlebih dahulu dan terus memperbarui nilai f(n) untuk node-node yang belum dieksplorasi, sehingga mampu mencapai jalur terpendek dengan mempertimbangkan cost dan heuristik.

### Implementasi 
```
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
```
### Alur A* algorithm
<img width="368" alt="image" src="https://user-images.githubusercontent.com/108170210/230701947-6242aba4-54b6-46b6-a50b-5a7b36c7e0e1.png">

### Berikut adalah output dari implementasi A* Algorithm

<img width="470" alt="image" src="https://user-images.githubusercontent.com/108170210/230701447-a711e6d0-9bf8-4903-abb8-218836c852c6.png">

### Referensi A*: 
- PPT KB Informed Search
- https://stackoverflow.com/questions/58157354/python-create-a-graph-from-a-dictionary
- https://www.w3schools.com/python/python_dictionaries.asp
- https://www.youtube.com/watch?v=Y4tPnavVwKM 
