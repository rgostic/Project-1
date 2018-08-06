import csv
expPlayers = []
nonPlayers = []
dragons = []
sharks = []
raptors = []
with open('soccer_players.csv', newline='') as csvfile:
	rdr = csv.reader(csvfile, delimiter=',')
	
	rows = list(rdr)[1:]
	for row in rows:
		if row[2] == "YES":
			expPlayers.append({'name': row[0], 'height': row[1], 'experience': row[2], 'guardians': row[3]})
		else:
			nonPlayers.append({'name': row[0], 'height': row[1], 'experience': row[2], 'guardians': row[3]})
	ind = 0
	for p in expPlayers:
		if ind % 3 == 0:
			dragons.append(p)
		elif ind % 3 == 1:
			sharks.append(p)
		elif ind % 3 == 2:
			raptors.append(p)
		ind += 1
	
	ind = 0
	for p in nonPlayers:
		if ind % 3 == 0:
			dragons.append(p)
		elif ind % 3 == 1:
			sharks.append(p)
		elif ind % 3 == 2:
			raptors.append(p)
		ind += 1



	

with open('teams.txt', "w") as teamsfile:
	
	teamsfile.write("Sharks\n")
	for p in sharks:
		print(p)
		val = ""
		val += p['name']
		val += ", "
		val += p['experience']
		val += ", "
		val += p['guardians']
		val += '\n'
		teamsfile.write(val)

	teamsfile.write("Dragons\n")
	for p in dragons:
		print(p)
		val = ""
		val += p['name']
		val += ", "
		val += p['experience']
		val += ", "
		val += p['guardians']
		val += '\n'
		teamsfile.write(val)

	teamsfile.write("Raptors\n")
	for p in raptors:
		print(p)
		val = ""
		val += p['name']
		val += ", "
		val += p['experience']
		val += ", "
		val += p['guardians']
		val += '\n'
		teamsfile.write(val)