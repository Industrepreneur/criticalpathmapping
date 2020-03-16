import random

from mapping.accounts.models import Company
from mapping.tracking.models import Product


types = [
    'Widget',
    'Gadget',
    'Gizmo',
    'Thingymabob',
    'Gear',
    'Spring',
    'Doohicky',
    'Gidget',
    'Flange',
    'Device',
    'Tool',
    'Hinge',
    'Pinion',
    'Helical Gear',
    'Spiral Bevel Gear',
    ]


def purge_products():
    Product.objects.all().delete()


def populate_products():
    companies = Company.objects.all()

    for c in companies:
        iterations = random.randint(0, 8)

        for i in range(0, iterations):
            num = random.randint(1, 3200)
            type = random.choice(types)
            name = '%s #%i' % (type, num)

            Product.objects.create(
                name=name,
                company=c,
                created_by_id=1,
                )


def run():
    purge_products()
    populate_products()
