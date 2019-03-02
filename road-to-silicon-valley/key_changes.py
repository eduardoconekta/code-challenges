'''
 
 renameKeys(map, kmap)
 
 Returns the map with the keys in kmap renamed to the vals in kmap
 
 renameKeys({a: 1, b: 2}, {a: ‘newA’, b: ‘newB’})
 => {newA: 1, newB: 2}
 
 renameKeys({a: 1}, {b: ‘newB’})
 => {a: 1}
 
 renameKeys({a: 1, b: 2}, {a: ‘b’})
 => {b: 1}
 
 renameKeys({a: 1, b: 2}, {a: ‘b’, b: ‘a’})
 => {b: 1, a: 2}
  

=> 0(n^2)
def rename_keys(xmap, kmap):
    temp_map = {}
    for current_position in kmap: # O(n)
        for left_map in xmap: # O(n)
            if current_position == left_map:
                temp_map[kmap[current_position]] = xmap[left_map]
    if len(temp_map ) == 0:
        return xmap
    return temp_map
'''

# => O(n)
def rename_keys(xmap, kmap):
    temp_map = {}
    for current_key in kmap:
        if xmap.has_key(current_key):
            temp_map[kmap[current_key]] = xmap[current_key]
    if len(temp_map) == 0:
        return xmap
    return temp_map
    

case_1_xmap = {"a": 1,"b": 2}
case_1_kmap = {"a": 'newA', "b": 'newB'}

case_2_xmap = {"a": 1}
case_2_kmap = {"b": 'newB'}

case_3_xmap = {"a": 1, "b": 2}
case_3_kmap = {"a":'b'}

case_4_xmap = {"a": 1, "b": 2} 
case_4_kmap = {"a":'b', "b": 'a'}


print rename_keys(case_1_xmap, case_1_kmap )
print rename_keys(case_2_xmap, case_2_kmap )
print rename_keys(case_3_xmap, case_3_kmap )
print rename_keys(case_4_xmap, case_4_kmap )


