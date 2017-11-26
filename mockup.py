import mock
import setuptools

with mock.patch.object(setuptools, 'setup') as mock_setup:
    import setup  # This is setup.py which calls setuptools.setup

# called arguments are in `mock_setup.call_args`
args, kwargs = mock_setup.call_args
print kwargs.get('install_requires', [])
