import datetime as dt
from typing import Optional

from .models import Task, CheckMark
from src import db


def get_tasks(date):
    if date:
        date = dt.datetime.strptime(date, '%Y-%m-%d').date()

    tasks = Task.query.filter_by(date=date).all()

    tasks = [t.to_dict() for t in tasks]

    for t in tasks:
        t['check_marks'] = list(
            filter(
                lambda cm: cm['parent_id'] is None, t['check_marks']
            )
        )

    return tasks


def create_task(title, date):
    date = dt.datetime.strptime(date, '%Y-%m-%d')
    new_task = Task(title=title, date=date)
    db.session.add(new_task)
    db.session.commit()
    return new_task


def delete_task(id):
    Task.query.filter_by(id=id).delete()
    db.session.commit()


def create_check_mark(text: str, task_id: int, parent_id: Optional[int] = None):
    if parent_id:
        parent = CheckMark.query.get({"id": parent_id})
        if parent:
            task_id = parent.task_id
        else:
            parent_id = None

    new_check_mark = CheckMark(text=text, task_id=task_id,
                               parent_id=parent_id)
    db.session.add(new_check_mark)
    db.session.commit()
    return new_check_mark


def delete_check_mark(id):
    CheckMark.query.filter_by(id=id).delete()
    db.session.commit()
