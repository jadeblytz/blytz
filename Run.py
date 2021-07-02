import messages as msg
import helpers, template

settings = helpers.get_settings()

def execute(ARGS):
	argDict = helpers.arguments(ARGS)

	currTemplate = template.basic()
	if 'props' in argDict:
		currTemplate = template.withProps(argDict['props'].split(','))

	if 'comp' in argDict:
		addToDir = helpers.kv_set(argDict, 'addTo')
		dirName = ''
		if addToDir:
			compName = argDict['comp'] + '.vue'
			parentDir = addToDir
			dirName = argDict['comp']
			helpers.run_command('mkdir {REPO}/ui/src/components/{ADD_TO_DIR}/{DIR}'.format(REPO = settings['repo'], ADD_TO_DIR = addToDir, DIR = dirName))
			helpers.run_command('touch {REPO}/ui/src/components/{ADD_TO_DIR}/{DIR}/{FILE}'.format(REPO = settings['repo'], ADD_TO_DIR = addToDir, DIR = dirName, FILE = compName))
			helpers.write_file('{ORIGIN}/{REPO}/ui/src/components/{ADD_TO_DIR}/{DIR}/{FILE}'.format(ORIGIN = helpers.path('user'), REPO = settings['repo'][2:], ADD_TO_DIR = addToDir, DIR = dirName, FILE = compName), currTemplate)
		else:
			compName = argDict['comp'] + '.vue'
			dirName = argDict['comp']
			helpers.run_command('mkdir {REPO}/ui/src/components/{DIR}'.format(REPO = settings['repo'], DIR = dirName))
			helpers.run_command('mkdir {REPO}/ui/src/components/{DIR}/{DIR}'.format(REPO = settings['repo'], DIR = dirName))
			helpers.run_command('touch {REPO}/ui/src/components/{DIR}/{DIR}/{FILE}'.format(REPO = settings['repo'], DIR = dirName, FILE = compName))
			helpers.write_file('{ORIGIN}/{REPO}/ui/src/components/{DIR}/{DIR}/{FILE}'.format(ORIGIN = helpers.path('user'), REPO = settings['repo'][2:], DIR = dirName, FILE = compName), currTemplate)

		msg.results('ui/src/components/{}/{}'.format(dirName, compName), compName, '@/components/{}/{}'.format(dirName, compName))

	if 'page' in argDict:
		addToDir = helpers.kv_set(argDict, 'addTo')
		if addToDir:
			pageName = argDict['page'] + '.vue'
			parentDir = addToDir
			dirName = argDict['page']
			helpers.run_command('mkdir {REPO}/ui/src/views/{ADD_TO_DIR}'.format(REPO = settings['repo'], ADD_TO_DIR = addToDir))
			helpers.run_command('mkdir {REPO}/ui/src/views/{ADD_TO_DIR}/{DIR}'.format(REPO = settings['repo'], ADD_TO_DIR = addToDir, DIR = dirName))
			helpers.run_command('touch {REPO}/ui/src/views/{ADD_TO_DIR}/{DIR}/{FILE}'.format(REPO = settings['repo'], ADD_TO_DIR = addToDir, DIR = dirName, FILE = pageName))
			helpers.write_file('{ORIGIN}/{REPO}/ui/src/views/{ADD_TO_DIR}/{DIR}/{FILE}'.format(ORIGIN = helpers.path('user'), REPO = settings['repo'][2:], ADD_TO_DIR = addToDir, DIR = dirName, FILE = pageName), currTemplate)
		else:
			pageName = argDict['page'] + '.vue'
			dirName = argDict['page']
			helpers.run_command('mkdir {REPO}/ui/src/views/{DIR}'.format(REPO = settings['repo'], DIR = dirName))
			helpers.run_command('mkdir {REPO}/ui/src/views/{DIR}/{DIR}'.format(REPO = settings['repo'], DIR = dirName))
			helpers.run_command('touch {REPO}/ui/src/views/{DIR}/{DIR}/{FILE}'.format(REPO = settings['repo'], DIR = dirName, FILE = pageName))
			helpers.write_file('{ORIGIN}/{REPO}/ui/src/views/{DIR}/{DIR}/{FILE}'.format(ORIGIN = helpers.path('user'), REPO = settings['repo'][2:], DIR = dirName, FILE = pageName), currTemplate)
		# if routerNotExists:
		# 	helpers.run_command('mkdir {REPO}/ui/src/router/{DIR}'.format(REPO = settings['repo'], DIR = dirName.toLowerCase()))
		# 	helpers.run_command('touch {REPO}/ui/src/router/{DIR}/{DIR}-routes.js'.format(DIR = dirName.toLowerCase()))
	msg.done()

'''
addTo:
	- components
	- views
	- existing
		- components
		- views
'''