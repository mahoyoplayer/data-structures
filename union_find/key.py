n = 9

# Copy starting from here

rank = [0] * n
parent = list(range(n))

def find_parent(i: int) -> int: 
    if parent[i] != i:
        parent[i] = find_parent(parent[i])
    return parent[i]

def union(x: int, y: int) -> None: 
    p_x, p_y = find_parent(x), find_parent(y)
    if p_x == p_y:
        return
    if rank[p_x] == rank[p_y]:
        rank[p_x] += 1
        parent[p_y] = p_x
    elif rank[p_x] > rank[p_y]:
        parent[p_y] = p_x
    else:
        parent[p_x] = p_y


if __name__ == "__main__":
    print("Union Find")