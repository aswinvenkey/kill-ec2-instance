import boto3;

ec2 = boto3.resource("ec2");

#create a file to save the file locally
outfile =   open("ec2-new-keypair.pem","w");

#calling funtion to create a key pair
key_pair = ec2.create_key_pair(KeyName='ec2-new-keypair')

#store it in a file
keypairout = str(key_pair.key_material)
print(keypairout);
outfile.write(keypairout);