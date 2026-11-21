from collections import defaultdict

# Define the dictionary with a default value of list


def solution(queries):

    data = {}
    counts = {}
    results = []
    expiry = {}

    links = defaultdict(list)

    def set(room, value, timestamp = 0, ttl = -1):

        if ttl != -1:
            expiry[room] = timestamp + ttl

        if room not in counts:
            counts[room] = 1
        data[room] = value
        return ""

    def get(room):

        if room not in data:
            return ""
        return data[room]

    def delete(room):
        if room not in data:
            return "false"
        data.pop(room, None)
        counts.pop(room, None)
        links.pop(room, None)
        for i in links:
            if room in links[i]:
                links[i].remove(room)

        return "true"

    def record(room):
        if room not in data:
            return ""
        counts[room] += 1
        return str(counts[room])

    def top(n):
        if not counts or n == 0:
            return ""
        res = dict(sorted(counts.items(), key=lambda item: (-item[1], item[0])))
        s = ""
        t = 0
        for i in res.keys():
            if t < n:
                item = i + "(" + str(counts[i]) + "), "
                s += item
                t += 1
        return s[:-2]

    def link(a, b):

        if a not in data or b not in data or (a == b):
            return "false"
        
        if a in data and b in data and a in links[b] and b in links[a]:
            return "false"
        
        links[a].append(b)
        links[b].append(a)

        return "true"
    
    def get_links(a):

        if a not in data or not links[a]:
            return ""

        s = ""
        r = sorted(links[a])
        for i in r:
            s += i + ", "
        
        return s[:-2]

    for query in queries:
        
        if query[0] == "SET":
            room = query[1]
            value = query[2]
            results.append(set(room, value))

        if query[0] == "GET":
            room = query[1]
            results.append(get(room))

        if query[0] == "DELETE":
            room = query[1]
            results.append(delete(room))

        if query[0] == "RECORD":
            room = query[1]
            results.append(record(room))

        if query[0] == "TOP":
            n = int(query[1])
            results.append(top(n))

        if query[0] == "LINK":
            a = query[1]
            b = query[2]
            results.append(link(a,b))
        
        if query[0] == "LINKS":
            results.append(get_links(query[1]))

        if query[0] == "SET_AT":
            timestamp = int(query[1])
            room = query[2]
            value = query[3]
            if len(query) == 4:
                ttl = 9999999999999999
            else:
                ttl = int(query[4])
            results.append(set(room, value, timestamp, ttl))
        
        if query[0] == "GET_AT":
            timestamp = int(query[1])
            room = query[2]
            if room not in data or expiry[room] < timestamp:
                results.append("")
            else:
                results.append(get(room))









    return results
