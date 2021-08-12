
def max( x, y ):

    if x > y:

        return x

    return y

def maxx( x, y, z ):

    return max( x, max( y, z ) )

print("max number is ",maxx(3, 6, 90))