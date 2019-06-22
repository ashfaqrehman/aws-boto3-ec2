#!/usr/bin/env python

# import libraries
try:
    import sys
    import boto3
except ImportError:
    sys.exit('One or more modules could not be imported. Make sure to \'pip install -r requirements.txt\'. Exiting.')
if sys.hexversion < 0x02070000:
    sys.exit('Python 2.7 or later is required.')    

# establish aws profile
#session =  boto3.Session(profile_name='saml', region_name='us-west-2')

# establish client 
#ec2_client = session.client('ec2')
ec2_client = boto3.client('ec2')

# establish variables, lists, dictionaries, etc.
filters = [{
            'Name': 'tag:Name',
            'Values': ['Jenkins*']
          }]

# establish resource sessions
#response = ec2_client.describe_instances(Filters=filters)
response = ec2_client.describe_instances()
for reservation in response["Reservations"]:
  for instance in reservation["Instances"]:
      print(instance["InstanceId"] + "...starting")
      #print("Status.." + instance["State"]["Name"])
      id=[instance["InstanceId"]]
      response=ec2_client.stop_instances(InstanceIds=id)
      #waiter = ec2_client.get_waiter('instance_running')
      #waiter.wait(InstanceIds=id)
      #print(instance["InstanceId"] + "...started")
