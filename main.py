from z3 import *

types = Datatype('ast_types')
types.declare('i8')
types.declare('i16')
types.declare('i32')
types.declare('i64')
types.declare('u8')
types.declare('u16')
types.declare('u32')
types.declare('u64')
typeSort = types.create()

Integer = Function('Integer', typeSort, BoolSort())
Addable = Function('Addable', typeSort, typeSort, typeSort, BoolSort())
s = Solver()
x0 = Const("x0", typeSort)
s.add(
    ForAll([x0],
       Implies(
           Integer(x0),
           Or(
              x0 == typeSort.i8,
              x0 == typeSort.i16,
              x0 == typeSort.i32,
              x0 == typeSort.i64,
              x0 == typeSort.u8,
              x0 == typeSort.u16,
              x0 == typeSort.u32,
              x0 == typeSort.u64,
           )
       )
    )
)
s.add(Integer(typeSort.i8) == True)
s.add(Integer(typeSort.i16) == True)
s.add(Integer(typeSort.i32) == True)
s.add(Integer(typeSort.i64) == True)
s.add(Integer(typeSort.u8) == True)
s.add(Integer(typeSort.u16) == True)
s.add(Integer(typeSort.u32) == True)
s.add(Integer(typeSort.u64) == True)
x = Const("x", typeSort)
y = Const("y", typeSort)
z = Const("z", typeSort)
s.add(ForAll([x, y, z],
             Implies(
                 Addable(x, y, z),
                    Or(
                        And(x == typeSort.i8, y == typeSort.i8, z == typeSort.i8),
                        And(x == typeSort.i16, y == typeSort.i16, z == typeSort.i16),
                        And(x == typeSort.i32, y == typeSort.i32, z == typeSort.i32),
                        And(x == typeSort.i64, y == typeSort.i64, z == typeSort.i64),
                        And(x == typeSort.u8, y == typeSort.u8, z == typeSort.u8),
                        And(x == typeSort.u16, y == typeSort.u16,  z == typeSort.u16),
                        And(x == typeSort.u32, y == typeSort.u32, z == typeSort.u32),
                        And(x == typeSort.u64, y == typeSort.u64, z == typeSort.u64),
                    ))))
v0 = Const("$0", typeSort)
v1 = Const("$1", typeSort)
s.add(v0 == typeSort.u32)
s.add(Addable(typeSort.i32, v0, v1))
Integer(v0)

print(s.check())
print(s.model())
