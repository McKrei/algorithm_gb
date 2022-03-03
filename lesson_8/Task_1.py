'''
На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
'''

def func_graph(n):
    graph = []

    for one in range(n):
        for two in range(one, n):
            if one != two:
                graph.append((one, two))

    return len(graph)


friend = int(input('Сколько было друзей: '))
print('Количество рукопожатий: ', func_graph(friend))