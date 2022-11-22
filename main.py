import Modules.alert
from Modules.alert import *

import Modules.jsonHandler
from Modules.jsonHandler import *

alertedplayers = []

def main():
	# loop that runs every 2.5 minutes
	while True:
		onlinePlayers = searchJSON()
		for player in onlinePlayers:
			server = player.split(":")[0]
			name = player.split(":")[1]
			if player not in alertedplayers:
				alert(server, name + " is now online!")
				alertedplayers.append(player)
	time.sleep(150)


if __name__ == '__main__':
	main()