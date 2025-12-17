def quality_check(provider):
    score = 0

    if provider.get("phone_valid"):
        score += 40
    if provider.get("address_valid"):
        score += 40
    if provider.get("license_number"):
        score += 10
    if provider.get("npi_id"):
        score += 10

    provider["confidence_score"] = score
    provider["needs_review"] = score < 80

    return provider
