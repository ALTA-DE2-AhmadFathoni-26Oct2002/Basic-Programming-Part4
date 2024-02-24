def play_with_asterisk(n):
    pattern = ""
    for x in range (n):
        for sp in range (n-x-1):
            pattern += " "

        for y in range (x+1):
            pattern += '* '
            
        pattern += '\n'
    
    return pattern
        
if __name__ == '__main__':
    print(play_with_asterisk(5))
    """
        *
       * *
      * * *
     * * * *
    * * * * *
    """
