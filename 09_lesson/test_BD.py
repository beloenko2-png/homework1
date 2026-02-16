import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:241012@localhost:5432/databaseSky"

Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Описание модели
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)

# Создание таблицы 
Base.metadata.create_all(bind=engine)

@pytest.fixture
def db_session():
    """Фиксатура для создания сессии и автоматической очистки данных."""
    session = SessionLocal()
    yield session
    # Очистка: удаляем всех студентов, созданных во время тестов
    session.query(Student).delete()
    session.commit()
    session.close()

# --- Тесты ---

def test_add_student(db_session):
    """Тест на добавление."""
    new_student = Student(name="Иван Иванов", age=20)
    db_session.add(new_student)
    db_session.commit()

    student_in_db = db_session.query(Student).filter_by(name="Иван Иванов").first()
    assert student_in_db is not None
    assert student_in_db.age == 20

def test_update_student(db_session):
    """Тест на изменение."""
    # Сначала создаем студента
    student = Student(name="Петр Петров", age=22)
    db_session.add(student)
    db_session.commit()

    # Изменяем возраст
    student.age = 23
    db_session.commit()

    updated_student = db_session.query(Student).filter_by(name="Петр Петров").first()
    assert updated_student.age == 23

def test_delete_student(db_session):
    """Тест на удаление."""
    # Сначала создаем студента
    student = Student(name="Сидор Сидоров", age=19)
    db_session.add(student)
    db_session.commit()

    # Удаляем студента
    db_session.delete(student)
    db_session.commit()

    deleted_student = db_session.query(Student).filter_by(name="Сидор Сидоров").first()
    assert deleted_student is None
