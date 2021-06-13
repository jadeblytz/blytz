import messages as msg
import helpers, template

settings = helpers.get_settings()

def execute(ARGS):
	argDict = helpers.arguments(ARGS)

	currTemplate = template.basic()
	if 'props' in argDict:
		currTemplate = template.withProps(argDict['props'].split(','))

	if 'comp' in argDict:
		compName = argDict['comp'] + '.vue'
		dirName = argDict['comp']
		helpers.run_command('mkdir {REPO}/ui/src/components/{DIR}'.format(REPO = settings['repo'], DIR = dirName))
		helpers.run_command('mkdir {REPO}/ui/src/components/{DIR}/{DIR}'.format(REPO = settings['repo'], DIR = dirName))
		helpers.run_command('touch {REPO}/ui/src/components/{DIR}/{DIR}/{FILE}'.format(REPO = settings['repo'], DIR = dirName, FILE = compName))
		helpers.write_file('{ORIGIN}/{REPO}/ui/src/components/{DIR}/{DIR}/{FILE}'.format(ORIGIN = helpers.path('user'), REPO = settings['repo'][2:], DIR = dirName, FILE = compName), currTemplate)
	msg.done()

'''
addTo:
	- components
	- views
	- existing
		- components
		- views
'''