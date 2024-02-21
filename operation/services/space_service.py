from operation.models.space import Space
from operation.models.work_space import WorkSpace
from response.error_response import Error

error=Error()

class SpaceService():
    def get_work_space(work_space_id):
        work_space = WorkSpace.objects.filter(id=work_space_id).first()
        if work_space:
            return work_space, None
        return None, error.add_errors(name='Workspace', message='Not Found')
    
    def list(work_space_id):
        return Space.objects.filter(work_space=work_space_id)
    
    def create(data):
        try:
            work_space=Space.objects.create(**data)
            return work_space, None
        except Exception as e:
            return None, error.add_errors(name='Workspace creation failed', message={str(e)})
        
    # def retrive(id, user_id):
    #     work_space=WorkSpace.objects.get(id=id, user=user_id)
    #     if work_space:
    #         return work_space, None
    #     return None, error.add_errors('Work Space error', 'Not found')
    
    # def update(instance, data):
    #     try:
    #        for key, value in data.items():
    #            setattr(instance, key, value)
    #        instance.save()
    #        return instance , None
    #     except Exception as e:
           
    #         return None, {"error": error.add_errors('Not Foun',str(e))}
