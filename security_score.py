def calculate_score(risk):

    scores = {
        "Low": 95,
        "Medium": 70,
        "High": 40,
        "Critical": 10,
        "Unknown": 0
    }

    return scores.get(risk, 0)