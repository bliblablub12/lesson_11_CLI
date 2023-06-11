import argparse

poem_file = open('raven.txt', encoding='utf-8')
content = poem_file.read()


#vymena pisma za cislo
parser = argparse.ArgumentParser (description='budeme delat zmeny v basni.')
parser.add_argument("-i", "--input_file", type=str, help="input file", required=True)
parser.add_argument("-v", "--vymena", help="replaces chosen letter with given number")
parser.add_argument("-c", "--number", type=int, help="the number you wish to be in the text", required=True)
parser.add_argument("-l", "--letter", type=str, help="the letter you wish to be replaced", required=True)
args = parser.parse_args()

input_file = args.input_file
vymena = args.vymena
number = args.number
letter = args.letter

def vymena(content, pismo, cislo):
    with open('raven.txt', encoding='utf-8') as poem_file:
        basen = poem_file.read()
        nova_basen = basen.replace(pismo, str(cislo))
        return nova_basen

print(vymena(content, letter, number))



# rozklad_kapitalky(poem_file) -------CLI

parser = argparse.ArgumentParser (description='budeme delat zmeny v basni.')
parser.add_argument("-i", "--input_file", type=str, help="input file", required=True)
parser.add_argument("-r", "--rozklad", help="split poem into words and capitalize each word")
args = parser.parse_args()

input_file = args.input_file
rozklad = args.rozklad


def rozklad_kapitalky(input_file, rozklad):  #rozdelit
    with open(input_file, 'r',encoding='utf-8') as file:
        content = file.read()
    for slova in content.split():
        print(slova.upper(), end='\n')

if __name__ == "__main__":
    rozklad_kapitalky(input_file, rozklad)

