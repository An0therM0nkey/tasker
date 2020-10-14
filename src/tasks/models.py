from sqlalchemy_serializer import SerializerMixin

from src import db


class Task(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    content = db.Column(db.String(512))
    date = db.Column(db.Date, nullable=False)


class CheckMark(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(256))
    checked = db.Column(db.Boolean, default=False)

    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    task = db.relationship('Task', backref=db.backref('check_marks', lazy=False))

    parent_id = db.Column(db.Integer, db.ForeignKey('check_mark.id'), nullable=True)
    parent = db.relationship('CheckMark', remote_side=[id], backref=db.backref('children', lazy=True))

    serialize_rules = ('-task', '-parent')
