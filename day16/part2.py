bit_dict = {
    '0' :'0000',
    '1' :'0001',
    '2' :'0010',
    '3' :'0011',
    '4' :'0100',
    '5' :'0101',
    '6' :'0110',
    '7' :'0111',
    '8' :'1000',
    '9' :'1001',
    'A' :'1010',
    'B' :'1011',
    'C' :'1100',
    'D' :'1101',
    'E' :'1110',
    'F' :'1111',
}

def get_next_total( subs, type_id):
    if type_id == "000":
        return sum(subs)
    elif type_id == "001":
        total = 1
        for sub in subs:
            total *= sub
        return total
    elif type_id == "010":
        return min(subs)
    elif type_id == "011":
        return max(subs)
    elif type_id == "101":
        return int(subs[0] > subs[1])
    elif type_id == "110":
        return int(subs[0] < subs[1])
    elif type_id == "111":
        return int(subs[0] == subs[1])
        


def analyze_packet(packet, i=0):
    if len(packet) <= i+6:
        return 0, i +6
    total = 0
    type_id = packet[i+3:i+6]
    literal = ""
    i += 6

    if type_id == "100":
        while len(packet) > i:
            subpacket = packet[i:i+5]
            literal += subpacket[1:]
            if subpacket[0] == "0":
                return int(literal,2), i + 5
            i += 5
    else:
        len_type = packet[i:i+1]
        i += 1
        subs = []
        if len_type == "0":
            str_length = packet[i:i+15]
            i +=15
            length = int(str_length, 2) + i
            if(len(packet) < length):
                print('huh', length)
                # return total, i
            while i < length and i < len(packet):
                n_v, n_i = analyze_packet(packet, i)
                subs.append(n_v)
                i = n_i
        elif len_type == "1":
            iterations = int(packet[i:i+11], 2)
            i += 11
            while iterations > 0:
                n_v, n_i = analyze_packet(packet, i)
                subs.append(n_v)
                i = n_i
                iterations -= 1
        total += get_next_total( subs, type_id)
    return total, i

def main():
    with open("input.txt") as f:
        input = f.read().strip()
    man_bin = ""
    for char in input:
        man_bin += bit_dict[char]

    version, _ = analyze_packet(man_bin)
    print(version)


if __name__ == "__main__":
    main()
