from rest_framework import views, response
from .models import Product
from .serializers import WarehouseSerializer


class WarehouseAPI(views.APIView):

    def get(self, request, *args, **kwargs):
        shirt_qty = self.request.query_params.get('1', None)
        jeans_qty = self.request.query_params.get('2', None)
        if shirt_qty is None:
            return response.Response({'message': "Ko'ylakni kodini berishni unitdingiz!"}, status=400)
        if jeans_qty is None:
            return response.Response({'message': "Shimni kodini berishni unitdingiz!"}, status=400)
        result = list()
        for p in Product.objects.all():
            data = dict()
            qty = int(self.request.query_params.get(str(p.code)))
            data['product_name'] = p.name
            data['product_qty'] = qty
            materials = list()
            for i in p.materials.all():
                total = i.quantity * qty
                for j in i.material.warehouse.filter(qty__gt=0).order_by('-qty'):
                    dt = WarehouseSerializer(j).data
                    if j.qty >= total:
                        dt['qty'] = total
                        j.qty -= total
                        j.save()
                        total = 0
                    else:
                        dt['qty'] = j.qty
                        total -= j.qty
                        j.qty = 0
                        j.save()
                    materials.append(dt)
                if total > 0:
                    dt = dict()
                    dt['warehouse_id'] = None
                    dt['material_name'] = i.material.name
                    dt['price'] = None
                    dt['qty'] = total
                    materials.append(dt)
            data['product_materials'] = materials
            result.append(data)
        return response.Response({'result': result})
