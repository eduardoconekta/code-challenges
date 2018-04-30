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
from time import sleep
class Ooyala:
  def merge_sort(self, l1, l2):
    result = []
    # validations
    if self.__is_not_ascendent_list(l1) and self.__is_not_ascendent_list(l2):
      raise ValueError('list 1 or list 2 are not ascendent list`s.')
    c1 = 0
    c2 = 0
    while True:
      if c1 == len(l1) and c2 == len(l2):
        if self.__is_not_ascendent_list(result) or self.is_well_sorted(result):
          break
        c1 = 0
        c2 = 0
        
        
      if l1[c1] == l2[c2]:
        sum_values = l1[c1]['value'] + l2[c2]['value']
        result.append({ 'timestamp': l1[c1]['timestamp'], 'value': sum_values })
      elif l1[c1] < l2[c2]: 
        result.append(l1[c1])
        result.append(l2[c2])
      elif l1[c1] > l2[c2]: 
        result.append(l2[c2])
        result.append(l1[c1])
      c1 +=1
      c2 +=1
    return self.__sort(result)

# Public functions 
  def is_well_sorted(self,l):
    list_length = len(l)
    flag = True
    for i in xrange(0, list_length - 1):
      if l[i] >= l[i + 1]: 
        flag = False
    return flag

# Private functions
  def __sort(self, l):
    done = True
    while done:
      done = False
      for i in xrange(0 , len(l) - 1):
        if l[i] > l[i + 1]:
          tmp_pos = l[i + 1]
          l[i + 1 ] = l[i]
          l[i] = tmp_pos
          done = True
    return l

  def __is_not_ascendent_list(self, l):
    list_length = len(l)
    for i in xrange(0, list_length  - 1):
      if l[i]['timestamp'] > l[i + 1]['timestamp'] :
        return True
    return False
