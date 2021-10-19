def inputGraphParams() -> list:
    ''' 
    Вводим параметры для таблицы графа узлы
    и количество соединений
    '''
    print('Enter value of nodes:')
    connections: int
    nodes: int
    nodes = int(input())
    print('Enter value of connections')
    connections = int(input())
    graph = [[0]*nodes for _ in range(nodes)]
    incidentMatrix = [[0]*connections for _ in range(nodes)]
    return [graph,incidentMatrix]

def adjacencyTable(graph: list)->list:
    '''
    Заполняем таблицу смежности графа, вводя связи в алгебраическом виде
    Параметр "graph" - должен быть пустой матрицей смежности обрабатываемого графа
    '''
    status = True
    i: int
    j: int
    conn: str
    while status:
        print('Enter node connectctions Example: 1,2:')
        conn = input()
        if conn == '0':
            status=False
            continue
        i,j=[int(x)-1 for x in conn.split(',')]
        graph[i][j] = 1
        graph[j][i] = 1
    return graph

def showGraph(graph: list)->None:
    for lines in graph:
        for cols in lines:
            print(f'{cols} ', end='')
        print('\n')

def adjToKirgof(graph: list)->list:
    '''
    Конвертируем матрицу смежности в матрицу киргофа
    Параметр "graph" - должен быть заполненной матрицей смежности!
    '''
    for i in range(len(graph)):
        graph[i] = [0-_ if _==1 else 0 for _ in graph[i]]
        graph[i][i] = graph[i].count(-1)
    return graph

def kirchoffToIncident(graph: list, incidentMatrix: list) ->list:
    """
    Конвертируем матрицу киргофа а матрицу инцидентности
    Параметры: 
    "graph" - Должен быть заполненной матрицей Киргофа
    "incidentMatrix" - Должен быть пустой матрицей инцидентности!
    """
    counter = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == -1:
               incidentMatrix[i][counter],incidentMatrix[j][counter] = 1,1
        counter+=1 if counter< len(incidentMatrix[0])-1 else 0
    return incidentMatrix

def dfs(adjMatrix: list, start: int)-> None:
    """
    Итеративный обход графа в глубину
    """
    graph = [list() for _ in adjMatrix] # Creating list with graph's node's connections
    visited = [False for _ in adjMatrix] # Creating visited list if None
    stack = [start]
    for i in range(len(adjMatrix)):
        for j in range(len(adjMatrix)):
            if adjMatrix[i][j] == 1:
                graph[i].append(j) # Filling nodes connections list
    counter = 0
    while len(stack):
        counter+=1
        start = stack.pop() # Getting last element and remove it from list
        print(f'DFS LOG[{counter}]: Visited befor condition: {visited}')
        if not visited[start]: # If Node wasn't visited yet, visit it
            print(f'DFS[{counter}]: {start+1}')
            visited[start] = True
        print(f'DFS LOG[{counter}]: Visited after condition: {visited}')
        for node in graph[start]: # Collecting connections from node
            if not visited[node]:
                stack.append(node)
        print(f'DFS LOG[{counter}]: New stack: {stack}')

adjMatrix,incidentMatrix = inputGraphParams()
print('Nulled adjacency table:')
showGraph(adjMatrix)
adjMatrix = adjacencyTable(adjMatrix)
print('Filled adjacency table:')
showGraph(adjMatrix)
kirchoffMatrix = adjToKirgof(adjMatrix.copy())
print('Adjacency table -> Kirchoff matrix:')
showGraph(kirchoffMatrix)
print('Kirchoff matrix -> Incident matrix')
showGraph(kirchoffToIncident(kirchoffMatrix, incidentMatrix))
dfs(adjMatrix,0)
