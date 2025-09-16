# Idosell Python SDK

A Python 3 SDK for the Idosell REST API ([official documentation](https://idosell.readme.io/docs/apps) and [reference](https://idosell.readme.io/reference)).
Inspired by the [@ltung7/idosell](https://github.com/ltung7/idosell) TypeScript library.

This library provides access to Idosell e-commerce platform APIs, enabling management of customers (CRM), orders (OMS), products (PIM), CMS content, system settings, and warehouse operations (WMS).

## Requirements

- Python >= 3.12
- httpx >= 0.27.0
- pydantic >= 2.1.0

## Installation

### Using uv (recommended)

[uv](https://github.com/astral-sh/uv) is a fast Python package/dependency manager.  
To prepare a virtual environment and install all dependencies:

```sh
uv venv .venv
source .venv/bin/activate
uv pip install -e .
```

### Using pip

```sh
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Quick Start

Initialize the API client and make your first request:

```python
from idosell.api_request import ApiRequest
from idosell.pim.products.categories import Get as GetCategories

# Initialize client
api = ApiRequest(
    base_url="https://yourshop.iai-shop.com/api/admin/v6",
    api_key="YOUR_API_KEY"
)

# Get product categories
categories_dto = GetCategories()
result = api.request(categories_dto)

print(result)
```

For API key authentication, set `IDOSELL_API_KEY` or `IDOSELL_BASE_URL` environment variables.

## API Modules

The library provides modular access to different Idosell systems:

- **PIM (Product Information Management)**: Manage products, categories, brands, collections, and variants
- **CRM (Customer Relationship Management)**: Handle customers, pricelists, discounts, and tags
- **OMS (Order Management System)**: Process orders, shipments, returns, and refunds
- **CMS (Content Management System)**: Manage entries, snippets, and configuration
- **System**: Configure shops, couriers, and deliveries
- **WMS (Warehouse Management System)**: Track inventory, locations, and suppliers

Each module includes GET, POST, PUT, DELETE operations with type-safe DTOs and Pydantic validation.

## Advanced Usage

See [USAGE.md](USAGE.md) for comprehensive examples, advanced patterns, bulk operations, async handling, error handling, and real-world integration guides.

## License

MIT

## Development

### Running Tests

```sh
pytest
```

### Linting

```sh
pylint idosell/
```

### Building

```sh
uv build
```

### Project Structure

- `idosell/cms/`: Content Management System
- `idosell/crm/`: Customer Relationship Management
- `idosell/oms/`: Order Management System
- `idosell/pim/`: Product Information Management
- `idosell/system/`: System-related
- `idosell/wms/`: Warehouse Management System
- `idosell/_common.py`: Shared enumerations, models, and utilities
- `idosell/api_request.py`: HTTP client for API requests
- `idosell/_samples/`: Sample DTOs for all modules
- `tests/`: Pytest-based tests

API version: Use v6 (`/api/admin/v6/`) for full functionality.
