'''

* Gap = TotalArreglo / 2 ? 

1.- Tener gap
  1.1 longitud total entre dos
  1.2 restas 1 en cada iteracion 

2.- iterar arreglo cada (Gap)
3.- comparar si el num es menor al indice actual
  3.1.- (Si) intercambia
  3.2.- (No) corta el ciclo sin hacer nada

print "{} {} ".format(arr[i],arr[j])

'''
class ShellSort(object):
  def sort(self, obj):
    longitud = len(arr)
    gap      = 2
    for i in range(longitud-gap):
        if arr[i] > arr[i + gap]:
            tmp   = arr[i]
            arr[i] = arr[i + gap]
            arr[i + gap] = tmp            
    return arr

     
  def __init__(self, arg=None):
    super(ShellSort, self).__init__()
    self.arg = arg


arr       = [5,4,2,6,8,17,9]
instancia = ShellSort()
res       = instancia.sort(arr)
print res


