def own_print(y):
    def my_print (x):
        return y + ' it\'s ' +  x
    return my_print

func = own_print('foo')
func('bar')
