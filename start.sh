#!/bin/sh

# Taken and modified from https://apple.stackexchange.com/a/58151
osascript <<EOF
tell application "Terminal"
    activate
    do script "cd $1 && vagrant up && vagrant ssh" in front window
    delay 10
    activate
    my makeTab()
    do script "cd $1/api && ./manage.py runserver" in front window
    my makeTab()
    do script "cd $1/ui && npm run serve -- --port 8081" in front window
	my makeTab()
	do script "cd $1/consumer-ui && npm run serve -- --port 8082" in front window
end tell

on makeTab()
    tell application "System Events" to keystroke "t" using {command down}
    delay 0.2
end makeTab
EOF