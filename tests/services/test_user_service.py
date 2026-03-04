from sqlalchemy.orm import Session
from app.services import user_service
from app.schemas import UserCreate, UserUpdate
from app.core.security import verify_password

def test_create_user(db: Session) -> None:
    # Given
    email = "service_test@example.com"
    password = "password"
    user_in = UserCreate(email=email, password=password, full_name="Service Test User")
    
    # When
    user = user_service.create(db, obj_in=user_in)
    
    # Then
    assert user.email == email
    assert hasattr(user, "hashed_password")
    assert verify_password(password, user.hashed_password)

def test_get_user(db: Session) -> None:
    # Given
    email = "get_user@example.com"
    password = "password"
    user_in = UserCreate(email=email, password=password)
    user = user_service.create(db, obj_in=user_in)
    
    # When
    user_2 = user_service.get(db, id=user.id)
    
    # Then
    assert user_2
    assert user.email == user_2.email
    assert user.id == user_2.id

def test_get_user_by_email(db: Session) -> None:
    # Given
    email = "get_by_email@example.com"
    password = "password"
    user_in = UserCreate(email=email, password=password)
    user = user_service.create(db, obj_in=user_in)
    
    # When
    user_2 = user_service.get_by_email(db, email=email)
    
    # Then
    assert user_2
    assert user.email == user_2.email
    assert user.id == user_2.id

def test_update_user(db: Session) -> None:
    # Given
    email = "update_user@example.com"
    password = "password"
    user_in = UserCreate(email=email, password=password)
    user = user_service.create(db, obj_in=user_in)
    new_password = "newpassword"
    user_update = UserUpdate(password=new_password, full_name="Updated Name")
    
    # When
    user_2 = user_service.update(db, db_obj=user, obj_in=user_update)
    
    # Then
    assert user.id == user_2.id
    assert user_2.full_name == "Updated Name"
    assert verify_password(new_password, user_2.hashed_password)

def test_update_user_dict(db: Session) -> None:
    # Given
    email = "update_user_dict@example.com"
    password = "password"
    user_in = UserCreate(email=email, password=password)
    user = user_service.create(db, obj_in=user_in)
    update_data = {"full_name": "Updated via Dict"}
    
    # When
    user_2 = user_service.update(db, db_obj=user, obj_in=update_data)
    
    # Then
    assert user.id == user_2.id
    assert user_2.full_name == "Updated via Dict"

def test_delete_user(db: Session) -> None:
    # Given
    email = "delete_user@example.com"
    password = "password"
    user_in = UserCreate(email=email, password=password)
    user = user_service.create(db, obj_in=user_in)
    
    # When
    user_2 = user_service.delete(db, id=user.id)
    user_3 = user_service.get(db, id=user.id)
    
    # Then
    assert user_3 is None
    assert user_2.id == user.id

def test_get_multi_users(db: Session) -> None:
    # Given
    email_1 = "user1@example.com"
    email_2 = "user2@example.com"
    user_in_1 = UserCreate(email=email_1, password="password")
    user_in_2 = UserCreate(email=email_2, password="password")
    user_service.create(db, obj_in=user_in_1)
    user_service.create(db, obj_in=user_in_2)
    
    # When
    users = user_service.get_all(db)
    
    # Then
    assert len(users) >= 2
    emails = [u.email for u in users]
    assert email_1 in emails
    assert email_2 in emails
