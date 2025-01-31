#!/usr/bin/python
###############################################################################
#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.    #
#                                                                             #
#  Licensed under the Apache License Version 2.0 (the "License"). You may not #
#  use this file except in compliance with the License. A copy of the License #
#  is located at                                                              #
#                                                                             #
#      http://www.apache.org/licenses/LICENSE-2.0/                                        #
#                                                                             #
#  or in the "license" file accompanying this file. This file is distributed  #
#  on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, express #
#  or implied. See the License for the specific language governing permis-    #
#  sions and limitations under the License.                                   #
###############################################################################
import pytest

from cis_parse_input import parse_event
def event():
    return {
        'expected_control_id': '2.3',
        'parse_id_pattern': '^arn:(?:aws|aws-cn|aws-us-gov):s3:::([A-Za-z0-9.-]{3,63})$',
        'Finding': {
            "ProductArn": "arn:aws:securityhub:us-east-2::product/aws/securityhub",
            "Types": [
                "Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark"
            ],
            "Description": "Details: 2.3 Ensure the S3 bucket used to store CloudTrail logs is not publicly accessible",
            "SchemaVersion": "2018-10-08",
            "Compliance": {
                "Status": "WARNING",
                "StatusReasons": [
                    {
                        "Description": "The finding is in a WARNING state, because the S3 Bucket associated with this rule is in a different region/account. This rule does not support cross-region/cross-account checks, so it is recommended to disable this control in this region/account and only run it in the region/account where the resource is located.",
                        "ReasonCode": "S3_BUCKET_CROSS_ACCOUNT_CROSS_REGION"
                    }
                ]
            },
            "GeneratorId": "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/2.3",
            "FirstObservedAt": "2020-05-20T05:02:44.203Z",
            "CreatedAt": "2020-05-20T05:02:44.203Z",
            "RecordState": "ACTIVE",
            "Title": "2.3 Ensure the S3 bucket used to store CloudTrail logs is not publicly accessible",
            "Workflow": {
                "Status": "NEW"
            },
            "LastObservedAt": "2020-06-17T13:01:35.884Z",
            "Severity": {
                "Normalized": 90,
                "Label": "CRITICAL",
                "Product": 90,
                "Original": "CRITICAL"
            },
            "UpdatedAt": "2020-06-17T13:01:25.561Z",
            "WorkflowState": "NEW",
            "ProductFields": {
                "StandardsGuideArn": "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0",
                "StandardsGuideSubscriptionArn": "arn:aws:securityhub:us-east-2:111111111111:subscription/cis-aws-foundations-benchmark/v/1.2.0",
                "RuleId": "2.3",
                "RecommendationUrl": "https://docs.aws.amazon.com/console/securityhub/standards-cis-2.3/remediation",
                "RelatedAWSResources:0/name": "securityhub-s3-bucket-public-read-prohibited-4414615a",
                "RelatedAWSResources:0/type": "AWS::Config::ConfigRule",
                "RelatedAWSResources:1/name": "securityhub-s3-bucket-public-write-prohibited-f104fcda",
                "RelatedAWSResources:1/type": "AWS::Config::ConfigRule",
                "StandardsControlArn": "arn:aws:securityhub:us-east-2:111111111111:control/cis-aws-foundations-benchmark/v/1.2.0/2.3",
                "aws/securityhub/SeverityLabel": "CRITICAL",
                "aws/securityhub/ProductName": "Security Hub",
                "aws/securityhub/CompanyName": "AWS",
                "aws/securityhub/annotation": "The finding is in a WARNING state, because the S3 Bucket associated with this rule is in a different region/account. This rule does not support cross-region/cross-account checks, so it is recommended to disable this control in this region/account and only run it in the region/account where the resource is located.",
                "aws/securityhub/FindingId": "arn:aws:securityhub:us-east-2::product/aws/securityhub/arn:aws:securityhub:us-east-2:111111111111:subscription/cis-aws-foundations-benchmark/v/1.2.0/2.3/finding/f51c716c-b33c-4949-b748-2ffd22bdceec"
            },
            "AwsAccountId": "111111111111",
            "Id": "arn:aws:securityhub:us-east-2:111111111111:subscription/cis-aws-foundations-benchmark/v/1.2.0/2.3/finding/f51c716c-b33c-4949-b748-2ffd22bdceec",
            "Remediation": {
                "Recommendation": {
                    "Text": "For directions on how to fix this issue, please consult the AWS Security Hub CIS documentation.",
                    "Url": "https://docs.aws.amazon.com/console/securityhub/standards-cis-2.3/remediation"
                }
            },
            "Resources": [
                {
                    "Partition": "aws",
                    "Type": "AwsS3Bucket",
                    "Region": "us-east-2",
                    "Id": "arn:aws:s3:::cloudtrail-awslogs-111111111111-kjfskljdfl"
                }
            ]
        }
    }

def expected():
    return {
        "account_id": '111111111111',
        "resource_id": 'cloudtrail-awslogs-111111111111-kjfskljdfl',
        "finding_id": 'arn:aws:securityhub:us-east-2:111111111111:subscription/cis-aws-foundations-benchmark/v/1.2.0/2.3/finding/f51c716c-b33c-4949-b748-2ffd22bdceec',
        "product_arn": 'arn:aws:securityhub:us-east-2::product/aws/securityhub',
        "control_id": '2.3',
        "object": {
            "Type": 'AwsS3Bucket',
            "Id": 'cloudtrail-awslogs-111111111111-kjfskljdfl',
            "OutputKey": 'Remediation.Output'
        },
        "matches": [ "cloudtrail-awslogs-111111111111-kjfskljdfl" ],
        'details': {},
        'testmode': False
    }

def cis41_event():
    return {
        'expected_control_id': '4.1',
        'parse_id_pattern': '^arn:(?:aws|aws-cn|aws-us-gov):ec2:(?:[a-z]{2}(?:-gov)?-[a-z]+-[0-9]):[0-9]{12}:security-group/(sg-[a-f0-9]{8,17})$',
        'Finding': {
            "SchemaVersion": "2018-10-08",
            "Id": "arn:aws:securityhub:us-east-1:111111111111:subscription/cis-aws-foundations-benchmark/v/1.2.0/4.1/finding/f371b170-1881-4af0-9a33-840c81d91a04",
            "ProductArn": "arn:aws:securityhub:us-east-1::product/aws/securityhub",
            "ProductName": "Security Hub",
            "CompanyName": "AWS",
            "Region": "us-east-1",
            "GeneratorId": "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/4.1",
            "AwsAccountId": "111111111111",
            "Types": [
                "Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark"
            ],
            "FirstObservedAt": "2020-05-08T08:56:08.195Z",
            "LastObservedAt": "2021-07-20T16:43:29.362Z",
            "CreatedAt": "2020-05-08T08:56:08.195Z",
            "UpdatedAt": "2021-07-20T16:43:26.312Z",
            "Severity": {
                "Product": 70,
                "Label": "HIGH",
                "Normalized": 70,
                "Original": "HIGH"
            },
            "Title": "4.1 Ensure no security groups allow ingress from 0.0.0.0/0 to port 22",
            "Description": "Security groups provide stateful filtering of ingress/egress network traffic to AWS resources. It is recommended that no security group allows unrestricted ingress access to port 22.",
            "Remediation": {
                "Recommendation": {
                "Text": "For directions on how to fix this issue, please consult the AWS Security Hub CIS documentation.",
                "Url": "https://docs.aws.amazon.com/console/securityhub/standards-cis-4.1/remediation"
                }
            },
            "ProductFields": {
                "StandardsGuideArn": "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0",
                "StandardsGuideSubscriptionArn": "arn:aws:securityhub:us-east-1:111111111111:subscription/cis-aws-foundations-benchmark/v/1.2.0",
                "RuleId": "4.1",
                "RecommendationUrl": "https://docs.aws.amazon.com/console/securityhub/standards-cis-4.1/remediation",
                "RelatedAWSResources:0/name": "securityhub-restricted-ssh-33f8347e",
                "RelatedAWSResources:0/type": "AWS::Config::ConfigRule",
                "StandardsControlArn": "arn:aws:securityhub:us-east-1:111111111111:control/cis-aws-foundations-benchmark/v/1.2.0/4.1",
                "aws/securityhub/ProductName": "Security Hub",
                "aws/securityhub/CompanyName": "AWS",
                "Resources:0/Id": "arn:aws:ec2:us-east-1:111111111111:security-group/sg-087af114e4ae4c6ea",
                "aws/securityhub/FindingId": "arn:aws:securityhub:us-east-1::product/aws/securityhub/arn:aws:securityhub:us-east-1:111111111111:subscription/cis-aws-foundations-benchmark/v/1.2.0/4.1/finding/f371b170-1881-4af0-9a33-840c81d91a04"
            },
            "Resources": [
                {
                "Type": "AwsEc2SecurityGroup",
                "Id": "arn:aws:ec2:us-east-1:111111111111:security-group/sg-087af114e4ae4c6ea",
                "Partition": "aws",
                "Region": "us-east-1",
                "Details": {
                    "AwsEc2SecurityGroup": {
                    "GroupName": "launch-wizard-17",
                    "GroupId": "sg-087af114e4ae4c6ea",
                    "OwnerId": "111111111111",
                    "VpcId": "vpc-e5b8f483",
                    "IpPermissions": [
                        {
                        "IpProtocol": "tcp",
                        "FromPort": 22,
                        "ToPort": 22,
                        "IpRanges": [
                            {
                            "CidrIp": "0.0.0.0/0"
                            }
                        ]
                        }
                    ],
                    "IpPermissionsEgress": [
                        {
                        "IpProtocol": "-1",
                        "IpRanges": [
                            {
                            "CidrIp": "0.0.0.0/0"
                            }
                        ]
                        }
                    ]
                    }
                }
                }
            ],
            "Compliance": {
                "Status": "FAILED"
            },
            "WorkflowState": "NEW",
            "Workflow": {
                "Status": "NOTIFIED"
            },
            "RecordState": "ACTIVE",
            "Note": {
                "Text": "Remediation failed for CIS control 4.1 in account 111111111111: No output available yet because the step is not successfully executed",
                "UpdatedBy": "update_text",
                "UpdatedAt": "2021-07-20T18:53:07.918Z"
            },
            "FindingProviderFields": {
                "Severity": {
                "Label": "HIGH",
                "Original": "HIGH"
                },
                "Types": [
                "Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark"
                ]
            }
        }
    }

def cis41_expected():
    return {
        "account_id": '111111111111',
        "resource_id": 'sg-087af114e4ae4c6ea',
        'testmode': False,
        "finding_id": 'arn:aws:securityhub:us-east-1:111111111111:subscription/cis-aws-foundations-benchmark/v/1.2.0/4.1/finding/f371b170-1881-4af0-9a33-840c81d91a04',
        "product_arn": 'arn:aws:securityhub:us-east-1::product/aws/securityhub',
        "control_id": '4.1',
        "object": {
            "Type": 'AwsEc2SecurityGroup',
            "Id": 'sg-087af114e4ae4c6ea',
            "OutputKey": 'Remediation.Output'
        },
        "matches": [ "sg-087af114e4ae4c6ea" ],
        'details': {'AwsEc2SecurityGroup': {'GroupId': 'sg-087af114e4ae4c6ea',
            'GroupName': 'launch-wizard-17',
            'IpPermissions': [{'FromPort': 22,
                'IpProtocol': 'tcp',
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}],
                'ToPort': 22}],
            'IpPermissionsEgress': [{'IpProtocol': '-1',
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}],
            'OwnerId': '111111111111',
            'VpcId': 'vpc-e5b8f483'}},
    }
def test_parse_event():
    parsed_event = parse_event(event(), {})
    assert parsed_event == expected()

def test_parse_cis41():
    parsed_event = parse_event(cis41_event(), {})
    assert parsed_event == cis41_expected()

def test_parse_event_multimatch():
    expected_result = expected()
    expected_result['matches'] = [
        "aws",
        "cloudtrail-awslogs-111111111111-kjfskljdfl"
    ]
    test_event = event()
    test_event['resource_index'] = 2
    test_event['parse_id_pattern'] = '^arn:((?:aws|aws-cn|aws-us-gov)):s3:::([A-Za-z0-9.-]{3,63})$'
    parsed_event = parse_event(test_event, {})
    assert parsed_event == expected_result

def test_bad_finding_id():
    test_event = event()
    test_event['Finding']['Id'] = "badvalue"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        parsed_event = parse_event(test_event, {})
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 'ERROR: Finding Id is invalid: badvalue'

def test_bad_control_id():
    test_event = event()
    test_event['Finding']['Id'] = "arn:aws:securityhub:us-east-2:111111111111:subscription/cis-aws-foundations-benchmark/v/1.2.0//finding/f51c716c-b33c-4949-b748-2ffd22bdceec"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        parsed_event = parse_event(test_event, {})
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 'ERROR: Finding Id is invalid: arn:aws:securityhub:us-east-2:111111111111:subscription/cis-aws-foundations-benchmark/v/1.2.0//finding/f51c716c-b33c-4949-b748-2ffd22bdceec - missing Control Id'

def test_control_id_nomatch():
    test_event = event()
    test_event['Finding']['Id'] = "arn:aws:securityhub:us-east-2:111111111111:subscription/cis-aws-foundations-benchmark/v/1.2.0/2.4/finding/f51c716c-b33c-4949-b748-2ffd22bdceec"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        parsed_event = parse_event(test_event, {})
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 'ERROR: Control Id from input (2.4) does not match 2.3'
    
def test_bad_account_id():
    test_event = event()
    test_event['Finding']['AwsAccountId'] = "1234123412345"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        parsed_event = parse_event(test_event, {})
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 'ERROR: AwsAccountId is invalid: 1234123412345'

def test_bad_productarn():
    test_event = event()
    test_event['Finding']['ProductArn'] = "badvalue"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        parsed_event = parse_event(test_event, {})
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 'ERROR: ProductArn is invalid: badvalue'

def test_bad_resource_match():
    test_event = event()
    test_event['parse_id_pattern'] = '^arn:(?:aws|aws-cn|aws-us-gov):logs:::([A-Za-z0-9.-]{3,63})$'
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        parsed_event = parse_event(test_event, {})
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 'ERROR: Invalid resource Id arn:aws:s3:::cloudtrail-awslogs-111111111111-kjfskljdfl'

def test_no_resource_pattern():
    test_event = event()
    expected_result = expected()

    test_event['parse_id_pattern'] = ''
    expected_result['resource_id'] = 'arn:aws:s3:::cloudtrail-awslogs-111111111111-kjfskljdfl'
    expected_result['matches'] = []
    expected_result['object']['Id'] = expected_result['resource_id']
    parsed_event = parse_event(test_event, {})
    assert parsed_event == expected_result

def test_no_resource_pattern_no_resource_id():
    test_event = event()

    test_event['parse_id_pattern'] = ''
    test_event['Finding']['Resources'][0]['Id'] = ''

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        parsed_event = parse_event(test_event, {})
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 'ERROR: Resource Id is missing from the finding json Resources (Id)'
