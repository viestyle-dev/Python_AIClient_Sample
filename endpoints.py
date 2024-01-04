def train_by_mode() -> str:
    return "api/v3/train_by_mode"


def inference(model_id: int) -> str:
    return f"api/v3/model/{model_id}/inference"

