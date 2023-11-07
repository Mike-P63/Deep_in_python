import subprocess

tst = "/home/user/tst"
out = "/home/user/out"
folder1 = "/home/user/folder1"


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, endcoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False
    
def test_step1():
    result1 = checkout("cd /home/user/tst; 7z a ../out/arx2", "Everything is Ok") 
    result2 = checkout("cd /home/user/out; ls", "arx2.7z")
    assert result1 and result2, 'test2 FAIL'

def test_step2():
    result1 = checkout("cd /home/user/out; 7z e arx2.7z -o/home/user/folder1 -y", "Everything is Ok")
    result2 = checkout("cd /home/user/folder1; ls", "qwe")
    result3 = checkout("cd /home/user/folder1; ls", "rty")
    assert result1 and result2 and result3 

def test_step3():
    assert checkout("cd /home/user/out; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"

def test_step4():
    assert checkout("cd /home/user/tst; 7z u ../out/arx2.7z", "Everything is Ok"), "test4 FAIL"

def test_step5():
    assert checkout("cd /home/user/out; 7z d arx2.7z", "Everything is Ok"), "test5 FAIL"