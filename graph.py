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
    '''
    for i in range(len(graph)):
        graph[i] = [0-_ if _==1 else 0 for _ in graph[i]]
        graph[i][i] = graph[i].count(-1)
    return graph

def kirgofToIncident(graph: list, incidentMatrix: list) ->list:
    counter = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == -1:
               incidentMatrix[i][counter],incidentMatrix[j][counter] = 1,1
        counter+=1 if counter< len(incidentMatrix[0])-1 else 0
    return incidentMatrix

graf,incidentMatrix = inputGraphParams()
print('Nulled adjacency table:')
showGraph(graf)
graf = adjacencyTable(graf)
print('Filled adjacency table:')
showGraph(graf)
graf = adjToKirgof(graf)
print('Adjacency table -> Kirgof matrix:')
showGraph(graf)
print('Kirgof matrix -> Incident matrix')
showGraph(kirgofToIncident(graf, incidentMatrix))
