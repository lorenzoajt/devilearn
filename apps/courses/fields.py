from django.core.exceptions import ObjectDoesNotExist
from django.db  import models


class OrderField(models.PositiveIntegerField):
    #definimos el constructor, si no le pasamos for_fields lo hace none
    def __init__(self, for_fields= None, *args, **kwargs):
        self.for_fields = for_fields #we add this field
        super().__init__(*args, **kwargs) #trae el constructor de positive integerfield

    #antes de que se guarde el modelo se ejecuta esta accion
    def pre_save(self, model_instance, add):
        #si la instancia que  estoy evaluando no tiene valor
        if getattr(model_instance, self.attname) is None:
            try:
                qs = self.model.objects.all() #traer todos los objetos del modelo al que pertenece mi campo
                if self.for_fields:
                    query = {
                        field: getattr(model_instance, field)
                        for field in self.for_fields
                    }

                    qs = qs.filter(**query) # los que tengan que ver con la instancia del for_fields
                
                last_item = qs.latest(self.attname)
                value = getattr(last_item, self.attname) + 1 # es como un count

            except ObjectDoesNotExist:
                value = 0

            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)

