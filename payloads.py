import numpy as np

inference = {
    "user_id": "1703057492-423e484a-2535-4227-9ca2-2095b68ed5e2",
    "mode": 0,
    "activity_type": "focus",
    "data": {
        "left": np.random.random(2400).tolist(),
        "right": np.random.random(2400).tolist(),
    },
}

train_by_mode = {
    "user_id": "1703057492-423e484a-2535-4227-9ca2-2095b68ed5e2",
    "mode": 0,
    "model_name": "Test from local",
    "raw_data_collection_id": 1,
    "data": {
        "base": {
            "left": np.random.random(24000).tolist(),
            "right": np.random.random(24000).tolist(),
        },
        "target": {
            "left": np.random.random(24000).tolist(),
            "right": np.random.random(24000).tolist(),
        },
    },
}
