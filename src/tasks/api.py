from flask_restful import Api, Resource, reqparse

from .services import get_tasks, create_task, delete_task, create_check_mark, delete_check_mark

api = Api()


class TaskAPI(Resource):
    def get(self, date=None):
        tasks = get_tasks(date)
        return tasks

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title')
        parser.add_argument('date')
        params = parser.parse_args()

        title = params['title']
        date = params['date']
        try:
            create_task(title, date)
            return 201
        except Exception as e:
            return {
                'error': str(e)
            }

    def delete(self, id):
        delete_task(id)
        return 200


class CheckMarkAPI(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text')
        parser.add_argument('task_id')
        parser.add_argument('parent_id')
        params = parser.parse_args()

        text = params.get('text')
        task_id = params.get('task_id')
        parent_id = params.get('parent_id')

        try:
            create_check_mark(text, task_id, parent_id)
            return 201
        except Exception as e:
            return {
                'error': str(e)
            }

    def delete(self, id):
        delete_check_mark(id)
        return 200


api.add_resource(TaskAPI, "/tasks", "/tasks/", "/tasks/<string:date>", "/tasks/<int:id>")
api.add_resource(CheckMarkAPI, "/check_marks", "/check_marks/", "/check_marks/<int:id>")
