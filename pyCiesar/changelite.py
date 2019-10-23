import HELPlib
import subprocess
x = ''
HELPlib.helper(x)
k = int(input("Введите номер, в зависимости от сдвига, который вам необходим(+/-):\n>>> "))
subprocess.call("cls", shell=True)
k = int(k % 33)
if k == 1 or k == -32:
    from libRU1 import lb
elif k == 2 or k == -31:
    from libRU2 import lb
elif k == 3 or k == -30:
    from libRU3 import lb
elif k == 4 or k == -29:
    from libRU4 import lb
elif k == 5 or k == -28:
    from libRU5 import lb
elif k == 6 or k == -27:
    from libRU6 import lb
elif k == 7 or k == -26:
    from libRU7 import lb
elif k == 8 or k == -25:
    from libRU8 import lb
elif k == 9 or k == -24:
    from libRU9 import lb
elif k == 10 or k == -23:
    from libRU10 import lb
elif k == 11 or k == -22:
    from libRU11 import lb
elif k == 12 or k == -21:
    from libRU12 import lb
elif k == 13 or k == -20:
    from libRU13 import lb
elif k == 14 or k == -19:
    from libRU14 import lb
elif k == 15 or k == -18:
    from libRU15 import lb
elif k == 16 or k == -17:
    from libRU16 import lb
elif k == 17 or k == -16:
    from libRU17 import lb
elif k == 18 or k == -15:
    from libRU18 import lb
elif k == 19 or k == -14:
    from libRU19 import lb
elif k == 20 or k == -13:
    from libRU20 import lb
elif k == 21 or k == -12:
    from libRU21 import lb
elif k == 22 or k == -11:
    from libRU22 import lb
elif k == 23 or k == -10:
    from libRU23 import lb
elif k == 24 or k == -9:
    from libRU24 import lb
elif k == 25 or k == -8:
    from libRU25 import lb
elif k == 26 or k == -7:
    from libRU26 import lb
elif k == 27 or k == -6:
    from libRU27 import lb
elif k == 28 or k == -5:
    from libRU28 import lb
elif k == 29 or k == -4:
    from libRU29 import lb
elif k == 30 or k == -3:
    from libRU30 import lb
elif k == 31 or k == -2:
    from libRU31 import lb
elif k == 32 or k == -1:
    from libRU32 import lb
else:
    pass
a = input("Введите слово\n>>> ")
subprocess.call("cls", shell=True)
if k == 0:
    print(a)
    exit(0)
else:
    k = 0
    for i in a:
        a = lb(i,k,a)
        k += 1
print("Результат:\n>>> ", a)
input("Нажмите любую кнопку")