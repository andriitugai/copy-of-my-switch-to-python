import click

RULES = {
        'NewYork': lambda ticket_nums: sum(ticket_nums[:3]) == sum(ticket_nums[3:]),
        'Boston': lambda ticket_nums: sum(ticket_nums[::2]) == sum(ticket_nums[1::2]),
        'BlackJack': lambda ticket_nums: sum(ticket_nums[:3]) == 21 | sum(ticket_nums[3:]) == 21, # the sum of 1-3 or 4-6 digits is equal to 21
        'Palindrome': lambda ticket_nums: ticket_nums == ticket_nums[::-1]
    }


def ticket_checker(ticket, rule):
    def to_int_list(tckt):
        return [int(char) for char in tckt]
    return rule(to_int_list(ticket))


@click.command()
@click.option('--rule', '-r',
    type=click.Choice(RULES),
    prompt='Enter the way of checking for happiness', 
    help='The name of the rule to check the happiness', 
    show_default=True)
@click.option('--action', '-a',
    type=click.Choice(['count', 'print']), 
    help='The action to perform with happy tickets: just count or print to the console',
    default='count', 
    show_default=True)
@click.argument('file_path', 
    type=click.File('r'))
def cli(rule, action, file_path):
    '''
    Counts [COUNT] or prints [PRINT] the happy tickets from the file [FILE_PATH] 
    according to the rule name [RULE] provided
    '''
    
    tickets = (ticket.strip() for ticket in iter(file_path))
    happy_tickets = (ticket for ticket in tickets if ticket_checker(ticket, RULES[rule]))

    if action == 'print':
        for ticket in happy_tickets:
            # click.echo(f'{ticket}: {ticket_checker(ticket, RULES[rule])}')
            click.echo(f'{ticket}')
    elif action == 'count':
        result = sum(1 for _ in happy_tickets)
        print(f'\nThere are {result} "happy" tickets in file {file_path.name} counted by "{rule}" way.\n')
