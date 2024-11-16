# line plot
import matplotlib.pyplot as plt
v = plt.plot([1,2,3],[4,5,6],color="red")
v1 =plt.plot([1,2,3],[3,4,6],color="green")
plt.xlim(1,3)
plt.ylim(1,6)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("DEMO GRAPH")
plt.legend(['values','data'])
plt.show()