import subprocess
def info(y):
    subprocess.call("cls", shell=True)
    y = input("Вам необходимо ввести ЦЕЛОЕ число от -бесконечности до +бесконечности, \nиначе бан или ошибки, в любом случае программно всё округлится,\nно вместе с этим может округлиться ̶в̶а̶ш̶ ̶е̶б̶а̶л̶ь̶н̶и̶к̶  ваше лицо.\n\nВы всё поняли???  (Д/н): ")
    return y
def helper(z):
    k = 0
    while z != 'y' and z != 'д' and z != 'Y' and z != 'Д':
        z = info(z)
        k += 1
        if k >= 13:
            subprocess.call("cls", shell=True)
            input("ЯСНО, АВТОРУ 0 ЛЕТ...")
            exit(1)
    if z == 'y' or z == 'д' or z == 'Y' or z == 'Д':
        subprocess.call("cls", shell=True)