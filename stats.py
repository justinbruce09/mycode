import requests

hockey= requests.get("https://statsapi.web.nhl.com/api/v1/teams").json()

print(hockey["teams"])

#hockey["teams"] is a list
for i in hockey["teams"]:
    print(hockey["teams"])

    print("")

    print(i['teamName'])

    print(i['venue']['timezone']['tz'])

    print(i['division']['name'])

    
    

