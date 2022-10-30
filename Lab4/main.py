from Lab4.scanner import Scanner
import tokenize

file_name = "p1.txt"
f = open(file_name, "r")
program = f.read()
with open(file_name, "r") as f:
    tokens = [t.string for t in tokenize.generate_tokens(f.readline) if t.string != '']
valid_tokens = open("token.in", "r").read().strip().split()

#tokens = [i.strip() for i in re.split(r'(\d+|\W+|)', program.strip()) if i != '' and i.isspace() is False]

s = Scanner(program, tokens, valid_tokens)
s.scan()

pif_file = open(f"{file_name}_PIF.out", "w+")
pif = "".join([str(p) + '\n' for p in s.pif])
pif_file.write(pif)

st_file = open(f"{file_name}_ST.out", "w+")
st_file.write("IDENTIFIERS: \n")
st_file.write(s.symbol_table.identifier_hash_table.__str__() + '\n')
st_file.write("INT CONSTANTS: \n")
st_file.write(s.symbol_table.int_constants_hash_table.__str__() + '\n')
st_file.write("STRING CONSTANTS: \n")
st_file.write(s.symbol_table.string_constants_hash_table.__str__())
print("lexically correct")
