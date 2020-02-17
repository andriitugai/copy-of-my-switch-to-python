from collections.abc import Iterable

def flatten(seq):
    '''Return an iterable from iterable of iterables
    '''
    for item in seq:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from flatten(item)
        else:
            yield item
            
def main():
    a  = [1,[2,3,[4,5],6],7,8,'Hello', {3,(4,5),6}]

    print(*flatten(a))


if __name__ == '__main__':
    main()
    
