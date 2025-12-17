from agents.validation_agent import validate_provider
from agents.enrichment_agent import enrich_provider
from agents.qa_agent import quality_check
from agents.directory_agent import update_directory

def run_agentic_pipeline(provider):
    provider = validate_provider(provider)
    provider = enrich_provider(provider)
    provider = quality_check(provider)
    provider = update_directory(provider)
    return provider
