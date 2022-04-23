import ctypes

shared_lib = ctypes.CDLL("./test_shared_lib.so")

shared_lib.ints.restype = ctypes.c_int
shared_lib.ints.argtypes = [ctypes.c_int, ctypes.c_int]

shared_lib.floats.restype = ctypes.c_float
shared_lib.floats.argtypes = [ctypes.c_float, ctypes.c_float]

shared_lib.doubles.restype = ctypes.c_double
shared_lib.doubles.argtypes = [ctypes.c_double, ctypes.c_double]

shared_lib.strings.restype = ctypes.c_char_p
shared_lib.strings.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char)]

test_ints = [3, 4]
test_doubles = [54321.45678, 1987654.09876543456787654]
test_strings = ["Bondarenko", "Stanislav"]

print(f"lib int result: {shared_lib.ints(test_ints[0], test_ints[1])}")
print(f"python result: {test_ints[0] + test_ints[1]}")
print()

print(f"lib float result: {shared_lib.floats(test_doubles[0], test_doubles[1])}")
print(f"lib double result: {shared_lib.doubles(test_doubles[0], test_doubles[1])}")
print(f"python result: {test_doubles[0] + test_doubles[1]}")
print()

print(f"lib string result: "
      f"{shared_lib.strings(test_strings[0].encode('utf8'), test_strings[1].encode('utf8')).decode('utf8')}")
print(f"python result: {test_strings[0] + test_strings[1]}")
