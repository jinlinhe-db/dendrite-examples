from dendrite import Dendrite
from dendrite.exceptions import DendriteException
from dotenv import load_dotenv
from dendrite.logic.llm.agent import LLM
from dendrite.logic.llm.config import LLMConfig
from dendrite.logic.config import Config
load_dotenv()

custom_agents = {
    "extract_agent": LLM("gpt-4", temperature=0.2),
    "scroll_agent": LLM("gpt-4", temperature=0.2),
    "ask_page_agent": LLM("gpt-4", temperature=0.2),
    "segment_agent": LLM("gpt-4", temperature=0.2),
    "select_agent": LLM("gpt-4", temperature=0.2),
    "verify_action_agent": LLM("gpt-4", temperature=0.2)
}

# Initialize config with custom agents
llm_config = LLMConfig(default_agents=custom_agents)
config = Config(llm_config=llm_config)
# Initate the Dendrite client
browser = Dendrite(config=config)

# Navigate with the `goto` method
browser.goto("https://google.com")

try:
    browser.click("Reject all cookies")
except DendriteException:
    print("No reject all cookies button found")

# Populate the search field and press Enter key
browser.fill("Search input field", "hello world")
browser.press("Enter")

# Extract the search results as a list of dicts with url and title
results = browser.extract("The search results as a list of dicts with url and title")
print(results)
