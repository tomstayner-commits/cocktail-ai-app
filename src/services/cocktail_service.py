from typing import Any

from fastapi import HTTPException

from src.database import table
from src.logging_config import logger
from src.models import Cocktail


def get_all_cocktails() -> list[dict[str, Any]]:

    logger.info("[SERVICE] Retrieving cocktail collection")

    response = table.scan()
    cocktails = response["Items"]

    logger.info(
        f"[SERVICE] Retrieved {len(cocktails)} cocktails"
    )

    return cocktails


def get_cocktail(cocktail_id: int) -> dict[str, Any]:

    logger.info(
        f"[SERVICE] Retrieving cocktail (ID {cocktail_id})"
    )

    response = table.get_item(
        Key={"id": cocktail_id}
    )

    item = response.get("Item")

    if not item:
        logger.warning(
            f"[SERVICE] Cocktail ID {cocktail_id} not found"
        )
        raise HTTPException(
            status_code=404,
            detail="Cocktail not found"
        )

    logger.info(
        f"[SERVICE] Retrieved cocktail '{item['name']}'"
    )

    return item


def create_cocktail(cocktail: Cocktail) -> dict[str, str]:

    logger.info(
        f"[SERVICE] Creating cocktail '{cocktail.name}' (ID {cocktail.id})"
    )

    table.put_item(
        Item={
            "id": cocktail.id,
            "name": cocktail.name,
            "spirit": cocktail.spirit,
            "ingredients": cocktail.ingredients,
        }
    )

    logger.info(
        f"[SERVICE] Created cocktail '{cocktail.name}'"
    )

    return {
        "message": "Cocktail added successfully"
    }


def delete_cocktail(cocktail_id: int) -> dict[str, str]:

    logger.info(
        f"[SERVICE] Deleting cocktail ID {cocktail_id}"
    )

    response = table.get_item(
        Key={"id": cocktail_id}
    )

    item = response.get("Item")

    if not item:
        logger.warning(
            f"[SERVICE] Delete failed - cocktail ID {cocktail_id} not found"
        )
        raise HTTPException(
            status_code=404,
            detail="Cocktail not found"
        )

    table.delete_item(
        Key={"id": cocktail_id}
    )

    logger.info(
        f"[SERVICE] Deleted cocktail '{item['name']}'"
    )

    return {
        "message": f"Cocktail {cocktail_id} deleted"
    }


def update_cocktail(cocktail_id: int, cocktail: Cocktail) -> dict[str, Any]:

    logger.info(
        f"[SERVICE] Updating cocktail ID {cocktail_id}"
    )

    response = table.get_item(
        Key={"id": cocktail_id}
    )

    if "Item" not in response:
        logger.warning(
            f"[SERVICE] Update failed - cocktail ID {cocktail_id} not found"
        )
        raise HTTPException(
            status_code=404,
            detail="Cocktail not found"
        )

    updated_cocktail = {
        "id": cocktail_id,
        "name": cocktail.name,
        "spirit": cocktail.spirit,
        "ingredients": cocktail.ingredients,
    }

    table.put_item(Item=updated_cocktail)

    logger.info(
        f"[SERVICE] Updated cocktail '{cocktail.name}'"
    )

    return updated_cocktail