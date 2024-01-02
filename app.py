from streamlit.logger import get_logger
from meta import meta
from main import main   

LOGGER = get_logger(__name__)

use_auth = False

def app():
    meta()  # Set meta-information for the app
    main()

if __name__ == "__main__":
    app()
