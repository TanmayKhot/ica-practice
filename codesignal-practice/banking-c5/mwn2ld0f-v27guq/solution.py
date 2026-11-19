from dataclasses import dataclass

def solution(queries):

    @dataclass
    class Account:
        name: str
        amount: int = 0
        record: int = 0

    res = []
    data = {}

    def create(name, value):
        for i in data:
            if data[i].name == name:
                return "false"
        id = len(data) 
        if value:
            value = int(value)
            data[id] = Account(name,int(value))
        else:
            data[id] = Account(name)
        return "true"
    
    def get(name):

        for i in data:
            if name == data[i].name:
                if data[i].amount > 0:
                    return str(data[i].amount)
                return str(i)
        return ""

    def delete(name):
        for i in data:
            if data[i].name == name:
                data.pop(i, None)
                return "true"
        return "false"
        
    def record(name, amount):
        for i in data:
            if data[i].name == name:
                data[i].record += int(amount)
                return str(data[i].record)
        return ""

    def top(target):
        if target == "0" or len(data) == 0:
            return ""
        target = int(target)
        d = {}
        for i in data:
            d[data[i].name] =  data[i].record
        dd = dict(sorted(d.items(), key=lambda item: (-item[1], item[0])))
        res = []
        for i in d:
            if target > 0:
                target -= 1
                item = ""
                item += str(i) + "(" + str(d[i]) + ")"
                res.append(item)
        res.reverse()
        s = ""
        for i in range(len(res)-1):
            s += res[i] + ", "
        s += res[-1]
        return s
    
    def transfer(a, b, amount):
        if a == b:
            return "false"
        
        aid = -1
        bid = -1
        amount = int(amount)

        for i in data:
            if data[i].name == a:
                if data[i].amount < amount:
                    
                    return "false"
                aid = i
            if data[i].name == b:
                bid = i
        
        if aid == -1 or bid == -1:
            return "false"
        data[aid].amount -= amount
        data[bid].amount += amount

        return "true"

    for query in queries:
        print(query[0], data)
        
        if query[0] == "CREATE":
            value = query[1]
            if len(query) == 3:
                res.append(create(value, query[2]))
            else:
                res.append(create(value, "0"))
        if query[0] == "GET":
            value = query[1]
            res.append(get(value))
        if query[0] == "DELETE":
            value = query[1]
            res.append(delete(value))   
        if query[0] == "RECORD":
            value = query[1]
            amount = query[2]
            res.append(record(value, amount))
        if query[0] == "TOP":
            value = query[1]
            res.append(top(value))
        if query[0] == "TRANSFER":
            a = query[1]
            b = query[2]
            amount = query[3]
            res.append(transfer(a,b,amount))


    return res




