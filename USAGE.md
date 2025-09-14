# Idosell REST API (Python v3)

This package wraps the Idosell REST API to make it easier to use by implementing chainable options, intuitive methods, and helpers for formatting requests. The [official Idosell documentation](https://idosell.readme.io/docs) still applies.

## Basic use

The Python package exposes readable method names matching the REST verbs and endpoints, using Pythonic snake_case. Most methods retain their original names but converted to snake_case.

TODO - make it clearer!!

```python
import asyncio
from idosell.client import IdosellClient
from idosell.models.enums import EnumGateType

async def main():
    client = IdosellClient("https://yourshop.iai-shop.com", "API_KEY")
    # Example usage (implementations are placeholders)
    # categories = await client.products.get_categories()
    # orders = await client.orders.get_orders()
    # returns = await client.returns.get_returns()
    # clients = await client.clients.get_clients()
    # enums = client.enums.get_enum(EnumGateType.PRODUCTS_RETURN_ELEMENTS)
    await client.close()

asyncio.run(main())
```

---

```python
from idosell import Idosell

# Initialize the client
idosell_request = Idosell(shop_url="https://yourdomain.com", api_key="API_KEY", api_version="v3")
print(idosell_request)
```

**Sample output:**

```json
{
    "method": null,
    "endpoint": null,
    "params": {},
    "base_url": "https://yourdomain.com/api/admin/v3",
    "headers": {
        "X-API-KEY": "API_KEY",
        "Content-Type": "application/json"
    }
}
```

- **API_KEY**: Obtainable from your Idosell panel.
- **SHOP_URL**: Base URI of your shop, e.g.: `https://yourdomain.com`, `https://clientXXXX.idosell.com`, `https://yourshop.iai-shop.com`.
- **API_VERSION**: Defaults to `v3`.

### Properties vs Endpoints

After creating the client, access its properties to work with specific endpoints. For example:

```python
# GET /products/categories
categories = idosell_request.get_products_categories().params({"ids": [1,2,3]}).exec()
print(categories)
```

**Sample output:**

```json
{
    "count": 3,
    "data": [
        { "categoryId": 1, "name": "Electronics" },
        { "categoryId": 2, "name": "Books" },
        { "categoryId": 3, "name": "Clothing" }
    ]
}
```

```python
# PUT /products/categories
create_category = idosell_request.put_products_categories().params({"name": "New Category"}).exec()
print(create_category)
```

**Sample output:**

```json
{ "status": "success", "categoryId": 42 }
```

Some endpoint-method mappings:

```python
idosell_request.get_products().exec()         # GET /products/products
idosell_request.search_products().exec()      # POST /products/products/search
idosell_request.delete_products().exec()      # POST /products/products/delete
idosell_request.delete_products_opinions().exec()  # POST /products/opinions/opinions/delete
```

### Chaining methods to set request parameters

You can chain methods named after parameters:

```python
categories = (
    idosell_request
    .get_products_categories()
    .ids([123, 456, 789])
    .languages(["pol", "eng"])
    .result_page(1)
    .result_limit(10)
    .exec()
)
print(categories)
```

**Sample output:**

```json
[
    { "categoryId": 123, "language": "pol" },
    { "categoryId": 456, "language": "eng" }
]
```

**Generated GET URL:**

```
https://yourdomain.com/api/admin/v3/products/categories?ids=123,456,789&languages=pol,eng&result_page=1&result_limit=10
```

For POST:

```python
rebate = (
    idosell_request
    .post_discounts_rebates_code()
    .campaign_id(123)
    .code_number("REBATECODE")
    .exec()
)
print(rebate)
```

**Sample output:**

```json
{ "status": "created", "codeId": 987 }
```

## Helper functions

### Page and Count

Many endpoints support pagination. Use `page(page_number, limit)` or `count()`:

```python
count = idosell_request.get_products_categories().count()
print(count)
```

**Sample output:**

```
42
```

```python
categories = idosell_request.get_products_categories().page(1, 10).exec()
print(categories)
```

**Sample output:**

```json
{
    "page": 1,
    "limit": 10,
    "data": [ ... ]
}
```

### Looping through pages

Requests track paging via `has_next()`:

```python
req = idosell_request.get_returns().dates("2023-12-01").page(0, 10)
while req.has_next():
    results = req.exec()
    print(results)
```

**Sample output:**

```json
{ "page": 0, "data": [ ... ], "hasNext": true }
{ "page": 1, "data": [ ... ], "hasNext": false }
```

### Date, date ranges and formatting

Use `dates(start_date, end_date, date_type)` for date ranges:

```python
dispatched = (
    idosell_request
    .search_orders()
    .dates("2023-12-01", "2023-12-31", "dispatch")
    .exec()
)
print(dispatched)
```

**Sample output:**

```json
{
  "ordersRange": {
    "ordersDateRange": {
      "ordersDateBegin": "2023-12-01 00:00:00",
      "ordersDateEnd": "2023-12-31 23:59:59",
      "ordersDateType": "dispatch"
    }
  },
  "data": [ ... ]
}
```

Single date defaults to now:

```python
from datetime import datetime, timedelta
orders = idosell_request.search_orders().dates(datetime.now() - timedelta(days=1)).exec()
print(orders)
```

**Sample output:**

```json
{ "range": "2025-07-24 12:00:00" to "2025-07-25 12:00:00", "data": [ ... ] }
```

## Array of objects

### Simple objects

```python
analytics = idosell_request.get_orders_analytics().serial_numbers([123, 456, 789]).exec()
print(analytics)
```

**Sample output:**

```json
{
  "orders": [
    { "orderSerialNumber": 123 },
    { "orderSerialNumber": 456 },
    { "orderSerialNumber": 789 }
  ]
}
```

### Complex objects

Use `append()` to build arrays:

```python
update = idosell_request.put_products().settings({"settingModificationType":"edit"})
update.product_id(101).product_displayed_code("CODE1").append()
update.product_id(102).product_displayed_code("CODE2").product_retail_price(99.99).append()
update.product_id(103).product_displayed_code("CODE3").product_note("Latest product").exec()
print(update)
```

**Sample output:**

```json
{
  "settings": {"settingModificationType": "edit"},
  "products": [
    { "productId": 101, "productDisplayedCode": "CODE1" },
    { "productId": 102, "productDisplayedCode": "CODE2", "productRetailPrice": 99.99 },
    { "productId": 103, "productDisplayedCode": "CODE3", "productNote": "Latest product" }
  ]
}
```

Or in loops:

```python
codes = [{"id":202,"code":"CODE202"}, {"id":203,"code":"CODE203"}]
update = idosell_request.put_products().settings({"settingModificationType":"edit"})
for item in codes:
    update.product_id(item["id"]).product_displayed_code(item["code"]).append()
update.exec()
```

**Sample output:**

```json
{ "status": "updated", "modifiedCount": 2 }
```

## Enums

Import and use ENUMS:

```python
from idosell import ENUMS
result = idosell_request.search_products().return_elements([ENUMS.PRODUCTS_RETURN_ELEMENTS.CODE]).exec()
print(result)

status = idosell_request.get_returns().status(ENUMS.RETURN_STATUS.ACCEPTED).exec()
print(status)
```

**Sample output:**

```json
{ "data": [ ... ], "returnStatus": "ACCEPTED" }
```

## Other formatters

### order_by

```python
lowest = idosell_request.get_products_opinions().order_by("rating", ascending=True).exec()
print(lowest)
```

**Sample output:**

```json
{ "ordersBy": [ { "elementName": "rating", "sortDirection": "ASC" } ], "data": [ ... ] }
```

### set_text

```python
update = (
    idosell_request
    .put_products()
    .product_id(202)
    .set_text("Świetny produkt")
    .set_text("Awesome product", type="short", language_id="eng")
    .set_text("<p>This product is really amazing</p>", type="long", language_id="eng", shop_id=1)
    .exec()
)
print(update)
```

**Generated request body:**

```json
{
  "products": [
    {
      "productId": 202,
      "productParamDescriptions": {
        "productParamDescriptionsLangData": [
          { "langId": "pol", "productParamDescriptions": "Świetny produkt" },
          { "langId": "eng", "productParamDescriptions": "Awesome product" }
        ]
      },
      "productLongDescriptions": {
        "productLongDescriptionsLangData": [
          { "langId": "eng", "shopId": 1, "productLongDescription": "<p>This product is really amazing</p>" }
        ]
      }
    }
  ]
}
```

### params

```python
query = {"orderSource": {"auctionsParams": {"auctionsServicesNames": ["allegro"]}}}
orders = idosell_request.params(query).exec()
print(orders)
```

**Sample output:**

```json
{ "data": [ ... ] }
```

## Debugging

Retrieve parameters without sending:

```python
params = idosell_request.search_orders().orders_serial_numbers([123,456,789]).get_params()
print(params)
```

**Sample output:**

```python
{ "ordersSerialNumbers": [123, 456, 789] }
```

## Examples

See more examples and documentation at [https://idosell-converter.vercel.app/examples](https://idosell-converter.vercel.app/examples)
