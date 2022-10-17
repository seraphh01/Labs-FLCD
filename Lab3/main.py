from Lab3.symbol_table import SymbolTable


st = SymbolTable(100)
pos1 = st.add_identifier("salut")
get_pos1 = st.find_identifier("salut")

print(pos1, get_pos1, st.get_identifier(*pos1))

pos2 = st.add_int_constant(20)
get_pos2 = st.find_int_constant(20)
print(pos2, get_pos2, st.get_int_constant(*pos2))

pos3 = st.add_string_constant("hello")
get_pos3 = st.find_string_constant("hello")
print(pos3, get_pos3, st.get_string_constant(*pos3))


print(st.get_identifier(10, 0))
