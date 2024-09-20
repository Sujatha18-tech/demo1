def logincheck(uname,pwd):
    if uname=='admin' and pwd=='admin123':
        return 'success'
    if uname!='admin' and pwd=='admin123':
        return 'uname fail'
import unittest
class logincheck(unittest,TestCase):
    def test1(self):
        result=logincheck('admin','admin123')
        self.assertEqual(result,'admin123')
    def test2(self):
        result=logincheck('admin123','admin123')
        self.assertEqual(result,'uname fail')
if __name__ == '__main__':
    unittest.main()
