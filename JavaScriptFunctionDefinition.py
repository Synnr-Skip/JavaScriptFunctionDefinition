import sublime, sublime_plugin, functools

class JavaScriptFunctionDefinition(sublime_plugin.EventListener):
	#pending = 0
	def on_load(self, view):
		if "JavaScript" not in view.settings().get("syntax"): return
	def on_modified(self, view):
		if "JavaScript" not in view.settings().get("syntax"): return
		#self.pending = self.pending + 1
		#sublime.set_timeout(functools.partial(self.handleTimeout, view), 10000)
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
			results.append(("__{0}\t({1}".format(functionParts[0], functionParts[1]), "{0}({1};".format(functionName,functionParts[1])))
		return (results, sublime.INHIBIT_WORD_COMPLETIONS)
	""" Function summary meta data is coming....
	def handleTimeout(self, view):
		self.pending = self.pending - 1
		if self.pending == 0:
			self.onIdle(view)
	def onIdle(self, view):
		print("No activity in the past 10000ms")
	def refreshList(self, view):
		print("refreshList not implemetned")
	"""
