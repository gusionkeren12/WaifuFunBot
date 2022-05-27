async def extract_user(message):
    return (await extract_user_and_reason(message))[0]
