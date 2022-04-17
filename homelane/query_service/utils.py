from typing import Any
from typing import Dict
from typing import List


BUDGET_SCHEMA = {"maxPrice":int, "minPrice":int}
SQFT_SCHEMA = {"minSqft":int}
YEAR_SCHEMA = {"year":int}
SCHEMA_TYPE = {"budget":BUDGET_SCHEMA, "sqft":SQFT_SCHEMA, 'year':YEAR_SCHEMA}
def validate_payload(payload: Dict[str, Any], check_fields: List[str], schema) -> Any:
    """
    Validate the request payload
    """

    if not all(
        True if chk in payload and payload.get(chk) and SCHEMA_TYPE[schema][chk] is type(payload.get(chk)) else False for chk in check_fields
    ):
        raise ValueError(",".join(check_fields) + " are required fields or might be invalid type")

