import urllib.request

domain_list = [
	'bgea.org.nz', # 200
	'livingtheword.org.nz', # 200
	
	'bowelscreening.org.nz', # HTTP Error 403
	'celiquehairproducts.org.nz', # urlopen error [Errno 8]
	'blakelibrary.org.nz' # HTTP Error 404
	]

broken_domain = list()

for domain in domain_list:
	try:
		response_code = urllib.request.urlopen('http://' + domain).getcode()
		print(domain, response_code)
	except Exception as e:
		broken_domain.append(domain + ' ' + str(e))

print()

for d in broken_domain:
	print(d)
