import correct
import projet_3

x = projet_3.lirePoints("data0.txt")
y = correct.plot_pareto_frontier([x[i][0] for i,_ in enumerate(x)],[x[i][1] for i,_ in enumerate(x)])
z= projet_3.EMPS(projet_3.Trier(x))
print(y == z)
assert y == z , (y,z)
x = projet_3.lirePoints("data1.txt")
y = correct.plot_pareto_frontier([x[i][0] for i,_ in enumerate(x)],[x[i][1] for i,_ in enumerate(x)])
z= projet_3.EMPS(projet_3.Trier(x))
print(y == z)
assert y == z , (y,z)
x = projet_3.lirePoints("data2.txt")
y = correct.plot_pareto_frontier([x[i][0] for i,_ in enumerate(x)],[x[i][1] for i,_ in enumerate(x)])
z= projet_3.EMPS(projet_3.Trier(x))
print(y == z)
assert y == z , (y,z)
x = projet_3.lirePoints("data3.txt")
y = correct.plot_pareto_frontier([x[i][0] for i,_ in enumerate(x)],[x[i][1] for i,_ in enumerate(x)])
z= projet_3.EMPS(projet_3.Trier(x))
print(y == z)
assert y == z , (y,z)