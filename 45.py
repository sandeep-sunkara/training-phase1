#create a class F15 with functions lights,fans and ac
#lights=prints the colour of light which is taken as parameter to function
#fan=it displays the speed in which taken as parameter
#AC displays the room temp and the outside temp taken as parameters
#4th function whose name is display which displays the diff b/w outside and room temp and also displays fan speed
class F15:
    def lights(sandeep,color):
        print("the colour of light is:",color)
    def fan(sandeep,speed):
        sandeep.speed=speed
        print("the fan is rotating at a speed of:",speed)
    def AC(sandeep,rt,ot):
        sandeep.ot=ot
        sandeep.rt=rt
        print("the room temp is:",rt)
        print("the outside temp is:",ot)
    def tempdiff(sandeep):
        print("temp difference is:",(sandeep.ot-sandeep.rt))
        print("fan speed in tempdiff:",sandeep.speed)
    def __init__(self):
        print("this is constructor field written at last but printed at first")
        print("oohooo")
obj=F15()
obj.lights("white")
obj.fan(5)
obj.AC(28,35)
obj.tempdiff()