#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
A stack is a data structure with four main operations (for our case, let’s assume it’s a stack of ints):

push(i):    Add i to the top of the stack
pop():      Remove and return the value on the top of the stack, raising an exception
            (e.g. IndexError or custom exception) if the stack is empty
peek():     Return, but do not remove, the value on the top of the stack, raising an
            exception if the stack is empty
is_empty(): Return a boolean that is true if there is nothing on the stack, and false
            otherwise

Given this definition, implement a new class called MaxStack.
It should have all the same functionality as a regular stack, as well as a function
that returns (but does not remove) the maximum value on the stack in O(1) time.
All other functions must continue to return in O(1) time.
'''


class MaxStack:
    def __init__(self):
        self.entire_stack = {}
        self.entire_stack['stack'] = []
        self.entire_stack['max_values'] = []

    def get_last_index(self):
        return len(self.entire_stack['max_values']) - 1

    def push(self, incoming):
        self.entire_stack['stack'].append(incoming)
        if len(self.entire_stack['max_values']) == 0:
            self.entire_stack['max_values'].append(incoming)
        elif incoming > self.entire_stack['max_values'][self.get_last_index()]:
            self.entire_stack['max_values'].append(incoming)

    def pop(self):
        if self.get_last_index() == 0:
            raise Exception('cannot pop anymore 😭')

        pop_value = self.entire_stack['stack'].pop()  # [4] => 5
        new_arr = []
        for i in self.entire_stack['max_values']:
            if i != pop_value:
                new_arr.append(i)
        self.entire_stack['max_values'] = new_arr
        return pop_value

    def is_empty(self):
        return len(self.entire_stack['stack']) == 0

    def peek(self):
        last = len(self.entire_stack['stack']) - 1
        return self.entire_stack['stack'][last]

    def max_value(self):
        return self.entire_stack['max_values'][self.get_last_index()]


stack = MaxStack()
stack.push(4)
stack.push(5)
print(stack.max_value())  # 5
stack.pop()
print(stack.max_value())  # 4
stack.peek()  # 4
stack.pop()
stack.pop()
