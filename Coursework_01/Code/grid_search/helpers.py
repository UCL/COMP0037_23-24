# Clamp a variable such that min <= x <= max

def clamp(x, minimum, maximum):
    return max(minimum, min(x, maximum))
 
