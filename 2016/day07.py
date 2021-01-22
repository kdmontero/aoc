with open('day07.txt') as f:
    ip_addrs = f.read().splitlines()

# part 1
ip_tls = 0
for ip in ip_addrs:
    inside_hypernet = False
    support_tls = False
    for i in range(1, len(ip)-2):
        if ip[i] == '[':
            inside_hypernet = True 
            continue
        elif ip[i] == ']':
            inside_hypernet = False
            continue

        if ip[i] == ip[i+1] and ip[i-1] == ip[i+2] and ip[i] != ip[i-1]:
            if inside_hypernet:
                break
            else:
                support_tls = True

    else:
        if support_tls:
            ip_tls += 1

print(f'Part 1: {ip_tls}') # 110


# part 2
ip_ssl = 0
for ip in ip_addrs:
    inside_hypernet = False
    aba = set()
    bab = set()
    for i in range(1, len(ip)-1):
        if ip[i] == '[':
            inside_hypernet = True
            continue
        elif ip[i] == ']':
            inside_hypernet = False
            continue

        if ip[i-1] == ip[i+1]:
            a, b = ip[i-1], ip[i]
            if inside_hypernet:
                bab.add(ip[i-1:i+2])
                if b + a + b in aba:
                    break
            else:
                aba.add(ip[i-1:i+2])
                if b + a + b in bab:
                    break
    
    else:
        continue
    ip_ssl += 1

print(f'Part 2: {ip_ssl}') # 242 
