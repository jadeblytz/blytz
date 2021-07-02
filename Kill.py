import messages as msg
import helpers

settings = helpers.get_settings()

def execute():
	if "opening_command" in settings:
		helpers.run_command(settings['opening_command'])
	helpers.run_command('npx kill-port 8000')
	helpers.run_command('npx kill-port 8081')
	helpers.run_command('npx kill-port 8082')
	helpers.run_command('vagrant halt')
	if "closing_command" in settings:
		helpers.run_command(settings['closing_command'])
	msg.done()