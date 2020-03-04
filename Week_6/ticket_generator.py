import string
import random
import click

def generate_ticket():
    return ''.join(
            [
                random.choice(string.digits) 
                for _ in range(6)
            ]
        )

@click.command()
@click.option('--number','-n',
    default=1_000,
    help='How many ticket numbers to generate.')
@click.argument('out', 
    type=click.File('w'), 
    default='-', 
    required=False)
def main(number, out):
    '''
    Generates NUMBER random 6-digits ticket numbers and write they to OUT file
    '''
    for _ in range(number):
        click.echo(generate_ticket(), file=out)

# if __name__ == '__main__':
#     main()
