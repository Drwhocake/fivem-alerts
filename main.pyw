import Modules.alert
from Modules.alert import *

import Modules.jsonHandler
from Modules.jsonHandler import *
import time

alertedplayers = []

def main():

	alert("Fivem Player Alert", "Script is now running")
	# loop that runs every 2.5 minutes
	while True:
		onlinePlayers = searchJSON()
		for player in onlinePlayers:
			for server in player:
				name = player[server]
				#check the name of the player against the list of players that have already been alerted per server
				if name not in alertedplayers:
					alert(server, name + " is now online!")
					alertedplayers.append(name)
		time.sleep(150)



if __name__ == '__main__':
	# run script in the background


	main()