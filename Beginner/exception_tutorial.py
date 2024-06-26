class valueToHighError(Exception):
    pass

class valueToSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
def test_value(x):
    if x > 100:
        raise valueToHighError("Value is too high")
    if x < 5:
        raise valueToSmallError(message="Value too small", value= x)
try:
    test_value(2)
except valueToSmallError as err:
    print(err.message + "," + str(err.value))