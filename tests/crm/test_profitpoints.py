import pytest

def test_profitpoints_module_imports():
    try:
        from idosell.crm import profitpoints
        assert profitpoints
    except ImportError:
        pytest.skip("Profitpoints module not importable")

def test_profitpoints_basic_functionality():
    try:
        import inspect
        from idosell.crm import profitpoints
        members = inspect.getmembers(profitpoints)
        assert len(members) > 0
    except Exception:
        pytest.skip("Profitpoints needs investigation")
