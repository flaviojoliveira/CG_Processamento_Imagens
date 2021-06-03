def contains(self, point):
    import sys
    # _huge é usado para agir como infinito se acontecer uma divisão por 0
    _huge = sys.float_info.max
    # _eps é usado para ter certeza de que pontos não estão nas mesmas linhas que os vértices
    _eps = 0.00001

    # Começamos com o lado de fora do polígono
    inside = False
    for edge in self.edges:
        # Tenha certeza de que A é o ponto mais baixo da borda
        A, B = edge[0], edge[1]
        if A.y > B.y:
            A, B = B, A

        # Tenha certeza de que o ponto não está na mesma altura do vértice
        if point.y == A.y or point.y == B.y:
            point.y += _eps

        if (point.y > B.y or point.y < A.y or point.x > max(A.x, B.x)):
            # O raio horizontal não faz intersecção com a borda
            continue

        if point.x < min(A.x, B.x):  # O raio intersecta com a borda
            inside = not inside
            continue

        try:
            m_edge = (B.y - A.y) / (B.x - A.x)
        except ZeroDivisionError:
            m_edge = _huge

        try:
            m_point = (point.y - A.y) / (point.x - A.x)
        except ZeroDivisionError:
            m_point = _huge

        if m_point >= m_edge:
            # O raio intersecta com a borda
            inside = not inside
            continue

    return inside
