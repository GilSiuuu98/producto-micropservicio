from rest_framework.test import APITestCase
from rest_framework import status
from .models import Producto

class ProductoEndpointsTest(APITestCase):
    def setUp(self):
        self.list_url = "/api/productos/"
        self.product_data = {
            "nombre": "Café",
            "descripcion": "Tueste medio",
            "precio": "12.50",
            "disponible": True
        }

    def test_crud_productos(self):
        # POST
        resp_post = self.client.post(self.list_url, self.product_data, format="json")
        self.assertEqual(resp_post.status_code, status.HTTP_201_CREATED)
        product_id = resp_post.data["id"]

        # GET list
        resp_list = self.client.get(self.list_url, format="json")
        self.assertEqual(resp_list.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp_list.data), 1)

        # GET detail
        resp_detail = self.client.get(f"{self.list_url}{product_id}/", format="json")
        self.assertEqual(resp_detail.status_code, status.HTTP_200_OK)

        # PUT
        updated_data = self.product_data.copy()
        updated_data["precio"] = "15.00"
        resp_put = self.client.put(f"{self.list_url}{product_id}/", updated_data, format="json")
        self.assertEqual(resp_put.status_code, status.HTTP_200_OK)
        self.assertEqual(resp_put.data["precio"], "15.00")

        # DELETE
        resp_delete = self.client.delete(f"{self.list_url}{product_id}/")
        self.assertEqual(resp_delete.status_code, status.HTTP_204_NO_CONTENT)