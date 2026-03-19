from abc import ABC, abstractmethod


class Plugin(ABC):

    @abstractmethod
    def execute(self):
        pass


class PrintPlugin(Plugin):
    def __init__(self, message):
        self.message = message

    def execute(self):
        print(self.message)


class SumPlugin(Plugin):
    def __init__(self, list_number):
        self.list_number = list_number

    def execute(self):
         print(sum(self.list_number))


class ReversePlugin(Plugin):
    def __init__(self, text):
        self.text = text

    def execute(self):
        print(self.text[::-1])


class PluginManager:
    def __init__(self):
        self.list_plugin = []

    def register(self, plugin: Plugin):
        self.list_plugin.append(plugin)

    def run_all(self):
        for value in self.list_plugin:
            value.execute()


mgr = PluginManager()
mgr.register(PrintPlugin("Привет"))
mgr.register(SumPlugin([1, 2, 3]))
mgr.register(ReversePlugin("Python"))
mgr.run_all()
