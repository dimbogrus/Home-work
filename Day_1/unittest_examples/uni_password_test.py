import unittest

import Day_1.Practice.strong_password as strong_password


class TestPassword(unittest.TestCase):
    def test_check_password(self):
        check, msg = strong_password.check_password("123456")
        self.assertFalse(check)
        self.assertRegex(msg, 'не')

    def test_check_password_one(self):
        check, msg = strong_password.check_password("123456478!")
        self.assertTrue(check)

    def test_check_password_two(self):
        check, msg = strong_password.check_password("saucacAusacu8")
        self.assertTrue(check)

    def test_check_password_three(self):
        check, msg = strong_password.check_password("o58anuahaunH!")
        self.assertTrue(check)
        self.assertRegex(msg, 'Пароль введен корректно')


if __name__ == "__main__":
    unittest.main(verbosity=2)
