from sqlalchemy import create_engine
from sqlalchemy import text

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)


def test_db_connection():
    names = db.table_names()
    assert names[1] == 'employee'


def test_insert(db):
    sql = text("""
        INSERT INTO company(name, is_active,
                create_timestamp, change_timestamp)
        VALUES (:name, :is_active, now(), now())
        RETURNING id
    """)

    result = db.execute(sql, {"name": "Skypro", "is_active": True})
    company_id = result.scalar()
    db.commit()

    # cleanup
    db.execute(text("DELETE FROM company WHERE id = :id"), {"id": company_id})
    db.commit()


def test_update(db):
    insert_sql = text("""
        INSERT INTO company(name, is_active,
                       create_timestamp, change_timestamp)
        VALUES (:name, :is_active, now(), now())
        RETURNING id
    """)

    company_id = db.execute(insert_sql, {
        "name": "Old Name",
        "is_active": True
    }).scalar()
    db.commit()

    update_sql = text("""
        UPDATE company
        SET description = :descr
        WHERE id = :id
    """)

    db.execute(update_sql, {
        "descr": "New descr",
        "id": company_id
    })
    db.commit()

    # cleanup
    db.execute(text("DELETE FROM company WHERE id = :id"), {"id": company_id})
    db.commit()


def test_delete(db):
    company_id = db.execute(text("""
        INSERT INTO company(name, is_active,
                                  create_timestamp, change_timestamp)
        VALUES (:name, :is_active, now(), now())
        RETURNING id
    """), {
        "name": "To Delete",
        "is_active": True
    }).scalar()

    db.commit()

    db.execute(text("DELETE FROM company WHERE id = :id"), {"id": company_id})
    db.commit()

    deleted = db.execute(text(
        "SELECT id FROM company WHERE id = :id"), {"id": company_id}).first()

    assert deleted is None
