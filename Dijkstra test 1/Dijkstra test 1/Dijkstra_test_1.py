import random
import heapq

def generate_cost_matrix(n):
    # ����n*n��С�ĳɱ����󣬳�ʼ������Ԫ��Ϊ�����
    cost_matrix = [[float('inf') for _ in range(n)] for _ in range(n)]

    # ������ɳɱ�ֵ
    for i in range(n):
        for j in range(n):
            if i != j:
                # ������ɷǶԽ����ϵĳɱ�ֵ������ʹ��1��10�ķ�Χ
                cost_matrix[i][j] = random.randint(1, 10)

    return cost_matrix

def dijkstra(cost_matrix, start, end):
    n = len(cost_matrix)
    if start[0] >= n or start[1] >= n or end[0] >= n or end[1] >= n:
        raise ValueError("Invalid start or end index")

    start_node = start[0] * n + start[1]
    end_node = end[0] * n + end[1]

    # ��¼�ڵ��Ƿ񱻷��ʹ�
    visited = [False] * (n * n)
    # ��¼��ʼ�㵽�������̾��룬��ʼ��Ϊ�����
    distances = [float('inf')] * (n * n)
    distances[start_node] = 0

    # ʹ�ö���ʵ�����ȶ��У�����ڵ�ľ���ͽڵ���
    priority_queue = [(0, start_node)]

    while priority_queue:
        # �����ȶ����е�����ǰ������С�Ľڵ�
        current_distance, current_node = heapq.heappop(priority_queue)

        if visited[current_node]:
            continue

        visited[current_node] = True

        # ������ǰ�ڵ�������ھ�
        for neighbor in range(n * n):
            row, col = neighbor // n, neighbor % n
            weight = cost_matrix[current_node % n][col]
            if not visited[neighbor] and weight != float('inf'):
                # �����µľ���
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    # ����µľ����С������¾��벢�������ȶ���
                    distances[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))

    # ����յ����̾�����Ȼ����������ʾ�޷�����
    if distances[end_node] == float('inf'):
        return "No path available."
    else:
        # ������ʼ�㵽�յ�����·���ɱ�
        return distances[end_node]

# ����һ��5*5�ĳɱ�����ʾ��
n = 5
cost_matrix = generate_cost_matrix(n)

# ��ӡ���ɵĳɱ�����
print("Cost Matrix:")
for row in cost_matrix:
    print(row)

# ѡ����ʼ����յ����꣬����ѡ��(0, 0)��(4, 4)
start_point = (0, 0)
end_point = (4, 4)

# �������·���ĳɱ�
shortest_path_cost = dijkstra(cost_matrix, start_point, end_point)

print(f"\nShortest Path Cost from {start_point} to {end_point}: {shortest_path_cost}")