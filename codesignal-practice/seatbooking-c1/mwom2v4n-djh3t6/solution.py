from dataclasses import dataclass

def solution(queries):

    @dataclass
    class Booking:
        seat: str
        amount: int = 0

    data = {}
    stack = []

    def create(seat, amount=0):
        if seat in data:
            return "false"
        data[seat] = Booking(seat, amount)
        stack.append(seat)
        return "true"

    def get(seat):
        if seat in data:
            stack.append(seat)
            return str(data[seat].amount)
        return ""

    def delete(seat):
        if seat not in data:
            return "false"
        data.pop(seat,None)
        return "true"

    def recent(n):
        if n == 0 or not stack:
            return ""

        if n == 1:
            return str(stack[-1])

        res = stack[::-1]
        s = ""
        for i in range(n-1):
            if i < len(stack) :
                s += res[i] + ", "
        if i < len(stack):
            s += res[i+1]
        
        if s[-1] == " ":
            return s[:-2]
        return s
        
    def transfer(a,b, amount):
        if (a not in data) or (b not in data) or (int(data[a].amount) < amount) or (a == b):
            return "false"
        
        data[a].amount -= int(amount)
        data[b].amount += int(amount)

        return "true"


    results = []
    for query in queries:

        if query[0] == "CREATE":
            seat=query[1]
            amount = 0
            if len(query) == 3:
                amount = int(query[2])
            results.append(create(seat, amount))
        
        if query[0] == "GET":
            seat=query[1]
            results.append(get(seat))

        if query[0] == "DELETE":
            seat=query[1]
            results.append(delete(seat))
        
        if query[0] == "RECENT":
            n=int(query[1])
            results.append(recent(n))
        
        if query[0] == "TRANSFER":
            a = query[1]
            b = query[2]
            amount = int(query[3])
            results.append(transfer(a,b,amount))

        pass
    return results
