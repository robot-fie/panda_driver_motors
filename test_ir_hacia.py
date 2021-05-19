import PCA9685
import time

pca9865 = PCA9685.PCA9865()

PWM_DUTY = 80
PWM_FREQ = 1000

right_front_EN = 0
right_front_IN_BW = 1
right_front_IN_FW = 2

left_front_EN = 7
left_front_IN_BW = 5
left_front_IN_FW = 6

left_back_EN = 10
left_back_IN_BW = 8
left_back_IN_FW = 9

right_back_EN = 12
right_back_IN_BW = 13
right_back_IN_FW = 14

pca9865.set_freq(PWM_FREQ)
pca9865.set_PWM(right_front_EN,0)
pca9865.set_PWM(right_front_IN_BW,0)
pca9865.set_PWM(right_front_IN_FW,0)

pca9865.set_PWM(right_back_EN,0)
pca9865.set_PWM(right_back_IN_BW,0)
pca9865.set_PWM(right_back_IN_FW,0)

pca9865.set_PWM(left_front_EN,0)
pca9865.set_PWM(left_front_IN_BW,0)
pca9865.set_PWM(left_front_IN_FW,0)

pca9865.set_PWM(left_back_EN,0)
pca9865.set_PWM(left_back_IN_BW,0)
pca9865.set_PWM(left_back_IN_FW,0)

MOTORS = (right_front_EN,
		  right_back_EN,
		  left_front_EN,
		  left_back_EN)

NORTH = (
	(right_front_IN_FW, PWM_DUTY),
	(right_back_IN_FW, PWM_DUTY),
	(left_front_IN_FW, PWM_DUTY),
	(left_back_IN_FW,PWM_DUTY)
	)
SOUTH = (
	(right_front_IN_BW, PWM_DUTY),
	(right_back_IN_BW, PWM_DUTY),
	(left_front_IN_BW, PWM_DUTY),
	(left_back_IN_BW,PWM_DUTY)
	)
EAST = (
	(right_front_IN_BW, PWM_DUTY),
	(right_back_IN_BW, PWM_DUTY),
	(left_front_IN_FW, PWM_DUTY),
	(left_back_IN_FW,PWM_DUTY)
	)
WEST = (
	(right_front_IN_FW, PWM_DUTY),
	(right_back_IN_FW, PWM_DUTY),
	(left_front_IN_BW, PWM_DUTY),
	(left_back_IN_BW,PWM_DUTY)
	)
NORTH_EAST = (
	(right_front_IN_BW, 0),
	(right_back_IN_BW, 0),
	(left_front_IN_FW, PWM_DUTY),
	(left_back_IN_FW,PWM_DUTY)
	)
SOUTH_WEST = (
	(right_front_IN_BW, PWM_DUTY),
	(right_back_IN_BW, PWM_DUTY),
	(left_front_IN_FW, 0),
	(left_back_IN_FW,0)
	)
NORTH_WEST = (
	(right_front_IN_FW, PWM_DUTY),
	(right_back_IN_FW, PWM_DUTY),
	(left_front_IN_BW, 0),
	(left_back_IN_BW,0))
SOUTH_EAST = (
	(right_front_IN_FW, 0),
	(right_back_IN_FW, 0),
	(left_front_IN_BW, PWM_DUTY),
	(left_back_IN_BW,PWM_DUTY)
	)

def enable_motor (enable, dir, duty):
	pca9865.set_PWM(enable,100)
	pca9865.set_PWM(dir,duty)

def disable_motor (enable, dir):
	pca9865.set_PWM(enable,0)
	pca9865.set_PWM(dir,0)

def ir_hacia (motors,direction):
	for m, d in zip(motors, direction):
		print(f'Ir Hacia: {m},{d[0]},{d[1]}')
		enable_motor(m,d[0],d[1])

def stop():
	print(f'Stop')
	pca9865.set_PWM(right_front_EN,0)
	pca9865.set_PWM(right_front_IN_BW,0)
	pca9865.set_PWM(right_front_IN_FW,0)
	pca9865.set_PWM(right_back_EN,0)
	pca9865.set_PWM(right_back_IN_BW,0)
	pca9865.set_PWM(right_back_IN_FW,0)
	pca9865.set_PWM(left_front_EN,0)
	pca9865.set_PWM(left_front_IN_BW,0)
	pca9865.set_PWM(left_front_IN_FW,0)
	pca9865.set_PWM(left_back_EN,0)
	pca9865.set_PWM(left_back_IN_BW,0)
	pca9865.set_PWM(left_back_IN_FW,0)

def test_mover(motors, direction):
	stop()
	time.sleep(1)
	stop()
	time.sleep(1)
	ir_hacia(motors,direction)
	time.sleep(2)
	stop()
	time.sleep(1)


def a_rodar_y_a_rodar():
	#test_mover(MOTORS,NORTH)
	#test_mover(MOTORS,EAST)
	#test_mover(MOTORS,SOUTH)
	#test_mover(MOTORS,WEST)
	test_mover(MOTORS,NORTH_WEST)
	test_mover(MOTORS,SOUTH_WEST)
	test_mover(MOTORS,NORTH_EAST)
	test_mover(MOTORS,SOUTH_EAST)

if __name__ == "__main__":
	a_rodar_y_a_rodar()






