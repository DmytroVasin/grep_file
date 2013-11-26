import sublime, sublime_plugin
import os, re

def is_folder(path, action):
    regex = re.compile(action)
    return regex.findall(path)

def generate_prefix(path, folder_name):
    if folder_name == 'controller':
        return path.rstrip('_controller.rb').split('/controllers/')[1] + '/'
    elif folder_name == 'view':
        current_path = os.path.dirname(path)
        return current_path.split('/app/views/')[1] + '/'
    else:
        return ''

def generate_file_name(path, action_name, folder_name):
    if re.search(r"def\s", action_name):
        # if matched action of controller
        path = generate_prefix(path, folder_name)
        action_name = action_name.replace("def ", "")
    elif re.match(r'[@:]', action_name):
        # render :edit || @products
        action_name = action_name[1:-1]
        path = generate_prefix(path, folder_name)
    elif len(action_name.split('/')) > 1:
        # render template: 'account/account_admin/surveys/show' ( absolute path )
        action_name = action_name.replace("'", "").replace('"', '')
        path = ''
    else:
        # render 'new' ( relative path )
        path = generate_prefix(path, folder_name)
        action_name = action_name.replace("'", "").replace('"', '')

    path += action_name
    return path

def get_action_name(self):
    sel = self.view.sel()[0]
    return ( str(self.view.substr(sel)), sel )

class GrepFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        path = str(self.view.file_name())
        action_name, sel = get_action_name(self)
        if sel.empty():
            self.view.window().run_command("expand_selection", {"to": "scope"} )
            action_name, sel = get_action_name(self)

        if is_folder(path, '(controllers)'):
            path = generate_file_name(path, action_name, 'controller')
        if is_folder(path, '(app/view)'):
            path = generate_file_name(path, action_name, 'view')

        # self.view.sel().clear()
        self.view.window().run_command("show_overlay", {"overlay": "goto", "show_files": True, "text": "app/view/"+path} )
