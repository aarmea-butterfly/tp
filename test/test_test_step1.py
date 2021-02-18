from subprocess import check_output
import sys
import pathlib
import tempfile
import yaml

THIS_DIR = pathlib.Path(__file__).parent.absolute()

def test_run_no_arg():
    s = check_output([
        'python',
        str(THIS_DIR / '../steps/test_step1.py'),
    ]).decode(sys.stdout.encoding)
    assert "output_directory: ???" in s

def test_run_override_cli():
    s = check_output([
        'python',
        str(THIS_DIR / '../steps/test_step1.py'),
        'base.output_directory=/tmp',
    ]).decode(sys.stdout.encoding)
    assert "output_directory: /tmp" in s

def test_run_override_yaml():
    with tempfile.NamedTemporaryFile(mode='w+') as ntf:
        ntf.write(yaml.dump(
            dict(base=dict(output_directory="/tmp"), params=dict(dc=22))
        ))
        ntf.flush()
        s = check_output([
            'python',
            str(THIS_DIR / '../steps/test_step1.py'),
            '--config',
            ntf.name,
        ]).decode(sys.stdout.encoding)
        print(s)

    assert "output_directory: /tmp" in s
    assert "dc: 22.0" in s

def test_run_override_and_get_output():
    with tempfile.NamedTemporaryFile(mode='w+') as config_fd, \
            tempfile.NamedTemporaryFile(mode="r") as output_fd:
        config_fd.write(yaml.dump(
            dict(base=dict(output_directory="/tmp"), params=dict(dc=22))
        ))
        config_fd.flush()
        s = check_output([
            'python',
            str(THIS_DIR / '../steps/test_step1.py'),
            '--config',
            config_fd.name,
            '--output',
            output_fd.name,
        ]).decode(sys.stdout.encoding)
        print(s)

        assert "output_directory: /tmp" in s
        assert "dc: 22.0" in s
        output = yaml.safe_load(output_fd)
        assert output['measurement'] == 1000.0
        assert output['user_input'] == "User Input"
