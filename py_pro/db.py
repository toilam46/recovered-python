class Database:
    """"""
    def __init__(self):
        self.data = {}   
    
    def insert(self, key, value):
        self.data[key] = value
    
    def retrieve(self, key):
        return self.data.get(key, None) 
    
    def delete(self, key):
        if key in self.data:
            del self.data[key]  

    def update(self, key, value):
        if key in self.data:
            self.data[key] = value
        
    
    