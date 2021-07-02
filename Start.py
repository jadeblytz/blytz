import messages as msg
import helpers
import time

settings = helpers.get_settings()


def execute():
	helpers.run_command('open -a Terminal')
	helpers.run_command('sh {utilRoot}/start.sh "{repo}"'.format(repo=settings['repo'], utilRoot=helpers.path('util')))
	msg.done()