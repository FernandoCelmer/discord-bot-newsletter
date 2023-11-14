from app.core.query import QueryField, QueryData
from app.tests.confmodel import Item


def test_query_field_instance():
    instance = QueryField(
        field='field',
        value=True
    )

    assert instance.field is 'field'
    assert instance.value is True


def test_query_data_load_keys():
    model_keys = QueryData.load_keys(model_class=Item)
    
    assert model_keys == ['id', 'status']


def test_query_data_setup_status_true():
    params_test = [
        {"status": 1},
        {"status": True},
        {"status": 'True'},
        {"status": 'true'},
        {"status": 'TRuE'},
        {"status": 'tRuE'},
    ]

    for params in params_test:
        instance = QueryData(
            model_class=Item,
            params=params
        )
        assert instance[0].value is True


def test_query_data_setup_status_false():
    params_test = [
        {"status": 0},
        {"status": False},
        {"status": 'False'},
        {"status": 'false'},
        {"status": 'FaLsE'},
        {"status": 'fAlSe'},
    ]

    for params in params_test:
        instance = QueryData(
            model_class=Item,
            params=params
        )
        assert instance[0].value is False


def test_query_data_instance():
    instance = QueryData(
        model_class=Item,
        params={
            "id": '1',
            "status": 'True'
        }
    )

    assert len(instance) is 2
    assert instance[0].field is Item.id
    assert instance[0].value is 1

    assert instance[1].field is Item.status
    assert instance[1].value is True
