import os, sys, pathlib

NOTEBOOKS_DIR = pathlib.Path(__file__).parent
REDPO_DIR = NOTEBOOKS_DIR.parent
DJANGO_PROJECT_ROOT = REDPO_DIR / "src"
DJANGO_SETTINGS_MODULE = "ai_agentic.settings"

def init(verbose=False):
    # Apply nest_asyncio patch to allow nested event loop in jupyter
    try:
        import nest_asyncio

        nest_asyncio.apply()
        if verbose:
            print("Apply nested_asyncio patch jupyter compatibility")
    except ImportError:
        if verbose:
            print("Nested_asyncio not available, skipping patch")

    os.chdir(DJANGO_PROJECT_ROOT)
    sys.path.insert(0, str(DJANGO_PROJECT_ROOT))
    if verbose:
        print(f"Change working directory: {DJANGO_PROJECT_ROOT}")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    import django
    django.setup()


