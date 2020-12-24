import sys
from EnergyStarService import EnergyStarService
from CommandHandler import CommandInterpreter


if __name__ == "__main__":
    es_svc = EnergyStarService()
    ch = CommandInterpreter(es_svc)
    try:
        query = ch.parse_args(sys.argv[1:])
        result = es_svc.process_query(query)
        result.output_results()
    except AttributeError:
        print("For help enter -h")
