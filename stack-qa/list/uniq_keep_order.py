
def uniq(input):
    # order preserving
    # O(n^2)
    output = []
    for i in input:
        if i not in output:
            output.append(i)

    return output

def uniq_q(seq):
    # order preserving
    # O(n^2)
    seen = set()
    seen_add = seen.add
    return [x for x in seq if x not in seen and not seen_add(x)]

def uniq_3(seq):
    # not order preserving
    # O(n)
    keys = {}
    for e in seq:
        keys[e] = 1
    return keys.keys()

def uniq_4(seq):
    # not order preserving
    # O(n)
    Set =  set(seq)
    return list(Set)

def uniq_5(seq):
    # order preserving
    # O(n^2)
    output = []
    [output.append(i) for i in seq if not output.count(i)]
    return output

def uniq_6(seq):
    # order preserving
    # Best way
    # O(n)
    seen = {}
    output = []
    for item in seq:
        if item in seen: continue
        seen[item] = 1
        output.append(item)
    return output


old_list = [10, 1, 2, 3, 3, 4, 5, 6, 3, 6, 9]

print uniq_q(old_list)
print uniq(old_list)
print uniq_3(old_list)
print uniq_4(old_list)
print uniq_5(old_list)
print uniq_6(old_list)

