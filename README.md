# Bing-wallpaper-mac
Automatically set daily Bing wallpaper as Background on Mac 
Using:
1. Download and Extract
2. Edit "autowall.command" and edit path to "wallpaper.py" and Save
3. Edit "automator.plist" and edit path to "autowall.command" and Save
4. Copy "automator.plist" to "~/Library/LaunchAgents"
5. Goto Terminal.app and run the following "launchctl load ~/Library/LaunchAgents/automator.plist"
  
# To uninstall run this command
launchctl unload ~/Library/LaunchAgents/automator.plist

*Updating on further developments*
