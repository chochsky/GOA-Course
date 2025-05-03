def who_ate_the_cookie(x) -> str:
    if isinstance(x, str):
        name = "Zach"
    elif isinstance(x, (int, float)):
        name = "Monica"
    else:
        name = "the dog"
    return f"Who ate the last cookie? It was {name}!"
