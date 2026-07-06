import boto3
from src.logging_config import logger
from dotenv import load_dotenv
import os

load_dotenv()

AWS_REGION = os.getenv("AWS_REGION")
TABLE_NAME = os.getenv("TABLE_NAME")

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