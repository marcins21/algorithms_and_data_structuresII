import paramiko
from simple_term_menu import TerminalMenu

# connection to dev-3
# cd /home/msitko/.ssh
# ssh -i /home/msitko/.ssh/pt-openstack.pem -p2222 utfuser@pt-wroc-dev-3-pl.dyn.nesc.nokia.net

PATH = "/home/msitko/.ssh/pt-openstack.pem"
KEY = paramiko.RSAKey.from_private_key_file(PATH)


class Connector:
    def __init__(self, ip, username, port):
        self.ip = ip
        self.username = username
        self.port = port

    def connect_to_host(self) -> None:
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=f"{self.ip}", username=f"{self.username}", port=self.port, pkey=KEY)
            while True:
                try:
                    cmd = input(f"{self.username}$> ")
                    if cmd == "exit":
                        break
                    stdin, stout, stderr = client.exec_command(cmd)
                    print(stout.read().decode())
                except KeyboardInterrupt:
                    break

        except Exception as error:
            print(str(error))


def term_menu():
    options = ["dev1", "dev2", "dev3"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"\nYou have selected {options[menu_entry_index]}!")
    return options[menu_entry_index]


# TODO: json file with credentials
if __name__ == "__main__":
    user_server_choose = term_menu()

    if user_server_choose == "dev1":
        print(f"\nConnection to {user_server_choose}")
        dev1 = Connector("--", "--", 000)
        dev1.connect_to_host()

    elif user_server_choose == "dev2":
        print(f"\nConnection to {user_server_choose}")
        dev2 = Connector("--", "--", 000)
        dev2.connect_to_host()

    elif user_server_choose == "dev3":
        print(f"\nConnection to {user_server_choose}\n")
        dev3 = Connector("10.40.226.253", "utfuser", 2222)
        dev3.connect_to_host()

    else:
        print(f"\nSomething went wrong!")
