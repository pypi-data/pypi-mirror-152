#
# Copyright 2021 DataRobot, Inc. and its affiliates.
#
# All rights reserved.
#
# DataRobot, Inc.
#
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
#
# Released under the terms of DataRobot Tool and Utility Agreement.
import json

import pytest
import responses


@pytest.fixture()
def deployments_data():
    deployments = [
        {
            "id": "5c6f7a9e9ca9b20017ff95a2",
            "label": "is_bad Predictions",
            "description": "",
            "model": {
                "projectId": "5c0a969859b00004ba52e41b",
                "targetName": "is_bad",
                "id": "5cb9c8b979872d014a0bb080",
                "type": "TensorFlow Deep Learning Classifier",
            },
            "defaultPredictionServer": {
                "id": "5a7c7a72192765001fc22769",
                "url": "https://pred.example.com",
                "datarobot-key": "27782",
            },
            "predictionUsage": {
                "dailyRates": [5, 2, 10, 5, 13, 4, 7],
                "lastTimestamp": "2019-04-22T04:03:45.000000Z",
            },
            "capabilities": {"supportsModelReplacement": True, "supportsDriftTracking": True},
            "permissions": [
                "CAN_SHARE",
                "CAN_VIEW",
                "CAN_DELETE_DEPLOYMENT",
                "CAN_MAKE_PREDICTIONS",
            ],
            "serviceHealth": {"status": "unknown"},
            "modelHealth": {
                "status": "unknown",
                "message": "1 important feature is drifting",
                "startDate": "2019-04-18T02:00:00.000000Z",
                "endDate": "2019-04-22T02:00:00.000000Z",
            },
            "accuracyHealth": {"status": "unavailable", "startDate": None, "endDate": None},
            "fairnessHealth": {
                "status": "unknown",
                "messages": [],
                "startDate": "2022-02-22T11:38:11.562862Z",
                "endDate": None,
                "protected_features_count": 0,
                "influential_fairness_metric": None,
            },
            "governance": {"approvalStatus": "APPROVED", "hasOpenedChangeRequests": False},
            "owners": {
                "count": 2,
                "preview": [
                    {
                        "id": "5a7c7a72192765001fc22812",
                        "first_name": "Joe",
                        "last_name": "Schmoe",
                        "email": "joe.schmoe@example.com",
                    },
                    {
                        "id": "5a7c7a72192765001fc86345",
                        "first_name": "Jane",
                        "last_name": "Doe",
                        "email": "jane.doe@example.com",
                    },
                ],
            },
            "predictionEnvironment": {
                "id": "60b012436635fc00909df857",
                "isManagedByManagementAgent": True,
                "name": "https://custom-models-eks-test.dynamic.orm.datarobot.com",
                "platform": "datarobot",
                "plugin": None,
            },
        },
        {
            "id": "5c6f7a9e9ca9b20017ff93b7",
            "label": "is_bad Predictions2",
            "description": None,
            "model": {
                "projectId": "5c0a969859b00004ba52e41b",
                "targetName": "is_bad",
                "id": "5cb9c8b979872d014a0bb080",
                "type": "TensorFlow Deep Learning Classifier",
            },
            "defaultPredictionServer": {
                "id": "5a7c7a72192765001fc22769",
                "url": "https://pred.example.com",
                "datarobot-key": "27782",
            },
            "predictionUsage": {"dailyRates": [], "lastTimestamp": None},
            "capabilities": {"supportsModelReplacement": False, "supportsDriftTracking": False},
            "permissions": [
                "CAN_SHARE",
                "CAN_VIEW",
                "CAN_DELETE_DEPLOYMENT",
                "CAN_MAKE_PREDICTIONS",
            ],
            "serviceHealth": {"status": "unknown"},
            "modelHealth": {"status": "unknown", "startDate": None, "endDate": None},
            "accuracyHealth": {"status": "unavailable", "startDate": None, "endDate": None},
            "fairnessHealth": {
                "status": "unknown",
                "messages": [],
                "startDate": "2022-02-21T11:31:48.390512Z",
                "endDate": "2022-02-22T11:26:15.921576Z",
                "protected_features_count": 0,
                "influential_fairness_metric": None,
            },
            "governance": {"approvalStatus": "APPROVED", "hasOpenedChangeRequests": False},
            "owners": {
                "count": 1,
                "preview": [
                    {
                        "id": "5a7c7a72192765001fc22812",
                        "first_name": "Joe",
                        "last_name": "Schmoe",
                        "email": "joe.schmoe@example.com",
                    }
                ],
            },
            "predictionEnvironment": {
                "id": "60b012436635fc00909df857",
                "isManagedByManagementAgent": False,
                "name": "https://custom-models-eks-test.dynamic.orm.datarobot.com",
                "platform": "datarobot",
                "plugin": None,
            },
        },
    ]
    return deployments


@pytest.fixture()
def deployment_data(deployments_data):
    return deployments_data[0]


@pytest.fixture()
def deployment_get_response(unittest_endpoint, deployments_data):
    for deployment_data in deployments_data:
        url = "{}/{}/{}/".format(unittest_endpoint, "deployments", deployment_data["id"])
        responses.add(
            responses.GET,
            url,
            status=200,
            content_type="application/json",
            body=json.dumps(deployment_data),
        )
