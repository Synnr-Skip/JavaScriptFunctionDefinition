import sublime, sublime_plugin, functools

class JavaScriptFunctionDefinition(sublime_plugin.EventListener):
	pumpPrimed = False
	autoCompleteText = ""
	def on_load(self, view):
		if "JavaScript" not in view.settings().get("syntax"): return
	def on_modified(self, view):
		if "JavaScript" not in view.settings().get("syntax"): return
	def on_query_completions(self, view, prefix, locations):
		if "JavaScript" not in view.settings().get("syntax"): return
		matches = view.find_all("function {0}[a-zA-Z\\$0-9_]*\\([a-zA-Z\\$0-9_, \t]*\\)".format(prefix))
		results = []
		originalBehavior = view.extract_completions(prefix)
		for o in originalBehavior:
			results.append((o,o))
		for match in matches:
			functionParts = view.substr(match).split("(")
			functionName = functionParts[0].split("function")[1].strip()
			results.append(("{0}\t({1}".format(functionParts[0], functionParts[1]), "{0}({1};".format(functionName,functionParts[1])))
		self.pumpPrimed = (len(matches) > 0)
		if len(matches) > 0:
			self.autoCompleteText = functionName
		return (results, sublime.INHIBIT_WORD_COMPLETIONS)
	def on_post_text_command(self, view, command_name, args):
		if "JavaScript" not in view.settings().get("syntax"): return
		if((command_name == "insert_best_completion") and self.pumpPrimed):
			DisplayFunctionMetaDataCommand.popUpMenu(self, view, self.autoCompleteText)

class DisplayFunctionMetaDataCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		if (view.sel()[0].empty()): return
		region = view.sel()[0]
		selectedText = view.substr(region)
		self.popUpMenu(self, view, selectedText)
	@staticmethod
	def popUpMenu(self, view, selectedText):
		reg = "///[\s]*{0}[\s]*(\n///[\s\S]*\n)function[\s]+{0}[\s]*\([a-zA-Z\\$0-9_, \s]*\)".format(selectedText)
		matches = view.find_all(reg)
		if len(matches) >= 1:
			functionDefinition = view.substr(matches[0]).split("\n")
			functionDefinition = [w.strip("///") for w in  functionDefinition]
			view.window().show_quick_panel(functionDefinition, None, 1, 2)
	def on_done(self, index):
		return
