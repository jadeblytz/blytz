import messages as msg
import helpers

settings = helpers.get_settings()

def execute():
	helpers.run_command('touch {}/vagrant/custom_commands.sh'.format(settings['repo']))
	helpers.run_command('cd {}/vagrant && chmod -x custom_commands.sh'.format(settings['repo']))
	msg.done()
