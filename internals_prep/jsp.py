from sympy.logic.boolalg import to_cnf
from sympy import symbols
from sympy.logic.inference import satisfiable

P,Q,R = symbols('P Q R')

kb = ((~P | Q) & (~Q| R) & P)

query = R

cnf_formula = to_cnf(kb & ~query, simplify = True)
result = satisfiable(cnf_formula)

if not result:
    print("Query is entailed by KB (prived by Resulation)")

else:
    print("Query is NOT entailed")