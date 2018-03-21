# use python format tools

import json

data = '{"status": "OK", "count": 2, "results": [{"age": 27, "name": "Oz", "lactose_intolerant": true}, {"age": 29, ' \
       '"name": "Joe", "lactose_intolerant": false}]}'


print(json.dumps(data))