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