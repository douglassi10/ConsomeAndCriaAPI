import pytest
from app.load import retorna_instancia

@pytest.fixture(scope='module')
def app():
    # retorna uma instancia da aplicação
    return retorna_instancia()    