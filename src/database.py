import boto3
from src.logging_config import logger

AWS_REGION = "ap-southeast-2"
TABLE_NAME = "Cocktails"

dynamodb = boto3.resource(
    "dynamodb",
    region_name=AWS_REGION
)

table = dynamodb.Table(TABLE_NAME)

logger.info(
    f"[SYSTEM] AWS Region: {AWS_REGION}"
)

logger.info(
    f"[SYSTEM] Connected to DynamoDB table '{TABLE_NAME}'"
)