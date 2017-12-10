from Speech import Speech
import pandas as pd

class Brain(object):

    genre = ['genre']

    def talk(text):
        Speech.speechAnalysis(text)
        return text

    def suggest(text):
        Speech.speechAnalysis(text)
        return 'dsafasdf'

    def greeting(text):
        Speech.speechAnalysis(text)

    def searchData(data):
        df = pd.read_csv('./data/anime.csv')
        search = []

        index = 2 #name

        newData = data

        for temp in Brain.genre:
            if(temp in data):
                newData = newData.replace(temp + " ", "")
                index = 3 #genre
                print(newData)



        for row in df.itertuples():
            if newData in str(row[index]):
                print(row)
                search.append(str(row[2])   )
        return search

    def sortRating(data):
        df = pd.read_csv('anime.csv')
        # sort by rating
        df.sort_values(df.columns[5])


