import nose
from Ooyala import Ooyala

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

list_object_1_mixed = [
    {'timestamp': 1123830469, 'value': 321},
    {'timestamp': 1323830469, 'value': 123}, 
    {'timestamp': 1523830469, 'value': 345},
    {'timestamp': 1723830469, 'value': 543},
    {'timestamp': 1923830469, 'value': 567}
]

list_object_2_mixed = [
    {'timestamp': 1223830469, 'value': 321},
    {'timestamp': 1423830469, 'value': 123},
    {'timestamp': 1623830469, 'value': 345},
    {'timestamp': 1823830469, 'value': 543},
    {'timestamp': 2023830469, 'value': 567}
]

    
def test_sum_eq_values():
    ooyala_sorter = Ooyala()
    res           = ooyala_sorter.merge_sort(
        list_object_1, 
        list_object_2
    )
    sum_first_values = list_object_1[0]['value'] + list_object_2[0]['value']
    assert res[0]['value'] == sum_first_values
    assert ooyala_sorter.is_well_sorted(res)

def test_normal_behaviour():
    ooyala_sorter = Ooyala()
    res           = ooyala_sorter.merge_sort(
        list_object_1, 
        list_object_2
    )
    assert res != None
    assert ooyala_sorter.is_well_sorted(res)

def test_normal_behaviour_mixed_values():
    ooyala_sorter = Ooyala()
    res           = ooyala_sorter.merge_sort(
        list_object_1_mixed, 
        list_object_2_mixed
    )
    assert res != None
    assert ooyala_sorter.is_well_sorted(res)

def test_wrong_input_values():
    ooyala_sorter = Ooyala()
    res           = ooyala_sorter.merge_sort(
        list_object_1_wrong, 
        list_object_2
    )
    assert res != None
    assert not ooyala_sorter.is_well_sorted(res)
    