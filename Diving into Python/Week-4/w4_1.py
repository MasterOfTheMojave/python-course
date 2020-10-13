import os.path
import tempfile
import uuid

class File:
    
    def __init__(self, file_name):
        self.file_name = file_name
        self._create_file(self.file_name)
        self.position = 0
    
    def _create_file(self, name):
        f = open(name, 'a+')
        f.close()
    
    def write(self, text):
         with open(self.file_name, 'w') as f:
            return f.write(text)
    
    def read(self):
        with open(self.file_name, 'r') as f:
            return f.read()
    
    def __add__(self, obj):
        temp = tempfile.NamedTemporaryFile()
        temp.close()
        temp_file = os.path.join(os.path.dirname(temp.name), str(uuid.uuid4().hex))
        print(temp_file)
        print(type(temp_file))
        self._create_file(temp_file)
        new_file = type(self)(temp_file)
        new_file.write(self.read() + obj.read())
        return new_file
    
    def __str__(self):
        return os.path.abspath(self.file_name)
    
    def __iter__(self):
        self.fp = open(self.file_name, 'r')
        return self
    
    def __next__(self):
        self.fp.seek(self.position)
        read_l = self.fp.readline()
        self.position += len(read_l)
        if read_l == '':
            self.fp.close()
            self.position = 0
            raise StopIteration
        
        return read_l