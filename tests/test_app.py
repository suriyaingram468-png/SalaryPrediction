import sys
import os

# Add the root directory to the path so we can import app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_app_import():
    """Test that the app can be imported."""
    try:
        import app  # noqa: F401
        assert True
    except ImportError:
        assert False, "Failed to import app"


def test_streamlit_app_exists():
    """Test that streamlit_app.py exists and can be imported."""
    try:
        import streamlit_app  # noqa: F401
        assert True
    except ImportError:
        assert False, "Failed to import streamlit_app"


# Add more tests as your application grows
