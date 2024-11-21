import os
import shutil

print("WARNING: TERMUX & LINUX ENVIRONTMENT ONLY")


def check_termux():
    if os.path.exists("/data/data/com.termux/"):
        return True
    else:
        return False


choose = input("Please Choose Number:\n1. Copy\n2. Symbolic Link\n> ") or None
st = os.stat("./PySCli.py")
os.chmod("./PySCli.py", st.st_mode | 0o111)

if choose is None or choose not in ["1", "2"]:
    print("Please choose correctly")
    exit()
elif choose == "1":
    if check_termux():
        shutil.copy("PySCli.py", "/data/data/com.termux/files/usr/bin/PySCli")
    else:
        shutil.copy("PySCli.py", "/usr/bin/PySCli")
elif choose == "2":
    if check_termux():
        os.symlink(
            os.getcwd() + "/PySCli.py", "/data/data/com.termux/files/usr/bin/PySCli"
        )
    else:
        shutil.copy(os.getcwd() + "/PySCli.py", "/usr/bin/PySCli")

print("Done!")
