import pytest
from system.utils import *
from indy import payment


@pytest.mark.usefixtures('docker_setup_and_teardown')
class TestFeesSuite:

    @pytest.mark.asyncio
    async def test_case(self):
        pass