from operation.models.work_space import WorkSpace
from response.error_response import Error

class WorkSpaceService():
    def list_workspace(user_id):
        return WorkSpace.objects.filter(user=user_id)
    
    def create_work_space(data):
        try:
            work_space=WorkSpace.objects.create(**data)
            return work_space, None
        except Exception as e:
            error = Error.add_errors(name='Workspace creation failed', status=400, message='str{e}')
            return None, error
