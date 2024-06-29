import boto3

client = boto3.client('ec2',region_name="us-east-1")

response = client.start_instances(
   InstanceIds=['i-0e46e73c3fb0a1013']
)
print("instance started")

##response = client.start_instances(
##    InstanceIds=['i-0e5ae2df1a38a6155']
##)
##print("instance started")



#myami
##response = client.create_image(
##    InstanceId='i-0e5ae2df1a38a6155',
##    Name='myami1',
##    TagSpecifications=[
##        {
##            'ResourceType':'image',
##            'Tags': [
##                {
##                    'Key': 'Name',
##                    'Value': 'mynewami'
##                },
##            ]
##        },
##    ]
##)
##print("image created")





##instance = client.create_instance(
##    BlockDeviceMappings=[
##        {
##            'DeviceName': 'string',
##            'VirtualName': 'string',
##            'Ebs': {
##                'DeleteOnTermination': True|False,
##                'Iops': 123,
##                'SnapshotId': 'string',
##                'VolumeSize': 123,
##                'VolumeType': 'standard'|'io1'|'io2'|'gp2'|'sc1'|'st1'|'gp3',
##                'KmsKeyId': 'string',
##                'Throughput': 123,
##                'OutpostArn': 'string',
##                'Encrypted': True|False
##            },
##            'NoDevice': 'string'
##        },
##    ],
##    ImageId='string',
##    InstanceType='t2.micro',
##    KeyName='dbserver',
##   MaxCount=1,
##    MinCount=1,
     
##    TagSpecifications=[
##       {
##            'ResourceType':'instance',
##            'Tags': [
##                {
##                    'Key': 'Name',
##                    'Value': 'ec2'
##              },
##            ]
##      },
##  ],
    
##)

##print("instance created ",instance)






















