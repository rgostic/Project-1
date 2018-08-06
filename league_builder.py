import csv
# lists to load with data
expPlayers = []
nonPlayers = []
dragons = []
sharks = []
raptors = []

if __name__ == "__main__":

	with open('soccer_players.csv', newline='') as csvfile:
		rdr = csv.reader(csvfile, delimiter=',')
		
		rows = list(rdr)[1:]
		for row in rows:
			#if player is experienced
			if row[2] == "YES":
				expPlayers.append({'name': row[0], 'height': row[1], 'experience': row[2], 'guardians': row[3]})
			#if played is not experienced
			else:
				nonPlayers.append({'name': row[0], 'height': row[1], 'experience': row[2], 'guardians': row[3]})
		ind = 0
		# distribute experienced players evenly
		for p in expPlayers:
			if ind % 3 == 0:
				dragons.append(p)
			elif ind % 3 == 1:
				sharks.append(p)
			elif ind % 3 == 2:
				raptors.append(p)
			ind += 1
		
		ind = 0
		# distribute unexperienced players evenly
		for p in nonPlayers:
			if ind % 3 == 0:
				dragons.append(p)
			elif ind % 3 == 1:
				sharks.append(p)
			elif ind % 3 == 2:
				raptors.append(p)
			ind += 1

	with open('teams.txt', "w") as teamsfile:
		#write sharks to file
		teamsfile.write("Sharks\n")
		for p in sharks:		
			val = ""
			val += p['name']
			val += ", "
			val += p['experience']
			val += ", "
			val += p['guardians']
			val += '\n'
			teamsfile.write(val)
		#write dragons to file
		teamsfile.write("Dragons\n")
		for p in dragons:		
			val = ""
			val += p['name']
			val += ", "
			val += p['experience']
			val += ", "
			val += p['guardians']
			val += '\n'
			teamsfile.write(val)
		#write raptors to file
		teamsfile.write("Raptors\n")
		for p in raptors:		
			val = ""
			val += p['name']
			val += ", "
			val += p['experience']
			val += ", "
			val += p['guardians']
			val += '\n'
			teamsfile.write(val)