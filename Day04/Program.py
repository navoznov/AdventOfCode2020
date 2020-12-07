import re
lines = open('Day04\input.txt').read().split('\n')

def parsePassports(lines):
    results = []
    passport = {}
    for i, line in enumerate(lines):
        if line == '':
            results.append(passport)
            passport = {}
            continue

        pairs = [pair.split(':') for pair in line.split(' ')]
        passport.update(pairs)

    results.append(passport)
    return results

# part 1
def validatePassport1(passport):
    requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    passportFields = [k for k in passport.keys()]
    missedFields = [x for x in requiredFields if x not in passportFields]
    return len(missedFields) == 0

passports = parsePassports(lines)
validPassports = [x for x in passports if validatePassport1(x)]
print(len(validPassports))

# part 2
def validatePassport2(passport):
    requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    passportFields = passport.keys()
    missedFields = [x for x in requiredFields if x not in passportFields]
    if len(missedFields) > 0:
        return False

    rangeRules = {'byr': (1920, 2002), 'iyr': (2010, 2020), 'eyr': (2020, 2030)}
    passedRules = [field for field, (min, max) in rangeRules.items() if min <= int(passport[field]) <= max]
    if len(passedRules) != len(rangeRules):
        return False

    height = passport['hgt']
    if len(height) < 3:
        return False
    heightRules = {'in': (59, 76), 'cm': (150, 193)}
    minHeight, maxHeight = heightRules[height[-2:]]
    heightValue = int(height[:-2])
    if  heightValue > maxHeight or heightValue < minHeight:
        return False

    if re.match(r'^#[\da-f]{6}$', passport['hcl']) == None:
        return False

    validEyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if not passport['ecl'] in validEyeColors:
        return False

    if re.match(r'^[\d]{9}$', passport['pid']) == None:
        return False

    return True


validPassports = [x for x in passports if validatePassport2(x)]
print(len(validPassports))
