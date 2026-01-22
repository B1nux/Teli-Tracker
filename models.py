from dataclasses import dataclass
from datetime import datetime


@dataclass
class Vendor:
    name: str
    contact_email: str
    notes: str = ""

@dataclass
class Interaction:
    vendor_name: str
    keywords: str
    notes: str = ""
    unit_price: float | None = None
    quantity: int | None = None
    created_at: datetime = datetime.now()
 