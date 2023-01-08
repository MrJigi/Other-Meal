import pandas as pd
import json
import csv



class recipeService():

    dfFilePath = r"../set/recipeDF.csv"
    tempDataSet = pd.read_csv(dfFilePath)
    # def getAllData():
    #     headFile = tempDF.head(10)
    #     convertToJson = headFile.to_json(orient="table")
    #     convertToJson = json.loads(convertToJson)
    #     json.dumps(convertToJson, indent=4)
    #     return convertToJson

    def getOneItem(self,id):
        # dfFilePath = r"../set/recipeDF.csv"
        # tempDB = pd.read_csv(dfFilePath)
        tempDB = self.tempDataSet
        findItem = tempDB.where(tempDB['id'] == id).dropna()
        convertedToJson = findItem.to_json(orient="split")
        convertedToJson = json.loads(convertedToJson)
        json.dumps(convertedToJson,indent=4)
        return convertedToJson

    def getMostAccurate(self):
        tempDB = self.tempDataSet
        findItem = tempDB.where(tempDB['average_rating'] >= 4.5).dropna().head(10)
        convertedToJson = findItem.to_json(orient="split")
        convertedToJson = json.loads(convertedToJson)
        json.dumps(convertedToJson, indent=4)
        return

    def getByPrefferance(self):
        tempDB = self.tempDataSet
        findItem = tempDB.where(tempDB['votes'] == 1).dropna().head(10)
        convertedToJson = findItem.to_json(orient="split")
        convertedToJson = json.loads(convertedToJson)
        json.dumps(convertedToJson, indent=4)
        return convertedToJson

    def getDataOnDate(self):
        # pass temp arr
        tempDF = self.tempDataSet
        start_date_month = '2021-10-01'
        end_date_month = '2021-11-01'
        dfMon = tempDF[(tempDF['date'] > start_date_month) & (tempDF['date'] <= end_date_month)]
        # dfMon = dfMon[(dfMon['PC4'] == zipCode)]
        convertToJson = dfMon.to_json(orient="table")
        convertToJson = json.loads(convertToJson)
        json.dumps(convertToJson, indent=4)
        return dfMon

    def makeLikedCollumn(self):
        recipesLikesDislikes = self.tempDataSet

        # let's define some polarising ingredients
        liked_ingredients = ["cheese", "pizza", "avocado", "olive oil"]
        hated_ingredients = ["spinach", "mushroom", "olive", "beef", "truffle", "blue cheese"]

        # let's add a "like" property
        recipesLikesDislikes["like"] = 0

        # and populate our data
        recipesLikesDislikes.loc[
            recipesLikesDislikes.ingredients.str.lower().str.contains("|".join(hated_ingredients)), "like"] = -1
        recipesLikesDislikes.loc[
            recipesLikesDislikes.ingredients.str.lower().str.contains("|".join(liked_ingredients)), "like"] = +1
    def csv_to_json(self):
        csvcsvFilePath = r"../../set/recipeDF.csv"
        jsoncsvFilePath = r"../../set/recipeDFJson.json"
        jsonArray = []
        # read csv file
        with open(csvcsvFilePath, encoding='utf-8') as csvf:
            # load csv file data using csv library's dictionary reader
            csvReader = csv.DictReader(csvf)
            # convert each csv row into python dict
            for row in csvReader:
                # add this python dict to json array
                jsonArray.append(row)

        # convert python jsonArray to JSON String and write to file
        with open(jsoncsvFilePath, 'w', encoding='utf-8') as jsonf:
            jsonString = json.dumps(jsonArray, indent=4)
            jsonf.write(jsonString)

    def __init__(self, *args, **kwargs):
        super(recipeService, self).__init__(*args, **kwargs)

# this allows to create the json from the csv
# recipeService.csv_to_json(recipeService)
