from operation.models.work_space import WorkSpace
from response.error_response import Error

error=Error()

class WorkSpaceService():
    def list(user_id):
        return WorkSpace.objects.filter(user=user_id)
    
    def create(data):
        try:
            work_space=WorkSpace.objects.create(**data)
            return work_space, None
        except Exception as e:
            return None, error.add_errors(name='Workspace creation failed', status=400, message='str{e}')
        
    def retrive(id, user_id):
        work_space=WorkSpace.objects.get(id=id, user=user_id)
        if work_space:
            return work_space, None
        return None, error.add_errors('Work Space error', 'Not found')
    
    def update(instance, data):
        try:
           for key, value in data.items():
               setattr(instance, key, value)
           instance.save()
           return instance , None
        except Exception as e:
           
            return None, {"error": error.add_errors('Not Foun',str(e))}
