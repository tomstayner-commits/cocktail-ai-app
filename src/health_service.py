from botocore.exceptions import BotoCoreError
from botocore.exceptions import ClientError

from src.database import table
from src.logging_config import logger


def is_dynamodb_ready() -> bool:
    """Return whether the configured DynamoDB table can be reached."""

    try:
        table.meta.client.describe_table(TableName=table.name)
    except (BotoCoreError, ClientError):
        logger.warning("[HEALTH] DynamoDB readiness check failed")
        return False
    except Exception:
        logger.exception("[HEALTH] Unexpected DynamoDB readiness check failure")
        return False

    return True
