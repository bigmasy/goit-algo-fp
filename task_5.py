from task_4 import*
import matplotlib.colors as mcolors
import colorsys
from collections import deque

def generate_shades(color, n):
    base_color = colorsys.rgb_to_hsv(*mcolors.to_rgb(color))
    return [colorsys.hsv_to_rgb(base_color[0], base_color[1] * (i / n), 1.0) for i in range(1, n + 1)]

def bfs_traversal(root, base_color='#1296F0'):
    if not root:
        return
    queue = deque([root])
    visited = set()
    order = 0
    color_map = generate_shades(base_color, 20)  # Generate lighter shades
    while queue:
        node = queue.popleft()
        if node.id not in visited:
            visited.add(node.id)
            node.color = mcolors.rgb2hex(color_map[order % len(color_map)])
            order += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def dfs_traversal(node, order=0, color_map=None, base_color='#1296F0'):
    if node is None:
        return order
    if color_map is None:
        color_map = generate_shades(base_color, 20)  # Generate lighter shades
    node.color = mcolors.rgb2hex(color_map[order % len(color_map)])
    order += 1
    order = dfs_traversal(node.left, order, color_map)
    order = dfs_traversal(node.right, order, color_map)
    return order


# Обхід дерева в ширину і візуалізація
bfs_traversal(heap_root)
draw_tree(heap_root)

# Обхід дерева в глибину і візуалізація
dfs_traversal(heap_root)
draw_tree(heap_root)
