def draw_xyz(N):
    pattern = ""
    inc = 1
    for x in range(N):
        for y in range(N):
            if inc % 3 == 0:
                pattern += "X "
            elif inc % 2 == 0:
                pattern += "Z "
            else:
                pattern += "Y "
            inc = inc + 1
        pattern += '\n'
    return pattern
    

if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """


    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """