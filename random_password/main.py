import secrets
import string
import argparse

# pwd_length = 12
DEFAULT_LENGTH = 16

parser = argparse.ArgumentParser()
parser.add_argument('--length')
parser.add_argument('--letters-only', action='store_true')
parser.add_argument('--numbers-only')
parser.add_argument('--letters-and-numbers-only')
args = parser.parse_args()

special_chars = '.!@#$%*+'
digits = string.digits

def generate_alphabet() -> str:
  letters = string.ascii_letters
  if args.letters_only:
     return letters
  
  digits = string.digits
  if args.numbers_only:
     return digits
  
  if args.letters_and_numbers_only:
     return digits + letters
  special_chars = '.!@#$%*+'
  alphabet = letters + digits + special_chars
  return alphabet

def generate_length():
   if args.length:
      return int(args.length)
   return DEFAULT_LENGTH

def main():
  alphabet = generate_alphabet()
  pwd_length = generate_length()
  while True:
    pwd = ''
    for i in range(pwd_length):
      pwd += ''.join(secrets.choice(alphabet))

    if (any(char in special_chars for char in pwd) and 
        sum(char in digits for char in pwd)>=2):
            break
  return pwd






