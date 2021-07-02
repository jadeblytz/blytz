import helpers, json

actionList = json.loads(helpers.read_file('{}/{}'.format(helpers.path('util'), 'action-list.json')))

def statusMessage():
	if len(actionList['actions']) > 0:
		print("")
		for item in actionList['actions']:
			print('''[ {} {} ]\t\t{}'''.format(actionList['alias'], item['name'], item['description']))
		print("")
	else:
		print('''
blytz is working successfully!
''')

def done():
	print('''
[ Process Completed ]
''')

def example():
	print('''
process working!
''')

def results(LOCATION, FILE, IMPORT_PATH):
	print('''
Component Created!

===============================
PATH:    ui/src/{location}
FILE:    {file}
IMPORT:  import {fileRef} from '{importPath}'
===============================
'''.format(location = LOCATION, file = FILE, importPath = IMPORT_PATH, fileRef = FILE[:-4]))