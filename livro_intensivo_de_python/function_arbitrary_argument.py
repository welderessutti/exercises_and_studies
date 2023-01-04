def build_profile(first, last, **user_info):
    profile = dict()
    profile["First name"] = first
    profile["Last name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile("Albert", "Einstein", Location="Princeton", Field="Physics")

print(user_profile)
