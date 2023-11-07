import subprocess


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, srderr=subprocess.PIPE, endcoding='utf-8')
    if (text in result.stdout or text in result.stderr) and result.returncode !=0:
        return True
    else:
        return False
    

def test_step1():
    result1 = checkout("cd /home/user/out; 7z e bad_arx.7z -o/home/user/folder1 -y", "ERRORS")
    assert result1, "test1 FAIL"

def test_step2():
    assert checkout("cd /home/user/out; 7z t arx2.7z", "Everything is Ok"), "test2 FAIL"

