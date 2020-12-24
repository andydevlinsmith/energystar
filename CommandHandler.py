import argparse
import logging

logging.basicConfig(level=logging.INFO)


class Query:
    """Abstracts a command-line query."""

    def __init__(self, query_type, data):
        self.query_type = query_type
        self.data = data

    def is_search(self):
        return self.query_type == 'search'

    def get_product(self):
        return self.data.get('product', None)

    def get_brand(self):
        return self.data.get('brand', None)

    def get_model(self):
        return self.data.get('model', None)

    def get_terms(self):
        return self.data.get('terms', None)


class CommandInterpreter:
    """
    Translate command-line input.

    Returns a query object.
    """

    def __init__(self, service):
        self.es_service = service

    def parse_args(self, args):
        try:
            parser = argparse.ArgumentParser()
            subparsers = parser.add_subparsers()
            product_parser = subparsers.add_parser(
                'get', help='get [ev|tv|ups] -b brand -m model')
            product_parser.add_argument(
                'product', type=str, help='Product type: ev, tv, or ups')
            product_parser.add_argument(
                '-b', '--brand', type=str, dest='brand',
                nargs='*', help='Brand name', required=True)
            product_parser.add_argument(
                '-m', '--model', type=str, dest='model',
                nargs='*', help='Model', required=True)
            product_parser.set_defaults(func=self.parse_get)

            search_parser = subparsers.add_parser(
                'search', help='search [ev|tv|ups] -t term')
            search_parser.add_argument(
                'product', type=str,
                help='Product type: ev, tv, or ups')
            search_parser.add_argument(
                '-t', '--term', type=str, dest='terms',
                nargs='*', help='Search term(s), e.g. watts', required=True)
            search_parser.set_defaults(func=self.parse_search)
            args = parser.parse_args(args)
            result = args.func(args)
            return result
        except AttributeError as e:
            extra = {'error': str(e)}
            logging.error("No arguments to process.", extra=extra)
            raise

    def stringify_args(self, args):
        if type(args) == list:
            return ' '.join(args).lower()
        return(args.lower())

    def parse_get(self, args):
        data = {
            'type': 'get',
            'product': args.product,
            'brand': self.stringify_args(args.brand),
            'model': self.stringify_args(args.model)
        }

        return Query('get', data)

    def parse_search(self, args):
        terms = self.stringify_args(args.terms)
        data = {
            'product': args.product,
            'terms': terms
        }

        return Query('search', data)
