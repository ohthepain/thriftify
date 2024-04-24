countries = {}
flagfiles = {}
n = 0
with open("countrydata.tsv", "r") as countrystream:
	with open("flags.txt", "r") as flagstream:
		for line in flagstream:
			countrycode = line.strip().split(".")[0].upper()
			#print(countrycode)
			flagfiles[countrycode] = line
		for line in countrystream:
			country = line.strip().split("\t")
			countrycode = country[0].upper()
			if countrycode in flagfiles:
				iso3 = country[1]
				isonumeric = country[2]
				fips = country[3]
				display = country[4]
				capital = country[5]
				continent = country[8]
				flagfile = 'locations/flag-images/%s' % (countrycode.lower())
				print('%s,%s,%s,%s,%s,,%s,%s,%d,%s' % (countrycode, iso3, isonumeric, fips, display, capital, flagfile, n, continent))
				n = n + 1
