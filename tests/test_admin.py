import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.models import Base, User
from app.database import get_db
from app.auth import get_password_hash

# Test database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="function")
def test_db():
    # Create all tables
    Base.metadata.create_all(bind=engine)
    yield
    # Drop all tables after test
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def admin_user(test_db):
    db = next(override_get_db())
    # Create an admin user
    admin = User(
        email="admin@example.com",
        hashed_password=get_password_hash("adminpassword"),
        is_active=True,
        is_admin=True
    )
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin

@pytest.fixture(scope="function")
def regular_user(test_db):
    db = next(override_get_db())
    # Create a regular user
    user = User(
        email="user@example.com",
        hashed_password=get_password_hash("userpassword"),
        is_active=True,
        is_admin=False
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def test_admin_can_access_admin_endpoints(client, admin_user):
    # Login as admin
    response = client.post(
        "/auth/token",
        data={
            "username": admin_user.email,
            "password": "adminpassword"
        }
    )
    assert response.status_code == 200
    token = response.json()["access_token"]
    
    # Try to access admin endpoint
    response = client.get(
        "/auth/admin/users",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200

def test_regular_user_cannot_access_admin_endpoints(client, regular_user):
    # Login as regular user
    response = client.post(
        "/auth/token",
        data={
            "username": regular_user.email,
            "password": "userpassword"
        }
    )
    assert response.status_code == 200
    token = response.json()["access_token"]
    
    # Try to access admin endpoint
    response = client.get(
        "/auth/admin/users",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 403  # Forbidden

def test_admin_can_toggle_user_status(client, admin_user, regular_user):
    # Login as admin
    response = client.post(
        "/auth/token",
        data={
            "username": admin_user.email,
            "password": "adminpassword"
        }
    )
    assert response.status_code == 200
    token = response.json()["access_token"]
    
    # Toggle regular user's status
    response = client.put(
        f"/auth/admin/users/{regular_user.id}/toggle",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["is_active"] == False  # Status should be toggled

def test_regular_user_cannot_toggle_status(client, regular_user):
    # Login as regular user
    response = client.post(
        "/auth/token",
        data={
            "username": regular_user.email,
            "password": "userpassword"
        }
    )
    assert response.status_code == 200
    token = response.json()["access_token"]
    
    # Try to toggle another user's status
    response = client.put(
        f"/auth/admin/users/{regular_user.id}/toggle",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 403  # Forbidden 