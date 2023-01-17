### API framework with Python


## feature/01-test-python-api

    - Armar un proyecto: 
        Entorno: python3 -m venv venv 
        instalar las dependencias: pytest, requests, assertpy
        Armar bookings_test.py
    - Redactar los tests con los módulos json, assert y requests.


## feature/02-test-python-api

    -Armar módulo tests y archivo config
    - Armar la carpeta data y hacer un read_file en helpers (2 funciones)
    - Luego importar a test e incorporar en el dump el reader con el archivo.

## feature/03-test-python-api

    - Hacer la utils de assertion y request e importar al archivo de booking_test

## feature/04-test-python-api

    - Incorporar reportes en Allure y decoradores en Pytest y Allure

## Lista de Comandos para Allure:
    @allure.description('description') # Descripción del test
    @allure.testcase('testcase_url', 'testcase_name') # Link relacionado al caso de prueba
    @allure.link('link_url', 'link_type', 'link_name') # Links relacionados al test
    @allure.mark.critical # Tags del test
    @allure.tag('tag') # Tags del test
    @allure.severity('severity') # Alternativa a "pytest.mark.critical"
    @allure.parent_suite('parent_suite')
    @allure.suite('suite') # Nombre de la suite (default=nombre de la clase)
    @allure.sub_suite('sub_suite')
    @allure.testcase('url', 'name')
    @allure.epic('epic')
    @allure.feature('feature') # NO SE USA ACTUALMENTE
    @allure.story('story') # NO SE USA ACTUALMENTE
    @allure.issue('issue') # DEJA EL TEST FUERA DEL REPORTE
    @allure.id('id') # id del test NO SE USA ACTUALMENTE
    @allure.label('label') NO SE USA ACTUALMENTE

    --junitxml=build/testResult.xml
    allure serve reports
