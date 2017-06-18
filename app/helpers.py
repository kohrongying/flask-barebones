from app import app, db

def save(resource):
    db.session.add(resource)

    try:
        db.session.commit()
        return True
    except Exception as e:
        app.logger.error('Error Saving to db :%s',(e))
        db.session.rollback()
        db.session.flush()
        return False

def delete(resource):
    db.session.delete(resource)

    try:
        db.session.commit()
        return True
    except Exception as e:
        app.logger.error('Error deleting from db :%s',(e))
        db.session.rollback()
        db.session.flush()
        return False