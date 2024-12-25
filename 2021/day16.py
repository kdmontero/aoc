if __name__ == '__main__':
    print("Advent of Code 2021 - Day 16: Packet Decoder")
    
    with open('day16.txt') as f:
        given = f.readline()

    bits = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }
    
    bin_msg = ''
    for char in given:
        bin_msg += bits[char]

    total_version = 0

    def evaluate_inner_packet(packet: str) -> [int, int]:
        sub_packets = []
        if packet[6] == '0':
            length = int(packet[7:22], 2)

            i = 22
            while i < 22 + length:
                packet_value, end_index = evaluate_packet(packet[i:22+length])
                i += end_index
                sub_packets.append(packet_value)

            i = 22 + length

        elif packet[6] == '1':
            subpackets_qty = int(packet[7:18], 2)

            i = 18
            for _ in range(subpackets_qty):
                packet_value, end_index = evaluate_packet(packet[i:])
                i += end_index
                sub_packets.append(packet_value)

        return sub_packets, i

    def evaluate_packet(packet: str) -> [int, int]:
        global total_version 
        total_version += int(packet[0:3], 2)
        type_id = int(packet[3:6], 2)

        bin_value = ''
        if type_id == 4:
            for i in range(6, len(packet), 5):
                bin_value += packet[i+1:i+5]
                if packet[i] == '0':
                    end_index = i + 5 # start index of the next packet
                    return int(bin_value, 2), end_index

        else:
            sub_packets, i = evaluate_inner_packet(packet)
            if type_id == 0:
                return sum(sub_packets), i
            
            elif type_id == 1:
                product = 1
                for num in sub_packets:
                    product *= num
                return product, i

            elif type_id == 2:
                return min(sub_packets), i

            elif type_id == 3:
                return max(sub_packets), i

            elif type_id == 5:
                return int(sub_packets[0] > sub_packets[1]), i

            elif type_id == 6:
                return int(sub_packets[0] < sub_packets[1]), i

            elif type_id == 7:
                return int(sub_packets[0] == sub_packets[1]), i

    msg, _ = evaluate_packet(bin_msg)

    print(f'Part 1: {total_version}') # 889 - part 1

    print(f'Part 2: {msg}') # 739303923668 - part 2
