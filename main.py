import boto3;
from datetime import datetime,timezone,timedelta

#create an object for ec2 client from boto3
client = boto3.client('ec2')
response = client.describe_instances();
resource = boto3.resource('ec2')

#below logic parses through the response checks if any running instance
#has been running for more than an hour and terminates it.
for r in response['Reservations']:
    for i in r['Instances']:
        print (i['InstanceId'], i['LaunchTime'])
        now_utc = datetime.now(timezone.utc)
        instance_id = i['InstanceId']
        currentInstance = resource.Instance(instance_id)
        instance_launch_time = i['LaunchTime'] + timedelta(minutes=35)
        diff_time = now_utc - instance_launch_time;
        if(now_utc > instance_launch_time):
            print("Going to kill instances");
            currentInstance.terminate();
