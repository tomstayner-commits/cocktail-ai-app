import logging
from unittest.mock import MagicMock

from botocore.exceptions import ClientError

from src import health_service


def test_is_dynamodb_ready_describes_configured_table(monkeypatch):
    table = MagicMock()
    table.name = "cocktails"
    monkeypatch.setattr(health_service, "table", table)

    assert health_service.is_dynamodb_ready() is True
    table.meta.client.describe_table.assert_called_once_with(TableName=table.name)


def test_is_dynamodb_ready_returns_false_for_aws_failure(
    monkeypatch,
    caplog,
):
    table = MagicMock()
    table.meta.client.describe_table.side_effect = ClientError(
        error_response={
            "Error": {
                "Code": "AccessDeniedException",
                "Message": "Denied",
            }
        },
        operation_name="DescribeTable",
    )
    monkeypatch.setattr(health_service, "table", table)

    with caplog.at_level(logging.WARNING):
        result = health_service.is_dynamodb_ready()

    assert result is False
    assert "DynamoDB readiness" in caplog.text


def test_is_dynamodb_ready_returns_false_for_unexpected_failure(
    monkeypatch,
    caplog,
):
    table = MagicMock()
    table.meta.client.describe_table.side_effect = RuntimeError(
        "unexpected test failure"
    )
    monkeypatch.setattr(health_service, "table", table)

    with caplog.at_level(logging.ERROR):
        result = health_service.is_dynamodb_ready()

    assert result is False
    assert "Unexpected DynamoDB readiness" in caplog.text
