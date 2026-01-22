from models import Vendor, Interaction

vendor = Vendor(
    name="Wesco",
    contact_email="sales@wesco.com",
    notes="Good pricing on cables and connectors"
)

interaction = Interaction(
    vendor_name=vendor.name,
    keywords="cisco, sfp",
    notes="quoted fast, good response time",
    unit_price=129.99,
    quantity=10
)

print(vendor)
print(interaction)