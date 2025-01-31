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

from pci_parse_input import parse_event
def event():
    return {
        'expected_control_id': 'PCI.IAM.6',
        'parse_id_pattern': '^arn:aws:iam::[0-9]{12}:user/([A-Za-z0-9+=,.@-]{1,64})$',
        'Finding': {
            "SchemaVersion": "2018-10-08",
            "Id": "arn:aws:securityhub:us-east-1:111111111111:subscription/pci-dss/v/3.2.1/PCI.IAM.6/finding/fec91aaf-5016-4c40-9d24-9966e4be80c4",
            "ProductArn": "arn:aws:securityhub:us-east-1::product/aws/securityhub",
            "GeneratorId": "pci-dss/v/3.2.1/PCI.IAM.6",
            "AwsAccountId": "111111111111",
            "Types": [
                "Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS"
            ],
            "FirstObservedAt": "2021-06-01T18:39:09.192Z",
            "LastObservedAt": "2021-06-01T18:39:11.050Z",
            "CreatedAt": "2021-06-01T18:39:09.192Z",
            "UpdatedAt": "2021-06-01T18:39:09.192Z",
            "Severity": {
                "Product": 40,
                "Label": "MEDIUM",
                "Normalized": 40,
                "Original": "MEDIUM"
            },
            "Title": "PCI.IAM.6 MFA should be enabled for all IAM users",
            "Description": "This AWS control checks whether the AWS Identity and Access Management users have multi-factor authentication (MFA) enabled.",
            "Remediation": {
                "Recommendation": {
                "Text": "For directions on how to fix this issue, please consult the AWS Security Hub PCI DSS documentation.",
                "Url": "https://docs.aws.amazon.com/console/securityhub/PCI.IAM.6/remediation"
                }
            },
            "ProductFields": {
                "StandardsArn": "arn:aws:securityhub:::standards/pci-dss/v/3.2.1",
                "StandardsSubscriptionArn": "arn:aws:securityhub:us-east-1:111111111111:subscription/pci-dss/v/3.2.1",
                "ControlId": "PCI.IAM.6",
                "RecommendationUrl": "https://docs.aws.amazon.com/console/securityhub/PCI.IAM.6/remediation",
                "RelatedAWSResources:0/name": "securityhub-iam-user-mfa-enabled-8f8ddc5e",
                "RelatedAWSResources:0/type": "AWS::Config::ConfigRule",
                "StandardsControlArn": "arn:aws:securityhub:us-east-1:111111111111:control/pci-dss/v/3.2.1/PCI.IAM.6",
                "aws/securityhub/ProductName": "Security Hub",
                "aws/securityhub/CompanyName": "AWS",
                "Resources:0/Id": "arn:aws:iam::111111111111:user/foo-bar@baz",
                "aws/securityhub/FindingId": "arn:aws:securityhub:us-east-1::product/aws/securityhub/arn:aws:securityhub:us-east-1:111111111111:subscription/pci-dss/v/3.2.1/PCI.IAM.6/finding/fec91aaf-5016-4c40-9d24-9966e4be80c4"
            },
            "Resources": [
                {
                "Type": "AwsIamUser",
                "Id": "arn:aws:iam::111111111111:user/foo-bar@baz",
                "Partition": "aws",
                "Region": "us-east-1",
                "Details": {
                    "AwsIamUser": {
                    "CreateDate": "2016-09-23T12:42:13.000Z",
                    "Path": "/",
                    "UserId": "AIDAIMALBCBBI4ZZHJVTO",
                    "UserName": "foo-bar@baz"
                    }
                }
                }
            ],
            "Compliance": {
                "Status": "FAILED",
                "RelatedRequirements": [
                "PCI DSS 8.3.1"
                ]
            },
            "WorkflowState": "NEW",
            "Workflow": {
                "Status": "NEW"
            },
            "RecordState": "ACTIVE",
            "FindingProviderFields": {
                "Severity": {
                "Label": "MEDIUM",
                "Original": "MEDIUM"
                },
                "Types": [
                "Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS"
                ]
            }
        }
    }

def expected():
    return {
        "account_id": '111111111111',
        "resource_id": 'foo-bar@baz',
        'control_id': 'PCI.IAM.6',
        'testmode': False,
        "finding_id": 'arn:aws:securityhub:us-east-1:111111111111:subscription/pci-dss/v/3.2.1/PCI.IAM.6/finding/fec91aaf-5016-4c40-9d24-9966e4be80c4',
        "product_arn": 'arn:aws:securityhub:us-east-1::product/aws/securityhub',
        "object": {
            "Type": 'AwsIamUser',
            "Id": 'foo-bar@baz',
            "OutputKey": 'Remediation.Output'
        },
        "matches": [ "foo-bar@baz" ],
        'details': {'AwsIamUser': {'CreateDate': '2016-09-23T12:42:13.000Z', 'Path': '/', 'UserId': 'AIDAIMALBCBBI4ZZHJVTO', 'UserName': 'foo-bar@baz'}}
    }

def test_parse_event():
    parsed_event = parse_event(event(), {})
    assert parsed_event == expected()

def test_parse_event_multimatch():
    expected_result = expected()
    expected_result['matches'] = [
        "iam",
        "foo-bar@baz"
    ]
    test_event = event()
    test_event['resource_index'] = 2
    test_event['parse_id_pattern'] = '^arn:aws:(.*?)::[0-9]{12}:user/([A-Za-z0-9+=,.@-]{1,64})$'
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
    test_event['Finding']['Id'] = "arn:aws:securityhub:us-east-1:111111111111:subscription/pci-dss/v/3.2.1//finding/fec91aaf-5016-4c40-9d24-9966e4be80c4"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        parsed_event = parse_event(test_event, {})
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 'ERROR: Finding is missing Control Id: arn:aws:securityhub:us-east-1:111111111111:subscription/pci-dss/v/3.2.1//finding/fec91aaf-5016-4c40-9d24-9966e4be80c4'

def test_control_id_nomatch():
    test_event = event()
    test_event['Finding']['Id'] = "arn:aws:securityhub:us-east-2:111111111111:subscription/pci-dss/v/3.2.1/2.4/finding/fec91aaf-5016-4c40-9d24-9966e4be80c4"
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        parsed_event = parse_event(test_event, {})
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 'ERROR: Control Id from input (2.4) does not match PCI.IAM.6'

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
    assert pytest_wrapped_e.value.code == 'ERROR: Invalid resource Id arn:aws:iam::111111111111:user/foo-bar@baz'

def test_no_resource_pattern():
    test_event = event()
    expected_result = expected()

    test_event['parse_id_pattern'] = ''
    expected_result['resource_id'] = 'arn:aws:iam::111111111111:user/foo-bar@baz'
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
