from user_validation import UserValidation

class TestUserValidation:
    def test_validate_user_addition(self):
        uv = UserValidation()
        result = uv.validate_user(2, 3, 'Addition')
        assert result == 5

    def test_validate_user_division(self):
        uv = UserValidation()
        result = uv.validate_user(10, 2, 'Division')
        assert result == 5

    # Add more test cases for other operations and edge cases...
