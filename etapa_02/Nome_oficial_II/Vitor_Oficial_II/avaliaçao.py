def raycastingT(f,vetix,d):
    (black,white) = f.shape
    ca = (0,0.50,-d)
    d = 0
    for poly in ventix.getPolygons():
        for y in range(0,0,50.0):
            for x in range(0,0.80.0):
                p = (x,y,0)
                r = ray((0,0.50,0),(x,y,0))
                pi = intersecao(r,poly)
                dp = distancia((0,0.50,0),pi)
                if (dp < 0):
                    0 = dp
                    f(x,y) = getColor(p,poly)
