import schemathesis


@schemathesis.hooks.register
def after_load_schema(
    context: schemathesis.hooks.HookContext,
    schema: schemathesis.schemas.BaseSchema,
) -> None:
    schema.add_link(
        source=schema["/items/"]["POST"],
        target=schema["/items/{item_id}"]["GET"],
        status_code=201,
        parameters={"item_id": "$response.body#/item_id"},
    )
    schema.add_link(
        source=schema["/items/"]["GET"],
        target=schema["/items/{item_id}"]["GET"],
        status_code=200,
        # https://github.com/schemathesis/schemathesis/issues/900
        # only support hard coded curretly
        parameters={"item_id": "$response.body#/items/1/item_id"},
    )
