def index():
	with open('templates/index.html', 'rb') as f:
			data = f.read()
	return data
	# conn.send(data)
	# conn.close()