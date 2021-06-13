import messages as msg
import helpers

# settings = helpers.get_settings()

def execute():
	wcSnippets = '{}/snippets/segments-wc.code-snippets'.format(helpers.path('util'))
	classesSnippet = '{}/snippets/segments-classes.code-snippets'.format(helpers.path('util'))
	destinationSnippetPath = '"{}Library/Application Support/Code/User/snippets"'.format(helpers.path('user'))
	print("\nNOTE: Code Snippets are for VSCode\n")
	selection = helpers.user_selection("Select Type: ", ['Web Components', 'Classes'])
	if selection == 1:
		helpers.run_command('scp {FROM} {TO}'.format(FROM = wcSnippets, TO = destinationSnippetPath))
	elif selection == 2:
		helpers.run_command('scp {FROM} {TO}'.format(FROM = classesSnippet, TO = destinationSnippetPath))
	msg.done()