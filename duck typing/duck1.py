class pycharm:
    def compile(self):
        print("compile using pycharm")
    def execute(self):
        print("execute")
class vscode:
    def compile(self):
        print("compile using vscode")
    def execute(self):
        print("execute")
class programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()
p=programmer()
pyc=pycharm()
p.coding(pyc)