import json
import unittest
import re

#1)Abrir el json
# $$$$$$$$$$$$$$$$$$$$$$$$$$IMPORTANTE$$$$$$$$$$$ MODIFIQUE EL NOMBRE AGREGANDO UN _1 PARA VER SI RESUELVO EL OTRO LUEGO
with open('user_info_1.json') as f:
	data=json.load(f)

class TestStringMethods(unittest.TestCase):

#2) Verificar _typename=User parseando el json
    def test_type_name(self):
        self.assertEqual(data['data']['user']['result']['__typename'],'User')

#3)Verificar que sean 32
    def test_id_length(self):
        self.assertTrue(len(data['data']['user']['result']['id'])<=32)

#4) Verificar que rest_id posea solo numeros
    def test_rest_id_number(self):
        self.assertTrue(re.match('[-+]?\d+$', data['data']['user']['result']['rest_id']))

#5) Verificar name no este vacio ( is_empty )
	
    def test_name_empty(self):
        self.assertTrue(len(data['data']['user']['result']['legacy']['name'])!=0)

#6)Que screen_name no sea un dato vacío
    def test_name_b_empty(self):
        self.assertTrue(len(data['data']['user']['result']['legacy']['screen_name'])!=0)
#7) Que las siguientes columnas sean de tipo entero:   
    def test_is_int(self):
        self.assertTrue(isinstance(data['data']['user']['result']['legacy']['fast_followers_count'],int))

    def test_is_int2(self):
        self.assertTrue(isinstance(data['data']['user']['result']['legacy']['followers_count'],int))

    def test_is_int3(self):
        self.assertTrue(isinstance(data['data']['user']['result']['legacy']['friends_count'],int))

    def test_is_int4(self):
        self.assertTrue(isinstance(data['data']['user']['result']['legacy']['listed_count'],int))

    def test_is_int5(self):
        self.assertTrue(isinstance(data['data']['user']['result']['legacy']['media_count'],int))

    def test_is_int5(self):
        self.assertTrue(isinstance(data['data']['user']['result']['legacy']['normal_followers_count'],int))

    def test_is_int5(self):
        self.assertTrue(isinstance(data['data']['user']['result']['legacy']['statuses_count'],int))


#y con el resto de columnas es igual:)

if __name__ == '__main__':
    unittest.main()





