#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
  
set = {a, b, c, d} // finite set, distinct elements

k = 3

subsets_of_size_k = {{a, b, c}, {a, b, d}, {a, c, d}, {b, c, d}}

question: write a program to output all the subsets of size k from a finite set

set = { a,b,c }

k = 2

subsets_of_size_k = {{a, b}, {a , c}, {b , c}} // output for k = 2

subsets_of_size_k = {{a, b, c}} // output for k =3


// k should be negative in some cases
// set should be arbitrary labels 

subsets_of_size_k = {
    {a, b, c}, 
    {a, b, d}, 
    {a, c, d}, 
    {b, c, d}
}

a b c x k(3)
a b x d
a x c d
x b c d

a b x k(2)
a x c
x b c

x y z  k(3) len(3)

'''

def process_set_permutation(subset_case, k):
    if len(subset_case) < 2 or k < 2:
        return subset_case
    result = []
    counter_decrement = k
    for j in range(0,len(subset_case)):
        res = ''
        for i,elem in enumerate(subset_case):
            if i != counter_decrement:
                res += elem
            else:
                counter_decrement -=1
                continue
        result.append(res)
        if counter_decrement == k:
            break
    return result

subset_case1 = ['x','y','z']
k1 = 3

subset_case2 = ['a','b','c','d']
k2 = 3

subset_case3 = ['a','b','c']
k3 = 2

subset_case4 = []
k4 = 1
print process_set_permutation(subset_case1, k1)
print process_set_permutation(subset_case2, k2)
print process_set_permutation(subset_case3, k3)
print process_set_permutation(subset_case4, k4)
