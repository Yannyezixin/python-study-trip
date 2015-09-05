
def uniq(input):
    output = []
    for i in input:
        if i not in output:
            output.append(i)

    return output

def uniq_q(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if x not in seen and not seen_add(x)]


old_list = [1, 2, 3, 3, 4, 5, 6, 3]

print uniq_q(old_list)
print uniq(old_list)

