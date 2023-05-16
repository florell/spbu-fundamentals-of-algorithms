from time import perf_counter
import networkx as nx

class Maze:
    def __init__(self, list_view: list[list[str]]) -> None:
        self.list_view = list_view
        self.start_j = None
        for j, sym in enumerate(self.list_view[0]):
            if sym == "O":
                self.start_j = j

    @classmethod
    def from_file(cls, filename):
        list_view = []
        with open(filename, "r") as f:
            for l in f.readlines():
                list_view.append(list(l.strip()))
        obj = cls(list_view)
        return obj

    def print(self, path="") -> None:
        # Find the path coordinates
        i = 0  # in the (i, j) pair, i is usually reserved for rows and j is reserved for columns
        j = self.start_j
        path_coords = set()
        for move in path:
            i, j = _shift_coordinate(i, j, move)
            path_coords.add((i, j))
        # Print maze + path
        for i, row in enumerate(self.list_view):
            for j, sym in enumerate(row):
                if (i, j) in path_coords:
                    print("+ ", end="")  # NOTE: end is used to avoid linebreaking
                else:
                    print(f"{sym} ", end="")
            print()  # linebreak


def plot_graph(G):
    options = dict(
        font_size=12,
        node_size=500,
        node_color='white',
        edgecolors="black",
    )
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, **options)
    if nx.is_weighted(G):
        labels = {e: G.edges[e]['weight'] for e in G.edges}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)


def solve(maze: Maze) -> None:
    path = ""  # solution as a string made of "L", "R", "U", "D"
    m = open('maze_2.txt').readlines()
    start = None
    end = None
    for j in range(len(m[0])):
        if m[0][j] == 'O':
            start = (0, j, '')
            break
    for j in range(len(m[-1])):
        if m[-1][j] == 'X':
            end = (len(m) - 1, j)
    queue = [start]
    checked = []
    while len(queue) != 0:
        t = queue.pop()
        if m[t[0]][t[1] - 1] != '#':
            if m[t[0]][t[1] - 1] == 'X':
                path = t[2]
            else:
                if (t[0], t[1] - 1) not in checked:
                    queue.append((t[0], t[1] - 1, t[2] + 'L'))
                    checked.append((t[0], t[1] - 1))
        if m[t[0] + 1][t[1]] != '#':
            if m[t[0] + 1][t[1]] == 'X':
                path = t[2]
            else:
                if (t[0] + 1, t[1]) not in checked:
                    queue.append((t[0] + 1, t[1], t[2] + 'D'))
                    checked.append((t[0] + 1, t[1]))
        if m[t[0]][t[1] + 1] != '#':
            if m[t[0]][t[1] + 1] == 'X':
                path = t[2]
            else:
                if (t[0], t[1] + 1) not in checked:
                    queue.append((t[0], t[1] + 1, t[2] + 'R'))
                    checked.append((t[0], t[1] + 1))

    print(f"Found: {path}")
    maze.print(path)


def _shift_coordinate(i: int, j: int, move: str) -> tuple[int, int]:
    if move == "L":
        j -= 1
    elif move == "R":
        j += 1
    elif move == "U":
        i -= 1
    elif move == "D":
        i += 1
    return i, j


if __name__ == "__main__":
    maze = Maze.from_file("maze_2.txt")
    t_start = perf_counter()
    solve(maze)
    t_end = perf_counter()
    print(f"Elapsed time: {t_end - t_start} sec")