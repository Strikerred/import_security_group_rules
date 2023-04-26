import boto3
import json

filters = [dict(Name='group-name', Values=['security_group_name'])]
client = boto3.client('ec2')
response = client.describe_security_groups(Filters=filters)

rules = []
sg_rules = []
num_rules = 0

for sg in response['SecurityGroups']:
    for ingressrule in sg['IpPermissions']:
        protocol = ingressrule['IpProtocol']
        from_port = ingressrule.get('FromPort', -1)
        to_port = ingressrule.get('ToPort', -1)
        if from_port == -1:
            from_port = to_port
        ip_ranges = []
        for iprange in ingressrule['IpRanges']:
            cidr_ip = iprange.get('CidrIp', None)
            description = iprange.get('Description', None)
            if cidr_ip:
                ip_ranges.append({'cidr_ip': cidr_ip, 'description': description})
        for groupid in ingressrule['UserIdGroupPairs']:
            group_id = groupid.get('GroupId', None)
            description = groupid.get('Description', None)
            if group_id:
                ip_ranges.append({'cidr_ip': group_id, 'description': description})
        rule = {
            'protocol': protocol,
            'from_port': from_port,
            'to_port': to_port,
            'ip_ranges': ip_ranges
        }
        rules.append(rule)

for rule in rules:
    for ip_range in rule['ip_ranges']:
        sg_rule = {
            'description': ip_range['description'],
            'protocol': rule['protocol'],
            'from_port': rule['from_port'],
            'to_port': rule['to_port'],
            'cidr_blocks': [ip_range['cidr_ip']] if not ip_range['cidr_ip'].startswith('sg-') else [""],
            'source_security_group_id': ip_range['cidr_ip'] if ip_range['cidr_ip'].startswith('sg-') else ""
        }
        sg_rules.append(sg_rule)

json_string = json.dumps(sg_rules, indent=4)
print(json_string)

for i, rule in enumerate(rules):
    for j, ip_range in enumerate(rule['ip_ranges']):
        protocol = rule['protocol']
        from_port = rule['from_port']
        to_port = rule['to_port']
        import_string = f'terraform import "aws_security_group_rule.ingress_rule[{num_rules}]" {sg["GroupId"]}_ingress_{protocol}_{from_port}_{to_port}_{ip_range["cidr_ip"]}'
        print(import_string)
        num_rules += 1
