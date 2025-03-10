from database import SessionFactory


def get_session():
    session = SessionFactory()

    try:
        yield session
    except Exception as exc:
        session.rollback()
        raise exc
    finally:
        session.close()
