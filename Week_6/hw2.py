import logging


def log_error(message):
    logger = logging.getLogger(__name__)
    logger.error(f'{message}')


GET_DATA_QUERY = "SELECT id, date, stub_demo_field as {alias} FROM {env}demo_table"

query_context = {"alias": "python", "env": "dev_"}

def get_command_with_context(command: str, context: dict):
    """Get command, with context added"""

    try:
        return command.format(**context).replace('\n','').rstrip().lstrip()
    except Exception as err:
        log_error(f'Error when try to formatting query: {err}')
        return False
        