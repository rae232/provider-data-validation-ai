def validate_provider(provider):
    phone = str(provider.get("phone", ""))
    address = str(provider.get("address", ""))

    provider["phone_valid"] = len(phone) == 10
    provider["address_valid"] = len(address) > 10

    return provider
