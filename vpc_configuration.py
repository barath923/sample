import boto3

client = boto3.client('ec2',region_name="ap-south-1",aws_access_key_id="AKIA6ODU57I5KE3IJ2YO",aws_secret_access_key="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")

# vpc=input("Enter the vpc cidr ")
# ##avazone=input("enter the Subnet's Availability Zone ")
# subnetcidr=input("enter the subnet's cidr ")
# routeentry=input("Enter igw route entry ")


myvpc1 = client.create_vpc(
    CidrBlock='10.10.0.0/16',
    TagSpecifications=[
        {
            'ResourceType':'vpc',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'boto3vpc'
                },
            ]
        },
    ]
)

print(myvpc1['Vpc']['VpcId'])

mysubnet1 = client.create_subnet(
    TagSpecifications=[
        {
            'ResourceType':'subnet',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Subnetbotot3_1'
                },
            ]
        },
    ],
    CidrBlock = '10.10.1.0/24',
    VpcId = myvpc1['Vpc']['VpcId']
)

print(mysubnet1['Subnet']['SubnetId'])

internet_gtw = client.create_internet_gateway(
    TagSpecifications=[
        {
            'ResourceType':'internet-gateway',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Igwbotot3_1'
                },
            ]
        },
    ],
)
print(internet_gtw['InternetGateway']['InternetGatewayId'])

igw_attachment = client.attach_internet_gateway(
    InternetGatewayId=internet_gtw['InternetGateway']['InternetGatewayId'],
    VpcId=myvpc1['Vpc']['VpcId']
)

route_table_1 = client.create_route_table(
    VpcId=myvpc1['Vpc']['VpcId'],
    TagSpecifications=[
        {
            'ResourceType':'route-table',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Rtboto3_1'
                },
            ]
        },
    ]
)
print(route_table_1['RouteTable']['RouteTableId'])

route1_rt = client.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gtw['InternetGateway']['InternetGatewayId'],
    RouteTableId=route_table_1['RouteTable']['RouteTableId'],
    
)

route_table_association = client.associate_route_table(
    SubnetId=mysubnet1['Subnet']['SubnetId'],
    RouteTableId=route_table_1['RouteTable']['RouteTableId'],
)



























