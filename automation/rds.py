def lambda_handler(event, context):
print("Connecting to RDS")
client = boto3.client('rds')

print("RDS snapshot backups stated at %s...\n" % datetime.datetime.now())
client.create_db_cluster_snapshot(
    DBClusterIdentifier='enter-your-cluster-name-her', 
    DBClusterSnapshotIdentifier='enter-your-cluster-name-here-%s' % datetime.datetime.now().strftime("%y-%m-%d-%H"),
    Tags=[
        {
            'Key': 'ENV',
            'Value': 'dev'
        },
    ]
)