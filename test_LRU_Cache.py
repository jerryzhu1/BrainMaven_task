# test_LRU_Cache.py

import pytest
from LRU_Cache import LRU_Cache
from collections import OrderedDict

################ Test init method ###########
# When size is int 2,  it should be passed into LRU_Obj.size
def test_init_LRU_Cache_with_int():
    LRU_Obj = LRU_Cache(2)
    assert LRU_Obj.size == 2

# When size is float 2.5, it should be transformed into int 2 then pass into LRU_Obj.size
def test_init_LRU_Cache_with_float():
    LRU_Obj = LRU_Cache(2.5)
    assert LRU_Obj.size == 2

# When size is string 5.5, it should be transformed into float then int 2 and pass into LRU_Obj.size
def test_init_LRU_Cache_with_string_but_able_to_tranfrom_to_int():
    LRU_Obj = LRU_Cache('5.5')
    assert LRU_Obj.size == 5

# When size is smaller than 0,  it should passed 0 into LRU_Obj.size
def test_init_LRU_Cache_with_negative_number():
    LRU_Obj = LRU_Cache(-2)
    assert LRU_Obj.size == 0

# When size is string 'Noise', which can't be transformed int, code should raise ValueError
def test_init_LRU_Cache_with_value_that_not_able_to_tranfrom_to_int():
    with pytest.raises(ValueError):
        LRU_Obj = LRU_Cache('Noise')



################ Test PUT method ###########
# Test that put method will put key-value pair to LRU
def test_put_LRU_Cache_base():
    LRU_Obj = LRU_Cache(3)
    assert LRU_Obj.size == 3

    LRU_Obj.put('Toronto', 'ON')
    assert LRU_Obj.cache == OrderedDict([('Toronto', 'ON')])

    LRU_Obj.put('Washington', 'DC')
    assert LRU_Obj.cache == OrderedDict([('Toronto', 'ON'), ('Washington', 'DC')])

# Test that when Cache reach the max_size, it will remove the "last recent used" key-value pair
def test_put_LRU_Cache_remove_last_recent_used():
    LRU_Obj = LRU_Cache(2)
    assert LRU_Obj.size == 2

    LRU_Obj.put('Toronto', 'ON')
    LRU_Obj.put('Washington', 'DC')
    assert LRU_Obj.cache == OrderedDict([('Toronto', 'ON'), ('Washington', 'DC')])

    LRU_Obj.put('Shanghai', 'SH')
    assert LRU_Obj.cache == OrderedDict([('Washington', 'DC'), ('Shanghai', 'SH')])
    
    LRU_Obj.put('Tokyo', 'Tokyo')
    assert LRU_Obj.cache == OrderedDict([('Shanghai', 'SH'), ('Tokyo', 'Tokyo')])

# Test that when a key is write, it is considered used and move to most recent
def test_put_LRU_Cache_move_key_to_most_recent_used():
    LRU_Obj = LRU_Cache(3)
    assert LRU_Obj.size == 3

    LRU_Obj.put('Toronto', 'ON')
    LRU_Obj.put('Washington', 'DC')
    LRU_Obj.put('Shanghai', 'SH')
    assert LRU_Obj.cache == OrderedDict([('Toronto', 'ON'), ('Washington', 'DC'), ('Shanghai', 'SH')])
    
    LRU_Obj.put('Toronto', 'ON_2')
    assert LRU_Obj.cache == OrderedDict([('Washington', 'DC'), ('Shanghai', 'SH'), ('Toronto', 'ON_2')])

    
    LRU_Obj.get('Shanghai')
    assert LRU_Obj.cache == OrderedDict([('Washington', 'DC'), ('Toronto', 'ON_2'), ('Shanghai', 'SH')])


################ Test GET method ###########
# Test that get will return corresponding value if key exist in cache, or -1 if not.
def test_get_LRU_Cache_base():
    LRU_Obj = LRU_Cache(3)
    assert LRU_Obj.size == 3

    LRU_Obj.put('Toronto', 'ON')
    LRU_Obj.put('Washington', 'DC')
    LRU_Obj.put('Shanghai', 'SH')
    assert LRU_Obj.cache == OrderedDict([('Toronto', 'ON'), ('Washington', 'DC'), ('Shanghai', 'SH')])
    
    assert LRU_Obj.get('Toronto') == 'ON'

    assert LRU_Obj.get('Mars') == -1
    

# Test that when a key is read, it is considered used and move to most recent
def test_get_LRU_Cache_remove_last_recent_used():
    LRU_Obj = LRU_Cache(3)
    assert LRU_Obj.size == 3

    LRU_Obj.put('Toronto', 'ON')
    LRU_Obj.put('Washington', 'DC')
    LRU_Obj.put('Shanghai', 'SH')
    assert LRU_Obj.cache == OrderedDict([('Toronto', 'ON'), ('Washington', 'DC'), ('Shanghai', 'SH')])
    
    assert LRU_Obj.get('Toronto') == 'ON'
    
    assert LRU_Obj.cache == OrderedDict([('Washington', 'DC'), ('Shanghai', 'SH'), ('Toronto', 'ON')])

################ Test DELETE method ###########
# Test that when we delete a key, cache will remove the key-value pair if exist.
def test_delete_LRU_Cache_remove_key():
    LRU_Obj = LRU_Cache(3)
    assert LRU_Obj.size == 3

    LRU_Obj.put('Toronto', 'ON')
    LRU_Obj.put('Washington', 'DC')
    LRU_Obj.put('Shanghai', 'SH')
    assert LRU_Obj.cache == OrderedDict([('Toronto', 'ON'), ('Washington', 'DC'), ('Shanghai', 'SH')])
    
    LRU_Obj.delete('Toronto')
    
    assert LRU_Obj.cache == OrderedDict([('Washington', 'DC'), ('Shanghai', 'SH')])
    
    LRU_Obj.delete('Mars')
    
    assert LRU_Obj.cache == OrderedDict([('Washington', 'DC'), ('Shanghai', 'SH')])


################ Test RESET method ###########
# Test that when we reset LRU_Cache object, cache will be reset as empty object with origin size.
def test_reset_LRU_Cache():
    LRU_Obj = LRU_Cache(3)
    assert LRU_Obj.size == 3

    LRU_Obj.put('Toronto', 'ON')
    LRU_Obj.put('Washington', 'DC')
    LRU_Obj.put('Shanghai', 'SH')

    assert LRU_Obj.cache == OrderedDict([('Toronto', 'ON'), ('Washington', 'DC'), ('Shanghai', 'SH')])
    
    LRU_Obj.reset()

    assert LRU_Obj.size == 3
    
    assert LRU_Obj.cache == OrderedDict()

