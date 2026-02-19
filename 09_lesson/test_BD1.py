import pytest
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String
)
from sqlalchemy.orm import sessionmaker, declarative_base

# Константы
DATABASE_URL = (
    "postgresql://postgres:241012@"
    "localhost:5432/databaseSky"
)

# Базовые настройки
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
    """Фиксатура для создания сессии и очистки только созданных в тесте данных."""
    session = SessionLocal()
    created_ids = []  # Список для хранения ID созданных записей
    
    # Сохраняем оригинальный метод add
    original_add = session.add
    
    def tracked_add(instance):
        """Обёртка для отслеживания добавленных записей."""
        original_add(instance)
        # Если у объекта есть ID (и он уже сохранён в БД), добавляем его в список
        if instance.id is not None:
            created_ids.append(instance.id)
    
    # Подменяем метод add на отслеживающий
    session.add = tracked_add
    
    yield session
    
    # Очистка: удаляем только созданные в этом тесте записи
    if created_ids:
        session.query(Student).filter(Student.id.in_(created_ids)).delete(synchronize_session=False)
        session.commit()
    
    session.close()

# Тесты (остаются без изменений)
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
    # Сначала создаём студента
    student = Student(name="Пётр Петров", age=22)
    db_session.add(student)
    db_session.commit()

    # Изменяем возраст
    student.age = 23
    db_session.commit()

    updated_student = db_session.query(Student).filter_by(name="Пётр Петров").first()
    assert updated_student.age == 23

def test_delete_student(db_session):
    """Тест на удаление."""
    # Сначала создаём студента
    student = Student(name="Сидор Сидоров", age=19)
    db_session.add(student)
    db_session.commit()

    # Удаляем студента
    db_session.delete(student)
    db_session.commit()

    deleted_student = db_session.query(Student).filter_by(name="Сидор Сидоров").first()
    assert deleted_student is None
