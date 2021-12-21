import sys
class mapper(object):
    def __init__(self,text):
        super(mapper,self).__init__()
        self.text=text

    def map(self):
        self.words=self.text.split() #Converting the text into list so that it can be traversed upon
        self.map_output=[]
        for word in self.words:
            self.map_output.append({word:1})


mapper('Apple Ball and Cat')
