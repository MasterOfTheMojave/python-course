class FileReader:
    
    def __init__(self, name):
        self.name = name    
    
    def read(self):
        try:
            f = open(self.name, 'r')
            f_string = f.read()
            f.close()
            return f_string
        except FileNotFoundError:
            return ""