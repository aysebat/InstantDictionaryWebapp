import pandas as pd
class Definition:

    def __init__(self, term):
        self.term = term

    def get(self):
        #read the dictioanry file
        df = pd.read_csv('data.csv')
        definition = tuple(df.loc[df["word"] == self.term]['definition'])
        return definition


if __name__=="__main__":
    d = Definition(term='sun')
    print(d.get())