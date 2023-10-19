# import_security_group_rules

This script facilitate the work of importing several security group rules in a security group while using terraform. The python script has generated an output of 38 sg rules which are stored as a json file, then you can loop through it and import them to your terraform state.

```
[
    {
        "description": "",
        "protocol": "tcp",
        "from_port": 5000,
        "to_port": 7000,
        "cidr_blocks": [
            ""
        ],
        "source_security_group_id": "sg-xxxxxxx0cbdxxxxxx"
    },
    {
        "description": "OpenVPN access",
        "protocol": "udp",
        "from_port": 1194,
        "to_port": 1194,
        "cidr_blocks": [
            "XX.XX.XXX.XX/XX"
        ],
        "source_security_group_id": ""
    },
    {
        "description": "SSH",
        "protocol": "tcp",
        "from_port": 22,
        "to_port": 22,
        "cidr_blocks": [
            ""
        ],
        "source_security_group_id": "sg-xxxxxxxbebbxxxxx"
    },
    {
        "description": "",
        "protocol": "udp",
        "from_port": 4500,
        "to_port": 4500,
        "cidr_blocks": [
            "XX.XXX.XX.XXX/XX"
        ],
        "source_security_group_id": ""
    },
    {
        "description": "",
        "protocol": "udp",
        "from_port": 500,
        "to_port": 500,
        "cidr_blocks": [
            "XX.XXX.XX.XXX/XX"
        ],
        "source_security_group_id": ""
    },
    {
        "description": "Prod",
        "protocol": "tcp",
        "from_port": 6080,
        "to_port": 6080,
        "cidr_blocks": [
            ""
        ],
        "source_security_group_id": "sg-xxxxxxxx"
    },
    {
        "description": "ntopng",
        "protocol": "tcp",
        "from_port": 3000,
        "to_port": 3000,
        "cidr_blocks": [
            ""
        ],
        "source_security_group_id": "sg-xxxxxxxxxxx"
    },
    {
        "description": "Admin Console",
        "protocol": "tcp",
        "from_port": 443,
        "to_port": 443,
        "cidr_blocks": [
            ""
        ],
        "source_security_group_id": "sg-xxxxxxxxxxxx"
    },
    {
        "description": "PING response",
        "protocol": "icmp",
        "from_port": 8,
        "to_port": -1,
        "cidr_blocks": [
            "XXX.XX.XX.XXX/XX"
        ],
        "source_security_group_id": ""
    }
]
```
```
terraform import aws_security_group_rule.ingress_rule[0] sg-xxxxxxxxxx_ingress_tcp_5000_7000_sg-xxxxxxxx
.
terraform import aws_security_group_rule.ingress_rule[9] sg-xxxxxxxxxx_ingress_udp_1194_1194_xx.xx.xx.xx/xx
terraform import aws_security_group_rule.ingress_rule[10] sg-xxxxxxxxxx_ingress_tcp_22_22_sg-xxxxxxxxxx
terraform import aws_security_group_rule.ingress_rule[11] sg-xxxxxxxxxx_ingress_udp_4500_4500_xx.xx.xx.xx/xx
.
terraform import aws_security_group_rule.ingress_rule[22] sg-xxxxxxxxxx_ingress_udp_500_500_xx.xx.xx.xx/xx
.
terraform import aws_security_group_rule.ingress_rule[33] sg-xxxxxxxxxx_ingress_tcp_6080_6080_sg-xxxxxxxx
.
terraform import aws_security_group_rule.ingress_rule[35] sg-xxxxxxxxxx_ingress_tcp_3000_3000_sg-xxxxxxxx
terraform import aws_security_group_rule.ingress_rule[36] sg-xxxxxxxxxx_ingress_tcp_443_443_sg-0xxxxxxxx
terraform import aws_security_group_rule.ingress_rule[37] sg-xxxxxxxxxx_ingress_icmp_8_-1_xxx.xx.xx.xxx/xx
```
