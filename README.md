# status-openhab-org
openHAB's live status from [status.openhab.org](http://status.openhab.org/) as items inside your openHAB instance.

## Installation

### Python

At first you have to install some dependencies for `Python 3.x` with `pip`:

```
pip install requests
pip install beautifulsoup4
```

Then you can get the python file and make it executable:

```
cd /path/to/place
wget https://raw.githubusercontent.com/Michdo93/status-openhab-org/main/status_openhab.py
sudo chmod +x status_openhab.py
```

### openHAB

#### Items

You have to create empty items which get populated via the python script:

```
Group statusOpenhabOrg

DateTime myopenHABCloudServiceLastUpdatedLastHour "myopenHAB Cloud Service Last Updated Last Hour [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String myopenHABCloudServiceAvailabilityLastHour "myopenHAB Cloud Service Availability Last Hour [%s]" (statusOpenhabOrg)
String myopenHABCloudServiceDowntimeLastHour "myopenHAB Cloud Service Downtime LastHour [%s]" (statusOpenhabOrg)
DateTime myopenHABCloudServiceLastUpdatedLast24Hours "myopenHAB Cloud Service Last Updated Last 24 Hours [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String myopenHABCloudServiceAvailabilityLast24Hours "myopenHAB Cloud Service Availability Last 24 Hours [%s]" (statusOpenhabOrg)
String myopenHABCloudServiceDowntimeLast24Hours "myopenHAB Cloud Service Downtime Last 24 Hours [%s]" (statusOpenhabOrg)
DateTime myopenHABCloudServiceLastUpdatedLast7Days "myopenHAB Cloud Service Last Updated Last 7 Days [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String myopenHABCloudServiceAvailabilityLast7Days "myopenHAB Cloud Service Availability Last 7 Days [%s]" (statusOpenhabOrg)
String myopenHABCloudServiceDowntimeLast7Days "myopenHAB Cloud Service Downtime Last 7 Days [%s]" (statusOpenhabOrg)
DateTime myopenHABCloudServiceLastUpdatedLast30Days "myopenHAB Cloud Service Last Updated Last 30 Days [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String myopenHABCloudServiceAvailabilityLast30Days "myopenHAB Cloud Service Availability Last 30 Days [%s]" (statusOpenhabOrg)
String myopenHABCloudServiceDowntimeLast30Days "myopenHAB Cloud Service Downtime Last 30 Days [%s]" (statusOpenhabOrg)
DateTime myopenHABCloudServiceLastUpdatedLast90Days "myopenHAB Cloud Service Last Updated Last 90 Days [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String myopenHABCloudServiceAvailabilityLast90Days "myopenHAB Cloud Service Availability Last 90Days [%s]" (statusOpenhabOrg)
String myopenHABCloudServiceDowntimeLast90Days "myopenHAB Cloud Service DowntimeLast90Days [%s]" (statusOpenhabOrg)

DateTime openHABCommunityForumLastUpdatedLastHour "openHAB Community Forum Last Updated Last Hour [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String openHABCommunityForumAvailabilityLastHour "openHAB Community Forum Availability Last Hour [%s]" (statusOpenhabOrg)
String openHABCommunityForumDowntimeLastHour "openHAB Community Forum Downtime Last Hour [%s]" (statusOpenhabOrg)
DateTime openHABCommunityForumLastUpdatedLast24Hours "openHAB Community Forum Last Updated Last 24 Hours [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String openHABCommunityForumAvailabilityLast24Hours "openHAB Community Forum Availability Last 24 Hours [%s]" (statusOpenhabOrg)
String openHABCommunityForumDowntimeLast24Hours "openHAB Community Forum Downtime Last 24 Hours [%s]" (statusOpenhabOrg)
DateTime openHABCommunityForumLastUpdatedLast7Days "openHAB Community Forum Last Updated Last 7 Days [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String openHABCommunityForumAvailabilityLast7Days "openHAB Community Forum Availability Last 7 Days [%s]" (statusOpenhabOrg)
String openHABCommunityForumDowntimeLast7Days "openHAB Community Forum Downtime Last 7 Days [%s]" (statusOpenhabOrg)
DateTime openHABCommunityForumLastUpdatedLast30Days "openHAB Community Forum Last Updated Last 30 Days [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String openHABCommunityForumAvailabilityLast30Days "openHAB Community Forum Availability Last 30 Days [%s]" (statusOpenhabOrg)
String openHABCommunityForumDowntimeLast30Days "openHAB Community Forum Downtime Last 30 Days [%s]" (statusOpenhabOrg)
DateTime openHABCommunityForumLastUpdatedLast90Days "openHAB Community Forum Last Updated Last 90 Days [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String openHABCommunityForumAvailabilityLast90Days "openHAB Community Forum Availability Last 90 Days [%s]" (statusOpenhabOrg)
String openHABCommunityForumDowntimeLast90Days "openHAB Community Forum Downtime Last 90 Days [%s]" (statusOpenhabOrg)

DateTime openHABBuildServerLastUpdatedLastHour "openHAB Build Server Last Updated Last Hour [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String openHABBuildServerAvailabilityLastHour "openHAB Build Server Availability Last Hour [%s]" (statusOpenhabOrg)
String openHABBuildServerDowntimeLastHour "openHAB Build Server Downtime Last Hour [%s]" (statusOpenhabOrg)
DateTime openHABBuildServerLastUpdatedLast24Hours "openHAB Build Server Last Updated Last 24 Hours [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String openHABBuildServerAvailabilityLast24Hours "openHAB Build Server Availability Last 24 Hours [%s]" (statusOpenhabOrg)
String openHABBuildServerDowntimeLast24Hours "openHAB Build Server Downtime Last 24 Hours [%s]" (statusOpenhabOrg)
DateTime openHABBuildServerLastUpdatedLast7Days "openHAB Build Server Last Updated Last 7 Days [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String openHABBuildServerAvailabilityLast7Days "openHAB Build Server Availability Last 7 Days [%s]" (statusOpenhabOrg)
String openHABBuildServerDowntimeLast7Days "openHAB Build Server Downtime Last 7 Days [%s]" (statusOpenhabOrg)
DateTime openHABBuildServerLastUpdatedLast30Days "openHAB Build Server Last Updated Last 30 Days [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String openHABBuildServerAvailabilityLast30Days "openHAB Build Server Availability Last 30 Days [%s]" (statusOpenhabOrg)
String openHABBuildServerDowntimeLast30Days "openHAB Build Server Downtime Last 30 Days [%s]" (statusOpenhabOrg)
DateTime openHABBuildServerLastUpdatedLast90Days "openHAB Build Server Last Updated Last 90 Days [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String openHABBuildServerAvailabilityLast90Days "openHAB Build Server Availability Last90 Days [%s]" (statusOpenhabOrg)
String openHABBuildServerDowntimeLast90Days "openHAB Build Server Downtime Last 90 Days [%s]" (statusOpenhabOrg)

DateTime openHABDemoServerLastUpdatedLastHour "openHAB Demo Server Last Updated Last Hour [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String openHABDemoServerAvailabilityLastHour "openHAB Demo Server Availability Last Hour [%s]" (statusOpenhabOrg)
String openHABDemoServerDowntimeLastHour "openHAB Demo Server Downtime Last Hour [%s]" (statusOpenhabOrg)
DateTime openHABDemoServerLastUpdatedLast24Hours "openHAB Demo Server Last Updated Last 24 Hours [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String openHABDemoServerAvailabilityLast24Hours "openHAB Demo Server Availability Last 24 Hours [%s]" (statusOpenhabOrg)
String openHABDemoServerDowntimeLast24Hours "openHAB Demo Server Downtime Last 24 Hours [%s]" (statusOpenhabOrg)
DateTime openHABDemoServerLastUpdatedLast7Days "openHAB Demo Server Last Updated Last 7 Days [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String openHABDemoServerAvailabilityLast7Days "openHAB Demo Server Availability Last 7 Days [%s]" (statusOpenhabOrg)
String openHABDemoServerDowntimeLast7Days "openHAB Demo Server Downtime Last 7 Days [%s]" (statusOpenhabOrg)
DateTime openHABDemoServerLastUpdatedLast30Days "openHAB Demo Server Last Updated Last 30 Days [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String openHABDemoServerAvailabilityLast30Days "openHAB Demo Server Availability Last 30 Days [%s]" (statusOpenhabOrg)
String openHABDemoServerDowntimeLast30Days "openHAB Demo Server Downtime Last 30 Days [%s]" (statusOpenhabOrg)
DateTime openHABDemoServerLastUpdatedLast90Days "openHAB Demo Server Last Updated Last 90 Days [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String openHABDemoServerAvailabilityLast90Days "openHAB Demo Server Availability Last90 Days [%s]" (statusOpenhabOrg)
String openHABDemoServerDowntimeLast90Days "openHAB Demo Server Downtime Last 90 Days [%s]" (statusOpenhabOrg)

DateTime openHABOnlineRepositoryLastUpdatedLastHour "openHAB Online Repository Last Updated Last Hour [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String openHABOnlineRepositoryAvailabilityLastHour "openHAB Online Repository Availability Last Hour [%s]" (statusOpenhabOrg)
String openHABOnlineRepositoryDowntimeLastHour "openHAB Online Repository Downtime Last Hour [%s]" (statusOpenhabOrg)
DateTime openHABOnlineRepositoryLastUpdatedLast24Hours "openHAB Online Repository Last UpdatedL ast 24 Hours [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String openHABOnlineRepositoryAvailabilityLast24Hours "openHAB Online Repository Availability Last 24 Hours [%s]" (statusOpenhabOrg)
String openHABOnlineRepositoryDowntimeLast24Hours "openHAB Online Repository Downtime Last 24 Hours [%s]" (statusOpenhabOrg)
DateTime openHABOnlineRepositoryLastUpdatedLast7Days "openHAB Online Repository Last Updated Last 7 Days [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String openHABOnlineRepositoryAvailabilityLast7Days "openHAB Online Repository Availability Last 7 Days [%s]" (statusOpenhabOrg)
String openHABOnlineRepositoryDowntimeLast7Days "openHAB Online Repository Downtime Last 7 Days [%s]" (statusOpenhabOrg)
DateTime openHABOnlineRepositoryLastUpdatedLast30Days "openHAB Online Repository Last Updated Last 30 Days [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String openHABOnlineRepositoryAvailabilityLast30Days "openHAB Online Repository Availability Last 30 Days [%s]" (statusOpenhabOrg)
String openHABOnlineRepositoryDowntimeLast30Days "openHAB Online Repository Downtime Last 30 Days [%s]" (statusOpenhabOrg)
DateTime openHABOnlineRepositoryLastUpdatedLast90Days "openHAB Online Repository Last Updated Last 90 Days [%1$tY-%1$tm-%1$td %1$tH:%1$tM]" (statusOpenhabOrg)
String openHABOnlineRepositoryAvailabilityLast90Days "openHAB Online Repository Availability Last 90 Days [%s]" (statusOpenhabOrg)
String openHABOnlineRepositoryDowntimeLast90Days "openHAB Online Repository Downtime Last 90 Days [%s]" (statusOpenhabOrg)
```

#### Sitemaps

For easy testing you can create a sitemap like this:

```
sitemap Sitemap label="StatusOpenhabOrg" {
    Frame label="status.openhab.org" {
        Group item=statusOpenhabOrg
    }
}
```

#### Rules

We create a rule that the values get updated each hour.

```
rule "get openHAB's Live status from status.openhab.org"
when
    Time cron "0 0 * * * ? *" 
then
    executeCommandLine("/usr/bin/python3","/path/to/place/status_openhab.py")
end
```

To make sure that it works you have to add following to `/etc/openhab/misc/exec.whitelist`:

```
/usr/bin/python3 /path/to/place/status_openhab.py
```
