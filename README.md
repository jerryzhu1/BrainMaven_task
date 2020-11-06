![BrainMaven Logo](https://github.com/jerryzhu1/BrainMaven_task/blob/main/brainmaven_logo.jpg)

# BrainMaven_task (“Least-Recently Used” (LRU) Cache)

This is my answer for BrainMaven's TASK 1

This is a package for “Least-Recently Used” (LRU) Cache. LRU Cache will have its maximum capacity set at the time of the construction, and when adding
new keys that cause the capacity to be exceeded, the “least recently used” item will be identified and discarded. Both reading and writing the value of a key are considered the use of that key, and will update the key to "Most-Recent Used".

- ***source code***: LRU_Cache.py
- ***test code***:   test_LRU_Cache.py

## Table of content

- [Installation](#installation)
    - [python](#python)
    - [pytest](#pytest)
- [package_introduction](#package_introduction)
    - [Methods&Assumptions](#Methods&Assumptions)
        - [init](#init)
        - [put](#put)
        - [get](#get)
        - [delete](#delete)
        - [reset](#reset)
- [unit_test](#unit_test)
    - [test_init](#test_init)
        - [test_init_LRU_Cache_with_int](#test_init_LRU_Cache_with_int)
        - [test_init_LRU_Cache_with_float](#test_init_LRU_Cache_with_float)
        - [test_init_LRU_Cache_with_string_but_able_to_tranfrom_to_int](#test_init_LRU_Cache_with_string_but_able_to_tranfrom_to_int)
        - [test_init_LRU_Cache_with_negative_number](#test_init_LRU_Cache_with_negative_number)
        - [test_init_LRU_Cache_with_value_that_not_able_to_tranfrom_to_int](#test_init_LRU_Cache_with_value_that_not_able_to_tranfrom_to_int)
    - [test_put](#test_put)
        - [test_put_LRU_Cache_base](#test_put_LRU_Cache_base)
        - [test_put_LRU_Cache_remove_last_recent_used](#test_put_LRU_Cache_remove_last_recent_used)
        - [test_put_LRU_Cache_move_key_to_most_recent_used](#test_put_LRU_Cache_move_key_to_most_recent_used)
    - [test_get](#test_get)
        - [test_get_LRU_Cache_base](#test_get_LRU_Cache_base)
        - [test_get_LRU_Cache_remove_last_recent_used](#test_get_LRU_Cache_remove_last_recent_used)
    - [test_delete](#test_delete)
        - [test_delete_LRU_Cache_remove_key](#test_delete_LRU_Cache_remove_key)
    - [test_reset](#test_reset)
        - [test_reset_LRU_Cache](#test_reset_LRU_Cache)
- [run_unit_test](#run_unit_test)
    
## installation
### python
- This packaged is developed and tested under python 3.7.3 env, and anaconda env 3.7.

- Although not been tested, it should be safe to run with any version >= 3.6.

- Please download and install pure [**python**](https://www.python.org/downloads/release/python-373/) or [**anaconda**](https://www.anaconda.com/products/individual) if you don't have python installed with version >= 3.6.

### pytest

- This package is used for unit test purpose. Please use below command to install:

- `pip install pytest==4.3.1`

## package_introduction
### init

- ***description***: init method will take one input "size" and create empty LRU object.
- ***paramters***: ***size, int/float/string*** (maximum capacity of LRU object)
- ***assumptions***: 
    - the input of size is or can be transformed to type int (say string "5.5" or float 5.5), otherwise, it make no sense (say, size == 'Trump').
    - if int(float(size)) <= 0, it we will transform it to 0, because we allow with input size == -99, which should be same as size == 0.
    - If above 2 assumptions can't be satisfied, code will raise ValueError.
    
### put
- ***description***: put method will take input "key" and "value" to update the key-value pair into LRU object. 
- ***paramters***: ***key*** (key to store in LRU), ***value*** (corresponding value to store)
- ***assumptions***: 
    - put operation will update the key and move it to most recently used.
    - if the length of LRU_Cache exceed our maximum size, least recent used key-value pair will be removed.
    

### get
- ***description***: get method will take one input "key" and return corresponding value. 
- ***paramters***: ***key*** (key to extract value)
- ***assumptions***: 
    -  if key exist in cache, get method will return value and move the key to most recent used.
    -  if key not exist in cache, get method will return -1.
   

### delete
- ***description***: delete method remove input 'key' from LRU object. 
- ***paramters***: ***key*** (key to delete record)
- ***assumptions***: 
    - if key not exist in cache, code will do no operation.
    

### reset
- ***description***: reset method will remove all key-value pairs
- ***paramters***: ***N.A.***
- ***assumptions***: 
    - reset will keep original size
    

## unit_test
### test_init

#### test_init_LRU_Cache_with_int
- test init method when input size is integer

    ```
    LRU_Obj = LRU_Cache(2)
    assert LRU_Obj.size == 2
    ```


#### test_init_LRU_Cache_with_float
- test init method when input size is float
    ```
    LRU_Obj = LRU_Cache(2.5)
    assert LRU_Obj.size == 2
    ```

#### test_init_LRU_Cache_with_string_but_able_to_tranfrom_to_int
- When input size is string but can be transformed to integer
    ````
    LRU_Obj = LRU_Cache('5.5')
    assert LRU_Obj.size == 5
    ````
#### test_init_LRU_Cache_with_negative_number
- When input size is negative, size will be converted to 0
    ````
    LRU_Obj = LRU_Cache(-2)
    assert LRU_Obj.size == 0
    ````
    
#### test_init_LRU_Cache_with_value_that_not_able_to_tranfrom_to_int
- When input size can't be convert to int, raise ****ValueError****
    ```
    with pytest.raises(ValueError):
        LRU_Obj = LRU_Cache('Noise')
    ```


### test_put
#### test_put_LRU_Cache_base
- Test put method add new key-value to cache
    ```
    LRU_Obj = LRU_Cache(3)
    assert LRU_Obj.size == 3

    LRU_Obj.put('Toronto', 'ON')
    assert LRU_Obj.cache == OrderedDict([('Toronto', 'ON')])

    LRU_Obj.put('Washington', 'DC')
    assert LRU_Obj.cache == OrderedDict([('Toronto', 'ON'), ('Washington', 'DC')])
    ```
    
#### test_put_LRU_Cache_remove_last_recent_used
- When cache reach maximum size, drop less recent used record
    ```
    LRU_Obj = LRU_Cache(2)
    assert LRU_Obj.size == 2

    LRU_Obj.put('Toronto', 'ON')
    LRU_Obj.put('Washington', 'DC')
    assert LRU_Obj.cache == OrderedDict([('Toronto', 'ON'), ('Washington', 'DC')])

    LRU_Obj.put('Shanghai', 'SH')
    assert LRU_Obj.cache == OrderedDict([('Washington', 'DC'), ('Shanghai', 'SH')])
    
    LRU_Obj.put('Tokyo', 'Tokyo')
    assert LRU_Obj.cache == OrderedDict([('Shanghai', 'SH'), ('Tokyo', 'Tokyo')])
    ```

#### test_put_LRU_Cache_move_key_to_most_recent_used
- Test that put method will consider the key as used and move to most recent
    ```
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
    ```


### test_get
#### test_get_LRU_Cache_base
- Test get method will return corresponding value if key exist in cache, and -1 if not.
    ```
    LRU_Obj = LRU_Cache(3)
    assert LRU_Obj.size == 3

    LRU_Obj.put('Toronto', 'ON')
    LRU_Obj.put('Washington', 'DC')
    LRU_Obj.put('Shanghai', 'SH')
    
    assert LRU_Obj.cache == OrderedDict([('Toronto', 'ON'), ('Washington', 'DC'), ('Shanghai', 'SH')])
    assert LRU_Obj.get('Toronto') == 'ON'
    assert LRU_Obj.get('Mars') == -1
    ```

#### test_get_LRU_Cache_remove_last_recent_used
- When a key is read, it is considered used and move to most recent
    ```
    LRU_Obj = LRU_Cache(3)
    assert LRU_Obj.size == 3

    LRU_Obj.put('Toronto', 'ON')
    LRU_Obj.put('Washington', 'DC')
    LRU_Obj.put('Shanghai', 'SH')
    
    assert LRU_Obj.cache == OrderedDict([('Toronto', 'ON'), ('Washington', 'DC'), ('Shanghai', 'SH')])
    assert LRU_Obj.get('Toronto') == 'ON'
    assert LRU_Obj.cache == OrderedDict([('Washington', 'DC'), ('Shanghai', 'SH'), ('Toronto', 'ON')])
    ```
    
### test_delete
#### test_delete_LRU_Cache_remove_key
- When delete a key, if key exist, cache will remove the key-value pair. If not, code will do no operation.
    ```
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
    ```

### test_reset
#### test_reset_LRU_Cache
- When reset LRU_Cache object, cache will be reset as empty object with origin size.
    ```
    LRU_Obj = LRU_Cache(3)
    assert LRU_Obj.size == 3

    LRU_Obj.put('Toronto', 'ON')
    LRU_Obj.put('Washington', 'DC')
    LRU_Obj.put('Shanghai', 'SH')

    assert LRU_Obj.cache == OrderedDict([('Toronto', 'ON'), ('Washington', 'DC'), ('Shanghai', 'SH')])
    
    LRU_Obj.reset()
    
    assert LRU_Obj.size == 3
    assert LRU_Obj.cache == OrderedDict()
    ```
    
### run_unit_test
- Please cd to the dir of test_LRU_Cache.py and run below command:

    `pytest test_LRU_Cache.py`
    
- And you mey expect below result that indicate all unit tests passed:

    ```
    ================================================= test session starts =================================================
    platform win32 -- Python 3.7.3, pytest-4.3.1, py-1.8.0, pluggy-0.9.0
    rootdir: C:\Users\zhusi\Downloads\BrainMaven, inifile:
    plugins: remotedata-0.3.1, openfiles-0.3.2, doctestplus-0.3.0, arraydiff-0.3
    collected 12 items
    
    test_LRU_Cache.py ............                                                                                   [100%]
    
    ============================================== 12 passed in 0.12 seconds ==============================================
    ```
