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
        self.transition_output=[]
        self.transition_output_count=[]
        for length in range(0,len(self.map_list)):
            current_pair=self.map_list[length]
            current_word=current_pair.keys()
            current_word_list=list(current_word)
            current_count=0
            for i in self.map_list:
                key=i.keys()
                if current_word==key:
                    current_count+=1
            if current_word_list[0] not in self.transition_output:
                self.transition_output.append(current_word_list[0])
                self.transition_output_count.append(current_count)

        for i in range(0,len(self.transition_output_count)):
            self.reduce_output.append({self.transition_output[i]:self.transition_output_count[i]})


text=input("Enter the long text that you want to check: ")
mapper_object=mapper(text)
mapper_object.map()
map_output=mapper_object.map_output

reducer_object=reducer(map_output)
reducer_object.reduce()
print(reducer_object.reduce_output)
