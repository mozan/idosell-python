# Idosell Python SDK

A Python 3 SDK for the Idosell REST API ([official documentation](https://idosell.readme.io/docs/apps) and [reference](https://idosell.readme.io/reference)).
Inspired by the [@ltung7/idosell](https://github.com/ltung7/idosell) TypeScript library.

This library provides access to Idosell e-commerce platform APIs, enabling management of customers (CRM), orders (OMS), products (PIM), CMS content, system settings, and warehouse operations (WMS).

## Requirements

- Python >= 3.12
- httpx >= 0.27.0
- pydantic >= 2.1.0

## License

MIT

## Features

- Modular API clients for different IdoSell systems (CMS, CRM, OMS, PIM, System, WMS)
- Data validation and typing with Pydantic v2
- Sync and async HTTP requests using httpx
- Auto-generated DTOs and gateways from API specifications
- Enum validations and strict typing

## Project Structure

- `idosell/cms/`: Content Management System
- `idosell/crm/`: Customer Relationship Management
- `idosell/oms/`: Order Management System
- `idosell/pim/`: Product Information Management
- `idosell/system/`: System-related
- `idosell/wms/`: Warehouse Management System
- `idosell/_common.py`: Common enumerations, models, and utilities
- `idosell/api_request.py`: Base HTTP client for API requests
- `idosell/_samples/`: Sample DTOs usage for each module
- `tests/`: Pytest based tests

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

## Usage

Initialize an API request client:

```python
from idosell.api_request import ApiRequest

api = ApiRequest(
    base_url="https://yourshop.iai-shop.com/api/admin/v3",
    api_key="YOUR_API_KEY"
)
```

Example usage with CRM clients:

```python
from idosell.crm.clients import Get

# Get clients with pagination
clients_dto = Get(results_page=0, results_limit=10)
response = api.request(clients_dto)

print(response)
```

Async usage:

```python
import asyncio

async def main():
    # Same DTO instance can be reused
    result = await api.async_request(clients_dto)
    print(result)

asyncio.run(main())
```

See the specific module files for available endpoints, models, and enums.

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
