import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title="Binary Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_heap(array):
    n = len(array)
    nodes = [Node(array[i]) for i in range(n)]

    for i in range(n):
        if 2*i + 1 < n:
            nodes[i].left = nodes[2*i + 1]
        if 2*i + 2 < n:
            nodes[i].right = nodes[2*i + 2]

    return nodes[0] if nodes else None

def generate_colors(n):
    colors = []
    for i in range(n):
        shade = hex(200 - (150 // n * i))[2:].zfill(2) 
        colors.append(f'#{shade}{shade}FF')
    return colors

def dfs(node, colors, index=0):
    if node is None:
        return index
    node.color = colors[index]
    index += 1
    index = dfs(node.left, colors, index)
    index = dfs(node.right, colors, index)
    return index

def bfs(root, colors):
    queue = [root]
    index = 0
    while queue:
        node = queue.pop(0)
        node.color = colors[index]
        index += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

heap_array = [0, 4, 5, 10, 1, 3]

root = build_heap(heap_array)

num_nodes = len(heap_array)

colors = generate_colors(num_nodes)

dfs(root, colors)
draw_tree(root, title="DFS")

root = build_heap(heap_array)

bfs(root, colors)
draw_tree(root, title="BFS")