import os

class TextIterator():
    def __init__(self, filename:str = None)->None:
        self.filename = str(filename)
        self.Lines = []
        self._loaddata()
        self.linepointer = 0

    def _loaddata(self)->None:
        try:
            with open(self.filename, 'r') as txt:
                for line in txt:
                    self.Lines.append(line)
        except FileNotFoundError:
            print(os.getcwd())
            
    
    class textiteriter:
        def __init__(self, data:list)->None:
            self.linenum = 0
            self.data = data
            
        def __next__(self)->str:
            if self.linenum == len(self.data):
                raise StopIteration
            out = self.data[self.linenum]
            self.linenum += 1
            return out

    def __iter__(self):
        return self.textiteriter(self, self.Lines)

    def getline(self)-> str:
        out = self.Lines[self.linepointer]
        return out

    def getnext(self)-> str:
        self.linepointer += 1
        self.linepointer = self.linepointer % len(self.Lines)
        return self.getline()
    
    def getprevious(self)->str:
        if self.linepointer == 0:
            self.linepointer = len(self.Lines)-1
            return self.getline()
        else:
            self.linepointer -=1
            return self.getline()

    def getfirst(self)->str:
        return self.Lines[0]
    
    def getlast(self)->str:
        return self.Lines[len(self.Lines)-1]
        
    
class TIDemo():
    def __init__(self):
        self.TextIter = TextIterator(self.getFilename())
        self.menu()

    def getFilename(self)->str:
        return input("What is the filename, include extention:\n")

    def beemov(self):
        self.TextIter.filename = "bee movie script.txt"
        self.TextIter.Lines = []
        self.TextIter._loaddata()

    def menu(self):
        run = True
        commands = "First : to get first line\nPrev : to get previous line\nNext : to get the next line\nLast to get the last line\nQuit : to stop running\nHelp : to see this list"
        while(run):
            intext = input("Enter a command:")
            
            match intext:
                case "First":
                    print(self.TextIter.getfirst())
                case "Last":
                    print(self.TextIter.getlast())
                case "Next":
                    print(self.TextIter.getnext())
                case "Prev":
                    print(self.TextIter.getprevious())
                case "Quit":
                    run = False
                case "Help":
                    print(commands)
                case "Bee":
                    self.beemov()
                case _:
                    print(commands)
        



if __name__ == "__main__":
    Demo = TIDemo()
