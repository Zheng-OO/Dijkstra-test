import random
import heapq

def generate_cost_matrix(n):
    # 生成n*n大小的成本矩阵，初始化所有元素为无穷大
    cost_matrix = [[float('inf') for _ in range(n)] for _ in range(n)]

    # 随机生成成本值
    for i in range(n):
        for j in range(n):
            if i != j:
                # 随机生成非对角线上的成本值，这里使用1到10的范围
                cost_matrix[i][j] = random.randint(1, 10)

    return cost_matrix

def dijkstra(cost_matrix, start, end):
    n = len(cost_matrix)
    if start[0] >= n or start[1] >= n or end[0] >= n or end[1] >= n:
        raise ValueError("Invalid start or end index")

    start_node = start[0] * n + start[1]
    end_node = end[0] * n + end[1]

    # 记录节点是否被访问过
    visited = [False] * (n * n)
    # 记录起始点到各点的最短距离，初始化为无穷大
    distances = [float('inf')] * (n * n)
    distances[start_node] = 0

    # 使用堆来实现优先队列，保存节点的距离和节点编号
    priority_queue = [(0, start_node)]

    while priority_queue:
        # 从优先队列中弹出当前距离最小的节点
        current_distance, current_node = heapq.heappop(priority_queue)

        if visited[current_node]:
            continue

        visited[current_node] = True

        # 遍历当前节点的所有邻居
        for neighbor in range(n * n):
            row, col = neighbor // n, neighbor % n
            weight = cost_matrix[current_node % n][col]
            if not visited[neighbor] and weight != float('inf'):
                # 计算新的距离
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    # 如果新的距离更小，则更新距离并加入优先队列
                    distances[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))

    # 如果终点的最短距离仍然是无穷大，则表示无法到达
    if distances[end_node] == float('inf'):
        return "No path available."
    else:
        # 返回起始点到终点的最短路径成本
        return distances[end_node]

# 生成一个5*5的成本矩阵示例
n = 5
cost_matrix = generate_cost_matrix(n)

# 打印生成的成本矩阵
print("Cost Matrix:")
for row in cost_matrix:
    print(row)

# 选择起始点和终点坐标，这里选择(0, 0)到(4, 4)
start_point = (0, 0)
end_point = (4, 4)

# 计算最短路径的成本
shortest_path_cost = dijkstra(cost_matrix, start_point, end_point)

print(f"\nShortest Path Cost from {start_point} to {end_point}: {shortest_path_cost}")