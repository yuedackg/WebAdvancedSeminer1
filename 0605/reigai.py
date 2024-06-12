def calc ( warareru, waru ):
    ans = warareru / waru
    return ans

a = input( "Enter number:")
iA = int( a )

print(  "calc 10 / a :" , end="")
try:
    retA = calc( 10, iA)
    print( retA)    

except ZeroDivisionError:
    print( "0での割り算が行われました。")

