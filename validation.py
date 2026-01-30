def validate_template(template: dict):
    if not template:
        raise ValueError("Template is empty")

    for day, exercises in template.items():
        if not isinstance(exercises, list) or len(exercises) == 0:
            raise ValueError(f"{day} has no exercises")

        for ex in exercises:
            if not isinstance(ex, tuple) or len(ex) != 3:
                raise ValueError(
                    f"Invalid exercise format in {day}: {ex}"
                )
