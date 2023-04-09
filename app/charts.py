#Clase 31
import matplotlib.pyplot as plt #as plt es un sinonimo para no tener que copiar todo mas adelante

def generate_bar_chart(name,labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}.png')
  plt.close

def generate_pie_chart(labels, values):#grafica de torta
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  plt.savefig('pie.png')
  plt.close #cuando se ejecuta esto no deja ver mas graficas

if __name__ == '__main__':
  labels = ['a', 'b', 'c', 'd']
  values = [10, 40, 50, 5]
  generate_bar_chart(labels, values) #para ver una o la otra se debe hacer individual
  generate_pie_chart(labels, values)