
def get_speed(dis,time):
    speed = dis / time  
    print(f'the speed is {speed}')

#calling
get_speed(2000,30)

distance = 3000
speed = 200
time =100
get_speed(distance,time)

get_speed(dis = 250,time=100)

get_speed(time=100,dis=3400)

# get_speed(200) # error

def pythagoras(perpendicular:int, base:int):
    hyp = (perpendicular**2 + base**2) **.5
    print(f'p = {perpendicular},b= {base} => h = {hyp}')

pythagoras(3,4)
pythagoras(23,34)