import json
import struct
import uuid

from datetime import datetime

def b_parser(data_bytes):
    '''
    Binary parser for info about item
    param: data_bytes - byte-string the length of 13 which contains the info
    Returns a pretty json-formated string
    (see docs for more info)
    '''
    ITEM_FORMAT = '!I3sHf' # looking at the example, it seems they assumed network or big-endian order of bytes

    item_id, mark, country_id, rate = struct.unpack(ITEM_FORMAT, data_bytes)

    item_data = { 
        "country_id": country_id,
        "item_id": item_id,
        "mark": mark.decode('utf-8'),
        "rate": rate,
        "timestamp": int(datetime.now().timestamp()),
        "uuid": str(uuid.uuid4())
    }

    return json.dumps(item_data, indent=4, separators=(',', ': '))

def main():

    z = b_parser(b'I\x96\x02\xd2dEl\xd41@H\xf5\xc3')
    type(z)

    print(z)


if __name__ == '__main__':
    main()









