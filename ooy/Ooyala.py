#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Escribe una función que acepte dos entradas. 
Cada entrada es una lista de objetos, 
donde cada objeto tiene los atributos timestamp y value (ambos son enteros). 
Cada lista de entrada está ordenada por la clave timestamp, 
en orden ascendente. 
Tu función debe unir los elementos de ambas listas en una lista nueva, manteniéndola ordenada.
Además, si dos o más objetos tienen el mismo valor timestamp, 
entonces junta los objetos en uno solo, cuyo value es el resultado de la suma de cada value.
'''

class Ooyala:
  def sort(self, l1, l2):
    if self.__is_not_ascendent_list(l1) and self.__is_not_ascendent_list(l2):
      raise ValueError('list 1 or list 2 are not ascendent list`s.')
    
    list_1_length = len(l1)
    list_2_length = len(l2)
    for i in xrange(0, list_1_length -1):
      for j in xrange(0, list_2_length -1):
        if l1[i]['timestamp'] > l2[j]['timestamp']:  
          l1.append(l2[j])
          break
        elif l1[i] == l2[j]:
          sum_tmp = l1[i]['value'] + l2[j]['value']
          l1[i]['value'] = sum_tmp
          break
    return l1

  def __is_not_ascendent_list(self, l):
    list_length = len(l)
    for i in xrange(0, list_length -1 ):
      if l[i]['timestamp'] > l[i + 1]['timestamp'] :
        return True

    return False



     
