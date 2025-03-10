from dendrite import Dendrite
from dendrite.exceptions import DendriteException
from dotenv import load_dotenv

load_dotenv()

# Initiate client with authenticated session, read how create authentication sessions here: https://docs.dendrite.systems/concepts/authentication
client = Dendrite(auth="mail.google.com")

# Go to website with authenticated session
try:
    client.goto("https://mail.google.com/", expected_page="Gmail inbox")
except DendriteException as e:
    print("Authentication failed, page was not a Gmail inbox")
