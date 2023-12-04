
import sys

hex_table = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

PACKETS = []

def hex_to_bin(h):
    
    b = ""

    for n in h:
        b += hex_table[n]

    return b

def bin_to_dec(b):

    n = 0

    for i, c in enumerate(reversed(b)):
        
        n += (int(c) * pow(2, i))

    return n

def parse_packet(num, start, packet_limit, operator=None):

    end = start

    packets_found = []

    while end < len(num):

        packet = num[end::]

        if packet == (len(packet) * "0"): return

        version = bin_to_dec(packet[0:3])

        type_ID = bin_to_dec(packet[3:6])

        new_packet = None

        if type_ID == 4:

            (value, end) = parse_literal(packet[6::])

            new_packet = Packet(packet[0:6 + end], value)

        else:

            (new_packet, end) = parse_operator(packet)

        PACKETS.append(new_packet)
            
        if operator:
            operator.add_child(new_packet)
        
        packets_found.append(new_packet)

        if len(packets_found) >= packet_limit: 
            return packets_found
        
        num = packet[6::]

def parse_literal(packet):

    i = 0

    n = ""

    while True:

        over = packet[i]

        n += packet[i + 1:i + 5]

        i += 5

        if over == "0": break

    return (n, i)

def parse_operator(p):

    packet = p[6::]

    length_type_ID = packet[0]

    i = 0

    new_packet = None

    if length_type_ID == "0":

        sub_length = bin_to_dec(packet[1:16])

        new_packet = Packet(p[:3] + p[3:6] + packet[:1 + 15 + sub_length], packet[:1 + 15+ sub_length])

        parse_packet(packet[16:16 + sub_length], 0, sys.maxsize, new_packet)

        i = 1 + 15 + sub_length

    else:

        sub_count = bin_to_dec(packet[1:12])

        packets_found = parse_packet(packet[12::], 0, sub_count)

        operator_length = 0

        for el in packets_found:
            operator_length += el.length

        new_packet = Packet(p[:3] + p[3:6] + packet[:1 + 11 + operator_length], packet[:1 + 11 + operator_length])

        for el in packets_found:
            new_packet.add_child(el)

        i = 1 + 11 + operator_length
    
    return (new_packet, i)

def sum_versions(packets):

    s = 0

    for packet in packets:

        s += packet.version

    return s

def print_packets(packets):

    for packet in packets:
        print(packet)

def main():

    data = ""

    with open(sys.argv[1]) as f:
        data = f.readline().strip()

    b = hex_to_bin(data)

    print("HEX: {} | BIN: {}\n".format(data, b))

    parse_packet(b, 0, sys.maxsize)

    # print_packets(PACKETS)
    print("Sum of versions: {}".format(sum_versions(PACKETS)))

    print("Expression result: {}".format(PACKETS[-1].solve()))

################################################

class Packet:

    def __init__(self, packet, value):
        
        self.packet = packet
        self.length = len(self.packet)

        self.value = value

        self.version = bin_to_dec(self.packet[0:3])
        self.type_ID = bin_to_dec(self.packet[3:6])

        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_type(self):
        return "Literal" if self.type_ID == 4 else "Operator"

    def solve(self):

        val = 0

        match self.type_ID:
            case 0:
                for packet in self.children: val += packet.solve()
            case 1:
                val = 1
                for packet in self.children: val *= packet.solve()
            case 2:
                sp = [packet.solve() for packet in self.children]
                val = min(sp)
            case 3:
                sp = [packet.solve() for packet in self.children]
                val = max(sp)
            case 4:
                return bin_to_dec(self.value)
            case 5:
                val = 1 if self.children[0].solve() > self.children[1].solve() else 0
            case 6:
                val = 1 if self.children[0].solve() < self.children[1].solve() else 0
            case 7:
                val = 1 if self.children[0].solve() == self.children[1].solve() else 0

        return val

    def __str__(self):
        return "{}: {}{}, subpackets: {}".format(self.get_type(), self.packet, " -> {}".format(bin_to_dec(self.value)) if self.type_ID == 4 else "", [str(p) for p in self.children])

if __name__ == "__main__":
    main()