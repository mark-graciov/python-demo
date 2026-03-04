from app.core.security import verify_password, get_password_hash

def test_get_password_hash() -> None:
    # Given
    password = "testpassword"
    
    # When
    hashed_password = get_password_hash(password)
    
    # Then
    assert hashed_password != password
    assert verify_password(password, hashed_password)

def test_verify_password() -> None:
    # Given
    password = "testpassword"
    hashed_password = get_password_hash(password)
    
    # When / Then
    assert verify_password(password, hashed_password) is True
    assert verify_password("wrongpassword", hashed_password) is False
