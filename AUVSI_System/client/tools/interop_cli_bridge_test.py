import os
import unittest
from interop_cli_bridge import InteropCliBridge

server = os.getenv('TEST_INTEROP_SERVER', 'http://localhost:8000')
username = os.getenv('TEST_INTEROP_USER', 'testuser')
password = os.getenv('TEST_INTEROP_USER_PASS', 'testpass')
admin_username = os.getenv('TEST_INTEROP_ADMIN', 'testadmin')
admin_password = os.getenv('TEST_INTEROP_ADMIN_PASS', 'testpass')

class InteropCliBridgeTest(unittest.TestCase):
    """test class base"""

    def test_get_mission(self):
        """If no exception is thrown then it worked."""
        interop_cli_bridge = InteropCliBridge(server, username, password)
        interop_cli_bridge.get_mission(1)



