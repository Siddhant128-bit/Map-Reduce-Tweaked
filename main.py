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
class reducer(object):
    def __init__(self,map_list):
        super(reducer,self).__init__()
        self.map_list=map_list

    def reduce(self):
        self.reduce_output=[]
        for length in range(0,len(self.map_list)):
            current_pair=self.map_list[length]
            current_word=current_pair.keys()
            current_count=0
            for i in self.map_list:
                key=i.keys()
                if current_word==key:
                    current_count+=1
            self.reduce_output[current_word[0]]=current_count

text=input("Enter the long text that you want to check: ")
mapper_object=mapper(text)
mapper_object.map()
map_output=mapper_object.map_output
print(map_output)
