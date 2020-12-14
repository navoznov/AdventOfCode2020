
import re

input = open('Day14\input.txt').read()

def parse_mask(str):
    _, mask = str.split(' = ')
    return mask


def parse_instraction(str):
    memoryAddressStr, valueStr = str.split(' = ')
    return (int(memoryAddressStr[4:-1]), int(valueStr))


# part 1
def apply_mask1(value, mask):
    binary_value_str = list(str(bin(value))[2:].zfill(len(mask)))
    for i in range(len(mask)):
        if mask[i] == 'X':
            continue
        binary_value_str[i] = mask[i]

    return "".join(binary_value_str)


def run1(input):
    memory = {}
    lines = input.split('\n')
    i = 0
    mask = None
    for line in lines:
        if line.startswith("mask"):
            mask = parse_mask(line)
        else:
            address, value = parse_instraction(line)
            masked_value_str = apply_mask1(value, mask)
            masked_value = int(masked_value_str, 2)
            memory[address] = masked_value

    return sum(memory.values())


print(run1(input))


# part 2
def apply_mask2(value, mask):
    binary_value_str = list(str(bin(value))[2:].zfill(len(mask)))
    floating_ount = len([x for x in mask if x == 'X'])
    for i in range(len(mask)):
        if mask[i] == '0':
            continue

        binary_value_str[i] = mask[i]

    return "".join(binary_value_str)


def get_mask_variants(mask, x_index):
    binarya_alphabet = ['0', '1']
    char_list = list(mask)
    result = []
    for x in binarya_alphabet:
        char_list = list(mask)
        char_list[x_index] = x
        result.append("".join(char_list))

    return result


def get_binary_addresses(masked_address):
    x_index = masked_address.find('X')
    if x_index == -1:
        return [masked_address]

    result = []
    for x in get_mask_variants(masked_address, x_index):
        result = result + get_binary_addresses(x)
    return result


def run2(input):
    memory = {}
    lines = input.split('\n')
    i = 0
    mask = None
    for line in lines:
        if line.startswith("mask"):
            mask = parse_mask(line)
        else:
            address, value = parse_instraction(line)
            masked_address_str = apply_mask2(address, mask)
            addresses = [int(x, 2)
                         for x in get_binary_addresses(masked_address_str)]
            for address in addresses:
                memory[address] = value

    return sum(memory.values())


print(run2(input))
