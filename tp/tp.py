import uuid
from dataclasses import dataclass

from omegaconf import MISSING

@dataclass
class TestStepBaseConfig:
    output_directory: str = MISSING
    run_id: str = str(uuid.uuid4())
    step_id: str = str(uuid.uuid4())
