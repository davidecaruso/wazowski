import random
import socket


class Wazowski:
    FIRST_PORT = 1024
    LAST_PORT = 65535
    HOST = '127.0.0.1'

    @staticmethod
    def free_ports(start=FIRST_PORT, end=LAST_PORT, host=HOST):
        """
        Return the free ports on host in a range
        :param start: The starting port of the range. Default: 1024
        :param end: The ending port of the range. Default: 65535
        :param host: The host. Default: 127.0.0.1
        :return: List of port numbers
        """
        ports = []
        while start <= end:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.bind((host, start))
                ports.append(start)
            except:
                pass

            s.close()
            start += 1

        return sorted(ports)

    @staticmethod
    def is_port_free(port, host=HOST):
        """
        Check if the given port is free or not
        :param port: The port of reference
        :param host: The host. Default: 127.0.0.1
        :return: True if port is free, False if port is not free
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((host, port))
            s.close()
            return True
        except:
            s.close()
            return False

    @staticmethod
    def random_free_port(start=FIRST_PORT, end=LAST_PORT, host=HOST):
        """
        Return a random free port on host in a range
        :param start: The starting port of the range. Default: 1024
        :param end: The ending port of the range. Default: 65535
        :param host: The host. Default: 127.0.0.1
        :return: Port number
        """
        return random.choice(Wazowski.free_ports(start, end, host))

    @staticmethod
    def previous_free_port(port, start=FIRST_PORT, end=LAST_PORT, host=HOST):
        """
        Return a the previous free port of a given port on host in a range
        :param port: The port of reference
        :param start: The starting port of the range. Default: 1024
        :param end: The ending port of the range. Default: 65535
        :param host: The host. Default: 127.0.0.1
        :return: Port number or None
        """
        for free_port in Wazowski.free_ports(start, end, host)[::-1]:
            if free_port < port:
                return free_port

    @staticmethod
    def next_free_port(port, start=FIRST_PORT, end=LAST_PORT, host=HOST):
        """
        Return a the next free port of a given port on host in a range
        :param port: The port of reference
        :param start: The starting port of the range. Default: 1024
        :param end: The ending port of the range. Default: 65535
        :param host: The host. Default: 127.0.0.1
        :return: Port number or None
        """
        for free_port in Wazowski.free_ports(start, end, host):
            if free_port > port:
                return free_port
