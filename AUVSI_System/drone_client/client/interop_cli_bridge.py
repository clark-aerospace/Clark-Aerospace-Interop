"""A python3 interface for python2 client

This class will alow the usage of the interop client class in a python3 script.
"""

import subprocess

class InteropCliBridge():
    """Client which provides a python3 interface to interop_cli.py

    The init function takes a log in info.

    System class are used to execute command line tool.
    """

    def __init__(self,
                 url,
                 username,
                 password):
        """Stor all interop server infor for use in system calls

        Args:
            url: Base URL of interoperability server
                (e.g., http://localhost:8000).
            username: Interoperability username.
            password: Interoperability password.
        """
        self.url = url
        self.username = username
        self.password = password

    def get_mission(self, mission_id :int)-> str:
        command = "python2 ../../client/tools/interop_cli.py --url "
        command += self.url + " "
        command += "--username "
        command += self.username + " "
        command += "--password "
        command += self.password + " "
        command += "mission --mission_id "
        command += str(mission_id)

        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, text=True)
        output, error = process.communicate() 

        return(output)     
