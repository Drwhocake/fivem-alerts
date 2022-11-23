import config as cfg
#goal is to search through the json to match identifiers to those in the config file and then return the name of the player / players
import urllib.request, json

def searchJSON():
	onlinePlayers = []
	#for each server in the config file
	for server in cfg.json:
		#open json file from url
		with urllib.request.urlopen(cfg.json[server]) as url:
			data = json.loads(url.read().decode())
			#loop through the json file as players
			for player in data:
				#loop through the identifiers of each player
				for identifier in player['identifiers']:
					#loop through the identifiers in the config file
					for key in cfg.people:
						#if the identifier matches one in the config file
						if identifier == key:
							#store the name of the player under the server name multiple players can be stored under the same server name
							onlinePlayers.append({server:cfg.people[key]})
							break


	return onlinePlayers