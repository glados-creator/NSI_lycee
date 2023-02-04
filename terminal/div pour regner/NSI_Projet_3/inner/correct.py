import matplotlib.pyplot as plt

def plot_pareto_frontier(Xs, Ys, maxX=True, maxY=True):
    '''Pareto frontier selection process'''
    sorted_list = sorted([[Xs[i], Ys[i]] for i in range(len(Xs))], reverse=maxY)
    pareto_front = [sorted_list[0]]
    for pair in sorted_list[1:]:
        if maxY:
            if pair[1] >= pareto_front[-1][1]:
                pareto_front.append(pair)
        else:
            if pair[1] <= pareto_front[-1][1]:
                pareto_front.append(pair)
    
    '''Plotting process'''
    plt.scatter(Xs,Ys)
    pf_X = [pair[0] for pair in pareto_front]
    pf_Y = [pair[1] for pair in pareto_front]
    # print(pf_X,pf_Y)
    plt.plot(pf_X, pf_Y,c="r",marker="x")
    plt.xlabel("Objective 1")
    plt.ylabel("Objective 2")
    plt.show()
    return [(pf_X[i],pf_Y[i]) for i,_ in enumerate(pf_X)][::-1]

# plot_pareto_frontier([x[i][0] for i,_ in enumerate(x)],[x[i][1] for i,_ in enumerate(x)])