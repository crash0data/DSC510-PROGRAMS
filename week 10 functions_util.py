'''
to_int function
'''
def to_int(input_value):
    try:
        return int(float(input_value))
    except ValueError:
        return None

'''
get_value function
'''
def get_value(items, value):
    try:
        return items.index(value)
    except:
        try:
            return items[value]
        except:
            return None
