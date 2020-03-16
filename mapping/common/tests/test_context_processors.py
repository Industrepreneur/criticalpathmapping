import pytest

pytestmark = pytest.mark.django_db


@pytest.fixture
def products():
    from mapping.common.context_processors import products
    return products


# def test_products_context_processor(products):
#     request = {}
#     context = products(request)
#     product = context['products'][0]
#     # assert product.__class__ == mapping.tracking.models.product.Product
