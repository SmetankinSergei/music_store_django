import json
import os

from django.core.management import BaseCommand

from catalog.models import Product, Category

TABLES_DICT = {'product': Product, 'category': Category}
TABLES_DATAFILES = ['category_data.json', 'product_data.json']


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for table in TABLES_DICT.values():
            table.objects.all().delete()

        for datafile in TABLES_DATAFILES:

            path = os.path.join('datafiles', datafile)

            with open(path) as file:
                tables_data = json.load(file)
                preloading_list = []
                table = None
                for item in tables_data:
                    table = TABLES_DICT[item['model'].split('.')[1]]
                    preloading_list.append(table(**item['fields']))
                table.objects.bulk_create(preloading_list)
