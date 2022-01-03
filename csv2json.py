import csv
import json
from operator import itemgetter
import operator 
from collections import defaultdict
import requests

csv_file = "works.csv"
json_file = "works.json"


data = []


def getWdLabel(WD):
    try:
        resp = requests.get(f"https://www.wikidata.org/wiki/Special:EntityData/{WD}.json").json()
        labels = resp.get('entities').get(WD).get('labels')
        try:
            return labels.get('en')
        except:
            return labels.get(list(labels.keys())[0])
    except:
        return None


def parserow(row:list):
    tmpDict = {
        'author' : {
            'name' : row[0].replace('@','').rstrip()
        },
        'title' : row[6].rstrip(),
        'content' : {}
    }
    
    ## Add authority files for author
    for n,cell in enumerate(row[1:6],1):
        if not cell == "":
            try:
                tmpDict['author']['ID'].append(
                    {
                        fieldnames[n] : cell
                        }
                        )
            except KeyError:
                tmpDict['author']['ID'] = [
                    {
                        fieldnames[n] : cell
                        }
                ]
    ## Content

    if not row[7] == "":
        tmpDict['content']['num_books'] = row[7]
    
    if not row[8] == "":
        tmpDict['content']['num_verses'] = row[8]
    
    if not row[9] == "":
        tmpDict['content']['metre'] = row[9]
    
    if not row[10] == "":
        tmpDict['content']['subject'] = [{ "url" : subject, "label" : getWdLabel(subject)} for subject in row[10].split(',')]
    
    if not row[11] == "":
        tmpDict['content']['ordo'] = row[11]
    
    if not row[12] == "":
        tmpDict['Goetterapparat'] = row[12]
   
    ## Dates
    def parsedate(row:list,index:int):
        if not row[index] == "":
            if not "dates" in tmpDict.keys():
                tmpDict["dates"] = []
            tmpDict['dates'].append(
                    {
                        'value' : row[index],
                        'qualification ': row[index+1]
                    }
                )

    for index in [13,15]:
        parsedate(row,index)

    for n,manifestation in enumerate(row[21:26],21):
        if not manifestation == "":
            if not "manifestations" in tmpDict.keys():
                tmpDict["manifestations"] = []
            tmpDict['manifestations'].append(
                {
                    'description' : fieldnames[n],
                    'ID' : manifestation
                }
            )
    
    if not row[35] == "":
        if not "manifestations" in tmpDict.keys():
                tmpDict["manifestations"] = []
        for modEd in row[35].split(','):
            tmpDict['manifestations'].append(
                    {
                        'description' : "modern edition",
                        'ID' : modEd
                    }
                )
    
    if not row[36] == "":
        if not "manifestations" in tmpDict.keys():
                tmpDict["manifestations"] = []
        tmpDict['manifestations'].append(
                {
                    'description' : "machine readable edition",
                    'ID' : row[36]
                }
            )

    for url in itemgetter(25,26)(row):
        if not url == "":
            if not "urls" in tmpDict.keys():
                tmpDict["urls"] = []
            tmpDict['urls'].append(url)

    for url in itemgetter(27,29,31,33,36)(row):
        if not url == "":
            if not "urls" in tmpDict.keys():
                tmpDict["urls"] = []
            tmpDict['urls'].append(f"https://books.google.de/books?id={url}")
    
    for bibref in itemgetter(20,37)(row):
        if not bibref == "":
            if not "bibrefs" in tmpDict.keys():
                tmpDict["bibrefs"] = []
            tmpDict['bibrefs'].extend(bibref.split(','))
    


    return tmpDict



    
        

   

with open(csv_file, 'r') as IN:
    csvReader = csv.reader(IN)
    fieldnames = next(csvReader)
    for row in csvReader:
        data.append(parserow(row))
        

with open(json_file, 'w') as OUT:
    OUT.write(json.dumps(data, indent = 4))


for n,x in enumerate(fieldnames):
    print(f"{n}\t{x}")