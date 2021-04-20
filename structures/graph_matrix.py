from random import Random

def gen_rand_list(x):
    res = []
    rand = Random()
    quot = x // 2 if x <=6 else x//3
    for _ in range(x):
        res.append(rand.randrange(0,quot))
    return res

def gen_rand_matrix(x):
    matrix = []
    for _ in range(x):
        matrix.append(gen_rand_list(x))
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def get_neighbors(matrix ,vert):
    x, y = vert
    neighbors = []
    x_delta = [-1, 0, 1, 0]
    y_delta = [0, 1, 0, -1]
    

    for i in range(len(x_delta)):
        x_neighbor = x + x_delta[i]
        y_neighbor = y + y_delta[i]
        if x_neighbor >= 0 and y_neighbor >= 0 and x_neighbor < len(matrix[0]) and y_neighbor < len(matrix):
            neighbors.append((x + x_delta[i], y + y_delta[i]))
    return neighbors

def flood_fill(image ,start, new_color):
    x, y = start
    init_color = image[x][y]
    neighbors = get_neighbors(image, start)
    print(f'**********************start = {x, y}, color: {init_color}************************')

    q = []
    visited = set()
    q.append(start)
    visited.add(start)

    while len(q) > 0:
        size = len(q)
        for _ in range(size): 
            c_x, c_y = q.pop()
            image[c_x][c_y] = new_color
            for n in get_neighbors(image, (c_x,c_y)):
                if n not in visited:
                    n_x, n_y = n
                    if image[n_x][n_y] == init_color:
                        q.append(n)
                        visited.add(n)
    return image


    

test_mtx = gen_rand_matrix(10)
print_matrix(test_mtx)
for r in flood_fill(test_mtx, (1,2), 8):
    print(r)




