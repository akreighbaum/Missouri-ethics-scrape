from BeautifulSoup import BeautifulSoup

# We're going to grab the HTML from a local file rather than the Internet, just so we don't irritate
# the Ethics Commission with a bunch of requests.
html = open('page.html', 'r').read()
soup = BeautifulSoup(html)
lobbyists = soup.find('table', attrs={'id': 'ctl00_ContentPlaceHolder_grvMain'})

# Again, this is where our output will live
output = []

for tr in lobbyists.findAll('tr')[1:]:

	output_row = []
	#output.append(output_row)

	for td in tr.findAll('td'):

		if td.text != 'View':

			# if td.text = 'Columbia, City Of':
			output_row.append(td.text)

	if output_row[2] == 'Columbia, City Of':
		output_row[0] = output_row[0].replace('&nbsp;', '')
		output.append(output_row)

print output

		# if td = ctl00_ContentPlaceHolder_grvMain_ctl92_lbtnView
		# data = td.text.('ctl00_ContentPlaceHolder_grvMain_ctl01_lbtnDetails')
		# output_row.append(data)	
		# print output_row
		# print time.sleep(0.5)

	# output.append(output_row)
	# print output


# Your scraper should do several things:

# 1. First, grab all the lobbyist expenditures from the table
# 2. Skip, or ignore, the column that says "View"
# 3. If the transaction is for an official in Columbia, add it to the output list
# 4. Remove the &nbsp; string from all output where it appears
# 5. At the end, print the output list

########## YOUR CODE GOES HERE ##########