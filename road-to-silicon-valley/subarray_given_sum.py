import os
from time import sleep
class SubArrayGivenSum:
    def calculate(self, arr, given_sum):
        result_found = True
        tmp_sum = 0
        current = 0
        start_from = 0
        sub_arr = arr[start_from:]
        while result_found:
            if start_from == len(arr)-1:
                return -1
            tmp_sum = tmp_sum + int(sub_arr[current])
            current = current + 1
            if current == len(arr)-1:
                start_from = start_from +1
                sub_arr = arr[start_from:]
                current = 0
                tmp_sum = 0
            if given_sum == tmp_sum:
                result_found = False
            
        if result_found:
            return -1
        return [start_from +1 , current +1]
    def read_input_case(self):
        return open('subarray_case.txt', 'r')
    
    def execute(self):
        new_sub_arr = self.clean_file[1:]
        registry_counter = 0
        while registry_counter < len(new_sub_arr):
            sum = new_sub_arr[registry_counter].rstrip().split(' ')[:1][0]
            arr = new_sub_arr[registry_counter+1].rstrip().split(' ')
            print ' '.join(str(i) for i in self.calculate(arr, int(sum)))
            if registry_counter+2 > len(new_sub_arr):
                break
            registry_counter = registry_counter + 2
            
            
        
            
            
    # constructor
    def __init__(self):
        file = self.read_input_case()
        self.clean_file = file.readlines()
        self.cases = self.clean_file[0]
        
            
            


sub = SubArrayGivenSum()
sub.execute()
