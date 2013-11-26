grep_file
=========

Sublime plugin for ease opening "View" in Rails.

add key binding:
Preferences/Key Bindings - User/

	[
		{ "keys": ["shift+ctrl+g"], "command": "grep_file" }
	]

### Instalations:

	cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages
	git clone git@github.com:ArtyomTs/grep_file.git

### Removing:

	CMD + Shift + P
	Package Control: Remove Package
	choose "grep_file"

### Usage:

1. Jump to any Controller
2. Select file path or put cursor into it
3. Also you can jump by actions
4. Press ctrl+shift+g


		def index
		render :new
		render 'new'
		render 'some/absolute/path'


1. Jump to any View
2. Select file path or put cursor into it
3. Press ctrl+shift+g


		render @brands
		render :orders_table
		render 'orders_table'
		render 'shared/flash_messages'
