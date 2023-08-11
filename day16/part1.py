def analyze_packet(packet, i=0):
    if len(packet) <= i+6:
        return 0, i +6
    version = int(packet[i:i+3], 2)
    type_id = packet[i+3:i+6]
    i += 6
    if type_id == "100":
        while len(packet) > i:
            subpacket = packet[i:i+5]
            if subpacket[0] == "0":
                return version, i + 5
            i += 5
    else:
        len_type = packet[i:i+1]
        i += 1
        if len_type == "0":
            str_length = packet[i:i+15]
            i +=15
            length = int(str_length, 2) + i
            if(len(packet) < length):
                print('huh')
                return version, i
            while i < length:
                n_v, n_i = analyze_packet(packet, i)
                version += n_v
                i = n_i
        elif len_type == "1":
            iterations = int(packet[i:i+11], 2)
            i += 11
            while iterations > 0:
                n_v, n_i= analyze_packet(packet, i)
                version += n_v
                i = n_i
                iterations -= 1
    return version, i

def main():
    with open("input.txt") as f:
        input = f.read().strip()
    str_bin =str(bin(int(input, 16)))[2:]
    version, _ = analyze_packet(str_bin)
    print(version)


if __name__ == "__main__":
    main()
