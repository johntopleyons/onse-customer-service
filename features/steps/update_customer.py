from behave import when


@when('I update the surname of customer with ID "{customer_id:d}" to'
      ' "{new_surname}"')
def update_customer(context, customer_id, new_surname):
    context.response = context.web_client.get(f'/customers/{customer_id}')
    body = context.response.get_json()
    body['surname'] = new_surname

    response = context.web_client.put(f'/customers/{customer_id}', json=body)

    assert response.status_code == 200, response.status_code
    assert response.is_json
    body = response.get_json()
    assert f"{body['surname']}" == new_surname
