my_dict={ 'name':2,
           'age':1,
           'city':6,
           'uni':4}
 
sort=dict(sorted(my_dict.items(),key=lambda item:item[1]))
print(sort)
