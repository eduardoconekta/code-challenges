import nose
import Ooyala

# [{'timestamp': 1523830469, 'value': 246}, 
# {'timestamp': 1623830469, 'value': 321}, 
# {'timestamp': 2023830469, 'value': 321}, 
# {'timestamp': 1723830469, 'value': 345}, 
# {'timestamp': 2123830469, 'value': 345}, 
# {'timestamp': 1823830469, 'value': 543}, 
# {'timestamp': 2223830469, 'value': 543}, 
# {'timestamp': 1923830469, 'value': 567}, 
# {'timestamp': 2323830469, 'value': 567}]

list_object_1 = [
    {'timestamp': 1523830469, 'value': 123},
    {'timestamp': 1623830469, 'value': 321},
    {'timestamp': 1723830469, 'value': 345},
    {'timestamp': 1823830469, 'value': 543},
    {'timestamp': 1923830469, 'value': 567}
]

list_object_2 = [
    {'timestamp': 1523830469, 'value': 123},
    {'timestamp': 2023830469, 'value': 321},
    {'timestamp': 2123830469, 'value': 345},
    {'timestamp': 2223830469, 'value': 543},
    {'timestamp': 2323830469, 'value': 567}
]

list_object_1_wrong = [
    {'timestamp': 1623830469, 'value': 321},
    {'timestamp': 1523830469, 'value': 123}, # Not ascendent one
    {'timestamp': 1723830469, 'value': 345},
    {'timestamp': 1823830469, 'value': 543},
    {'timestamp': 1923830469, 'value': 567}
]

    
def test_sum_eq_values():
    ooyala_sorter = Ooyala.Ooyala()
    res           = ooyala_sorter.merge_sort(
        list_object_1, 
        list_object_2
    )
    print res
    sum_first_values = list_object_1[0]['value'] + list_object_2[0]['value']
    assert res[0]['value'] == sum_first_values

def test_normal_behaviour():
    ooyala_sorter = Ooyala.Ooyala()
    res           = ooyala_sorter.merge_sort(
        list_object_1, 
        list_object_2
    )
    assert res != None
    assert is_well_sorted(res)
    assert not duplicated_indexes(res)


def test_randomenes_values():
    assert True

def test_wrong_input_values():
    ooyala_sorter = Ooyala.Ooyala()
    res           = ooyala_sorter.merge_sort(
        list_object_1_wrong, 
        list_object_2
    )
    assert res != None
    assert not is_well_sorted(res)
    assert not duplicated_indexes(res)


def is_well_sorted(l):
    list_length = len(l)
    for i in xrange(0,  list_length -1):
      if l[i]['timestamp'] <= l[i + 1]['timestamp'] :
        return False
    return True

def duplicated_indexes(l):
    list_length = len(l)
    for i in xrange(0, list_length):
        for j in xrange(0, list_length -1):
            if l[i]['timestamp'] == l[j+1]['timestamp']:
                return True
    return False