import argparse

RULES = {
        'NewYork': lambda ticket_nums: sum(ticket_nums[:3]) == sum(ticket_nums[3:]),
        'Boston': lambda ticket_nums: sum(ticket_nums[::2]) == sum(ticket_nums[1::2]),
        'Diablo': lambda ticket_nums: ticket_nums.count(6) == 3,
        'Palindrome': lambda ticket_nums: ticket_nums == ticket_nums[::-1]
    }


def parse_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('counter', 
            choices=['NewYork', 'Boston', 'Diablo', 'Palindrome'])

def ticket_checker(ticket, rule):
    def to_int_list(tckt):
        return [int(char) for char in tckt]
    return rule(to_int_list(ticket))

def main():
    
    
    tickets = [
        '135333',
        '123453',
        '456654',
        '898988',
        '898989',
        '000000',
        '112004',
        '666477',
    ]

    for ticket in tickets:
        print(f'{ticket} '+ ''.join([]))
        for 
        print('{} NY: {:>5}, BO: {:>5}, DI: {:>5}, PA: {:>5}'.format(ticket, 
                *[ticket_checker(ticket, RULES[rule]) for rule in RULES]))

if __name__ == '__main__':
    main()
