import tempfile
from omegaconf import OmegaConf, MISSING, errors
from dataclasses import dataclass
import pytest

def test_invalid_config_additional_key():

    @dataclass
    class Output:
        measurement1: float = MISSING
        measurement2: int = MISSING
        user_input: str = MISSING

    output = dict(
        measurement1 = 1.1,
        measurement2 = 5,
        measurement3 = 10,
        user_input = "hi there",
    )

    with tempfile.NamedTemporaryFile(mode='w+') as config_fd:
        # Write an omega conf to a file that does not match the structured conf.
        conf = OmegaConf.create(output)
        config_fd.write(OmegaConf.to_yaml(conf))
        config_fd.flush()

        # Now validate against structured config - this should fail because what we wrote to the file
        # has an additional key.
        with pytest.raises(errors.ConfigKeyError):
            OmegaConf.merge(
                OmegaConf.structured(Output),
                OmegaConf.load(config_fd.name),
            )
