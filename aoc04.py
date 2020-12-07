import re

with open("./aoc04.txt") as file:
    input = list(file.read().splitlines())


class PasswordValidator:
    passports = []
    passport_data = []
    valid_passwords = 0
    valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def __init__(self, input):
        self.input = input

    def get_data(self):
        passport_data = []
        for line in self.input:
            if line == "":
                self.passports.append(passport_data)
                passport_data = []
            else:
                passport_data.append(line)
        self.passports.append(passport_data)

    def check_passports(self):
        self.get_data()
        self.valid_passwords = 0

        for passport in self.passports:
            if self.is_valid_password_improved(passport):
                self.valid_passwords += 1

        print("Total: ", len(self.passports))
        print("Valid passports: ", self.valid_passwords)

    def is_valid_password(self):
        fields = " ".join(self.passport_data)
        f = fields.split(" ")
        if len(f) == 8:
            self.valid_passwords += 1
        elif len(f) == 7 and not re.search(r'cid\:', fields):
            self.valid_passwords += 1

    def is_valid_password_improved(self, passport):
        fields = " ".join(passport)
        f = fields.split(" ")

        reason = ""

        valid_fields = 0
        cid_present = False
        for d in f:
            key, value = d.split(':')
            if key == 'byr' and 1920 <= int(value) <= 2002:
                valid_fields += 1
            elif key == 'iyr' and 2010 <= int(value) <= 2020:
                valid_fields += 1
            elif key == 'eyr' and 2020 <= int(value) <= 2030:
                valid_fields += 1
            elif key == 'hgt':
                if value[-2:] == 'cm' and 150 <= int(value[:-2]) <= 193:
                    valid_fields += 1
                elif value[-2:] == 'in' and 59 <= int(value[:-2]) <= 76:
                    valid_fields += 1
            elif key == 'hcl':
                if value[:1] == '#' and len(value) == 7 and re.match(r"^([\da-f]+)$", value[1:]):
                    valid_fields += 1
            elif key == 'ecl' and value in self.valid_ecl:
                valid_fields += 1
            elif key == 'pid' and len(value) == 9 and re.match(r"(\d+)$", value):
                valid_fields += 1
            elif key == 'cid':
                valid_fields += 1
                cid_present = True
            else:
                reason = key

        if valid_fields == 8 or (valid_fields == 7 and not cid_present):
            return True
        # else:
        #     if not reason:
        #         reason = 'cid' if not cid_present else 'FLD'
        #     print("N", len(f), reason, fields)


validator = PasswordValidator(input)

validator.check_passports()

