def add(*args):
    
    return sum(args)

print(add(5,6,7,7,3,43,34,43,453,543,53,54,45,3435,4,54,35,4,55))


def calculate(num, **kwargs):
    
    for key, value in kwargs.items():
        print(f"Key: {key}, Value: {value}")
        
calculate(10, one="two", two="three", three="four")