class utils:

    def reversed(number):
        if isinstance(number,int):
            reversed = int(str(number)[::-1])
            return reversed
        
        print("The only input type accepted is an integer.")
        return None


    def formatter(number):
        if isinstance(number,int):
            return bin(number), oct(number)
        
        print("The only input type accepted is an integer.")
        return None
    