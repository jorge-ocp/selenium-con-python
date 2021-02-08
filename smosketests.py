from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from searchtests import SearchTest

#variables con las cuales estaremos cargando los casos de prueba
assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)

#construir suite de pruebas cargandole las variables de los casos
smoke_text = TestSuite([assertions_test, search_test])

#indicar parametros para construir el reporte
kwargs = {
    "output": 'smoke-report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_text)