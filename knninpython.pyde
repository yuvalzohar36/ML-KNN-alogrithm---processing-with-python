import json
from pprint import pprint


def setup():
    titles = []
    size(600,600)
    background(255)
    fill(0)
    textSize(33);
    with open('movies.json') as f:
        data = json.load(f)
        users = {}                   # Declare users var
    person1 = "Alca"
    person2 = "hablwgq"
    
    for i in range(len(data['users'])):
        name = data['users'][i]['name']
        users[name] = data['users'][i]     # organize the data {name , [ratings]
   
    
    
    for key, value in users[person1].items():
        if (key != "name" and key != "timestamp"):   # Sorting "timestamp && name" 
            titles.append(key)
    #for key, value in users[person2].items():
    #    if (key != "name" and key != "timestamp"):   # Sorting "timestamp && name" 
    #        titles.append(key)
    sumSquares = 0 
    for j in range(len(titles)):
        title = titles[j];
        rating1 = users[person1][title]
        rating2 = users[person2][title]
        if (rating1 != None and rating2 != None):
                    diff = rating1 - rating2
                    sumSquares += diff * diff
        #print(titles[j] + str(rating1) + "\n ")
        #print(titles[j] + str(rating2))

    d = sqrt(sumSquares)
    print(d)
    text("First name :" + person1,0,100)
    text("Second name :" + person2,0,150)
    text("Similarity :" + str(d) ,0,200)
    
