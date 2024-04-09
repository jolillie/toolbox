#/bin/bash

# Couple of scripts to get data from Route53

# Get the list of Hosted Zones IDs in Route53

IDS=$(aws route53 list-hosted-zones  --query "HostedZones[*].Id" --region us-east-1 --output text | sed 's/\/hostedzone\///g')


for id in $IDS
do
  record_info=$(aws route53 list-resource-record-sets --region us-east-1 --output json --hosted-zone-id $id --query "ResourceRecordSets[*]")
  echo "$id: {$record_info}" >> test.json
done



# Couple of one liners to get data out of Route53

# Get the list of Hosted Zones IDs in Route53
aws route53 list-hosted-zones --query "HostedZones[?contains(Name, 'example.com')].Id" --output text | sed 's/\/hostedzone\///g' | pbcopy


aws route53 list-resource-record-sets --hosted-zone-id ZONE_ID --output text

aws route53 list-resource-record-sets --hosted-zone-id ZONE_ID --query "ResourceRecordSets[*].Name"