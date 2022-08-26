from urllib import response
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from requests.auth import HTTPBasicAuth

base_url = "<url>/rest"
auth = HTTPBasicAuth('<username>', '<password>')
headers = {"Content-type": "text/plain"}

def sendCommand(url, auth, data, headers):
    try:
        response = requests.post(url, auth=auth, data=data, headers=headers, timeout=8)
        response.raise_for_status()
        print(response)
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)

###
##
## myopenHAB Cloud Service
##
###

myopenHABCloudService = {}
myopenHABCloudService['LastHour'] = "http://status.openhab.org/check/359410?timefilter=1"
myopenHABCloudService['Last24Hours'] = "http://status.openhab.org/check/359410?timefilter=24"
myopenHABCloudService['Last7Days'] = "http://status.openhab.org/check/359410?timefilter=168"
myopenHABCloudService['Last30Days'] = "http://status.openhab.org/check/359410?timefilter=720"
myopenHABCloudService['Last90Days'] = "http://status.openhab.org/check/359410?timefilter=2160"

for key in myopenHABCloudService:
    print(key)
    page = requests.get(myopenHABCloudService[key])
    contents = page.content
    soup = BeautifulSoup(contents, "html.parser")

    LastUpdated = soup.find("div", "datetime").text
    LastUpdated = LastUpdated.replace("th,", ",")
    LastUpdated = datetime.strptime(LastUpdated, "%B %d, %Y %H:%M %p")
    LastUpdated = LastUpdated.strftime("%Y-%m-%dT%H:%M:%S")
    Availability = soup.find_all("div", "value")[0].text
    Downtime = soup.find_all("div", "value")[1].text

    print(LastUpdated)
    print(Availability)
    print(Downtime)

    url = base_url + "/items/myopenHABCloudServiceLastUpdated" +  key
    sendCommand(url, auth, LastUpdated, headers)

    url = base_url + "/items/myopenHABCloudServiceAvailability" +  key
    sendCommand(url, auth, Availability, headers)

    url = base_url + "/items/myopenHABCloudServiceDowntime" +  key
    sendCommand(url, auth, Downtime, headers)

###
##
## openHAB Community Forum
##
###

openHABCommunityForum = {}
openHABCommunityForum['LastHour'] = "http://status.openhab.org/check/359473?timefilter=1"
openHABCommunityForum['Last24Hours'] = "http://status.openhab.org/check/359473?timefilter=24"
openHABCommunityForum['Last7Days'] = "http://status.openhab.org/check/359473?timefilter=168"
openHABCommunityForum['Last30Days'] = "http://status.openhab.org/check/359473?timefilter=720"
openHABCommunityForum['Last90Days'] = "http://status.openhab.org/check/359473?timefilter=2160"

for key in openHABCommunityForum:
    print(key)
    page = requests.get(openHABCommunityForum[key])
    contents = page.content
    soup = BeautifulSoup(contents, "html.parser")

    LastUpdated = soup.find("div", "datetime").text
    LastUpdated = LastUpdated.replace("th,", ",")
    LastUpdated = datetime.strptime(LastUpdated, "%B %d, %Y %H:%M %p")
    LastUpdated = LastUpdated.strftime("%Y-%m-%dT%H:%M:%S")
    Availability = soup.find_all("div", "value")[0].text
    Downtime = soup.find_all("div", "value")[1].text

    print(LastUpdated)
    print(Availability)
    print(Downtime)

    url = base_url + "/items/openHABCommunityForumLastUpdated" +  key
    sendCommand(url, auth, LastUpdated, headers)

    url = base_url + "/items/openHABCommunityForumAvailability" +  key
    sendCommand(url, auth, Availability, headers)

    url = base_url + "/items/openHABCommunityForumDowntime" +  key
    sendCommand(url, auth, Downtime, headers)

###
##
## openHAB Build Server
##
###

openHABBuildServer = {}
openHABBuildServer['LastHour'] = "http://status.openhab.org/check/359475?timefilter=1"
openHABBuildServer['Last24Hours'] = "http://status.openhab.org/check/359475?timefilter=24"
openHABBuildServer['Last7Days'] = "http://status.openhab.org/check/359475?timefilter=168"
openHABBuildServer['Last30Days'] = "http://status.openhab.org/check/359475?timefilter=720"
openHABBuildServer['Last90Days'] = "http://status.openhab.org/check/359475?timefilter=2160"

for key in openHABBuildServer:
    print(key)
    page = requests.get(openHABBuildServer[key])
    contents = page.content
    soup = BeautifulSoup(contents, "html.parser")

    LastUpdated = soup.find("div", "datetime").text
    LastUpdated = LastUpdated.replace("th,", ",")
    LastUpdated = datetime.strptime(LastUpdated, "%B %d, %Y %H:%M %p")
    LastUpdated = LastUpdated.strftime("%Y-%m-%dT%H:%M:%S")
    Availability = soup.find_all("div", "value")[0].text
    Downtime = soup.find_all("div", "value")[1].text

    print(LastUpdated)
    print(Availability)
    print(Downtime)

    url = base_url + "/items/openHABBuildServerLastUpdated" +  key
    sendCommand(url, auth, LastUpdated, headers)

    url = base_url + "/items/openHABBuildServerAvailability" +  key
    sendCommand(url, auth, Availability, headers)

    url = base_url + "/items/openHABBuildServerDowntime" +  key
    sendCommand(url, auth, Downtime, headers)

###
##
## openHAB Demo Server
##
###

openHABDemoServer = {}
openHABDemoServer['LastHour'] = "http://status.openhab.org/check/359476?timefilter=1"
openHABDemoServer['Last24Hours'] = "http://status.openhab.org/check/359476?timefilter=24"
openHABDemoServer['Last7Days'] = "http://status.openhab.org/check/359476?timefilter=168"
openHABDemoServer['Last30Days'] = "http://status.openhab.org/check/359476?timefilter=720"
openHABDemoServer['Last90Days'] = "http://status.openhab.org/check/359476?timefilter=2160"

for key in openHABDemoServer:
    print(key)
    page = requests.get(openHABDemoServer[key])
    contents = page.content
    soup = BeautifulSoup(contents, "html.parser")

    LastUpdated = soup.find("div", "datetime").text
    LastUpdated = LastUpdated.replace("th,", ",")
    LastUpdated = datetime.strptime(LastUpdated, "%B %d, %Y %H:%M %p")
    LastUpdated = LastUpdated.strftime("%Y-%m-%dT%H:%M:%S")
    Availability = soup.find_all("div", "value")[0].text
    Downtime = soup.find_all("div", "value")[1].text

    print(LastUpdated)
    print(Availability)
    print(Downtime)

    url = base_url + "/items/openHABDemoServerLastUpdated" +  key
    sendCommand(url, auth, LastUpdated, headers)

    url = base_url + "/items/openHABDemoServerAvailability" +  key
    sendCommand(url, auth, Availability, headers)

    url = base_url + "/items/openHABDemoServerDowntime" +  key
    sendCommand(url, auth, Downtime, headers)

###
##
## openHAB Online Repository
##
###

openHABOnlineRepository = {}
openHABOnlineRepository['LastHour'] = "http://status.openhab.org/check/845970?timefilter=1"
openHABOnlineRepository['Last24Hours'] = "http://status.openhab.org/check/845970?timefilter=24"
openHABOnlineRepository['Last7Days'] = "http://status.openhab.org/check/845970?timefilter=168"
openHABOnlineRepository['Last30Days'] = "http://status.openhab.org/check/845970?timefilter=720"
openHABOnlineRepository['Last90Days'] = "http://status.openhab.org/check/845970?timefilter=2160"

for key in openHABOnlineRepository:
    print(key)
    page = requests.get(openHABOnlineRepository[key])
    contents = page.content
    soup = BeautifulSoup(contents, "html.parser")

    LastUpdated = soup.find("div", "datetime").text
    LastUpdated = LastUpdated.replace("th,", ",")
    LastUpdated = datetime.strptime(LastUpdated, "%B %d, %Y %H:%M %p")
    LastUpdated = LastUpdated.strftime("%Y-%m-%dT%H:%M:%S")
    Availability = soup.find_all("div", "value")[0].text
    Downtime = soup.find_all("div", "value")[1].text

    print(LastUpdated)
    print(Availability)
    print(Downtime)

    url = base_url + "/items/openHABOnlineRepositoryLastUpdated" +  key
    sendCommand(url, auth, LastUpdated, headers)

    url = base_url + "/items/openHABOnlineRepositoryAvailability" +  key
    sendCommand(url, auth, Availability, headers)

    url = base_url + "/items/openHABOnlineRepositoryDowntime" +  key
    sendCommand(url, auth, Downtime, headers)
