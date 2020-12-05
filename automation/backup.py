import json
import boto3 
import time
from botocore.exceptions import ClientError 
def lambda_handler(event, context):
    # EC2 Client
    client = boto3.client('ec2', region_name='us-east-2')
    # Get Volume ID of EBS attached to EC2 Instnace
    response = client.describe_volumes()
    if len(response['Volumes']) > 0:
        for k in response['Volumes']:
            print("EBS Volume ID : ",k['VolumeId'], " of EC2 Instance : ", k['Attachments'][0]['InstanceId'])
    try:
        # Create a Snapshot of Volume
        responsesnapsnot = client.create_snapshot(VolumeId= k['VolumeId'])
        print("Snapshot Created with ID : ", responsesnapsnot['SnapshotId'])
    except Exception as e:
        print("some error :", e)
        
    # Get snapshot resource 
    ec2resource = boto3.resource('ec2', region_name='us-east-2')
    snapshot = ec2resource.Snapshot(responsesnapsnot['SnapshotId'])
    
    volumename = k['VolumeId']
    
    # Add volume name to snapshot for easier identification
    snapshot.create_tags(Tags=[{'Key': 'backup','Value': volumename}])
    
    return {
        'statusCode': 200,
    }