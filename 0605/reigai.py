def calc( w, waru ):
    ans = w / waru 
    return ans

a = input( "enter number string:")
iA = int( a)

try:
    ret  =  calc( 10,  iA)
    print( ret)
except ZeroDivisionError:
    print( "計算ができません")
    
