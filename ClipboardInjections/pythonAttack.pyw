from hack import malware
import time

#Runs until a successful attack has been made
def main():
	done = 0
	while(done != 1):
		done = malware.mal("52","You got hacked haha")
		print("Run")
		time.sleep(4)
main()
