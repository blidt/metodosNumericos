def lagrangeInterpolation():
    p = []
    for i in range(len(points)):
        Li = {"y": points[i]["y"], "polynomial":[]}
        for j in range(len(points)):
            if j == i:
                continue
            Li["polynomial"].append({
                "sub": points[j]["x"], 
                "divisor": points[i]["x"] - points[j]["x"]
            })
        p.append(Li)
    return p

def evaluateLagrangePolynomial(p, x):
    y = 0
    for Li in p:
        prod = 1
        for term in Li["polynomial"]:
            prod *= (x - term["sub"])/term["divisor"]
        y += Li["y"]*prod
    return y