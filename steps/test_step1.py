from omegaconf import OmegaConf, MISSING
from tp import TestStepBaseConfig
from argparse import ArgumentParser
from dataclasses import dataclass

@dataclass
class TestStep1Config:
    dc: float = 15
    ac: float = 5

@dataclass
class Config:
    base: TestStepBaseConfig = TestStepBaseConfig()
    params: TestStep1Config = TestStep1Config()

@dataclass
class Output:
    measurement: float = MISSING
    user_input: str = MISSING


def main():
    parser = ArgumentParser('Test Step 1')
    parser.add_argument(
        '--config',
        required=False,
        help='the path of the yaml config file',
        default=None,
    )

    parser.add_argument(
        '--output',
        required=False,
        help='the path of the yaml config file',
        default=None,
    )

    args, unknown = parser.parse_known_args()

    configs = list(
        filter(
            lambda x: x is not None,
            [
                OmegaConf.structured(Config),
                OmegaConf.from_cli(unknown),
                None if args.config is None else OmegaConf.load(args.config),
            ],
        ),
    )

    cfg = OmegaConf.merge(*configs)
    print(OmegaConf.to_yaml(cfg))

    if args.output is not None:
        out: Output = OmegaConf.structured(Output)
        out.measurement = 1000.0
        out.user_input = "User Input"
        with open(args.output, 'w+') as ofd:
            ofd.write(OmegaConf.to_yaml(out))

if __name__ == "__main__":
    main()
