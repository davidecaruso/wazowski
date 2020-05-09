from graphene import ObjectType, String, Int, Boolean, List, Schema

from src.wazowski import Wazowski


class Query(ObjectType):
    """
    GraphQL queries and resolvers
    """

    list = List(
        of_type=Int,
        start=Int(default_value=Wazowski.FIRST_PORT),
        end=Int(default_value=Wazowski.LAST_PORT),
        host=String(default_value=Wazowski.HOST)
    )

    check = Boolean(
        port=Int(required=True),
        host=String(default_value=Wazowski.HOST)
    )

    next = Int(
        port=Int(required=True),
        start=Int(default_value=Wazowski.FIRST_PORT),
        end=Int(default_value=Wazowski.LAST_PORT),
        host=String(default_value=Wazowski.HOST)
    )

    previous = Int(
        port=Int(required=True),
        start=Int(default_value=Wazowski.FIRST_PORT),
        end=Int(default_value=Wazowski.LAST_PORT),
        host=String(default_value=Wazowski.HOST)
    )

    random = Int(
        start=Int(default_value=Wazowski.FIRST_PORT),
        end=Int(default_value=Wazowski.LAST_PORT),
        host=String(default_value=Wazowski.HOST)
    )

    def resolve_list(self, info, start, end, host):
        return Wazowski.free_ports(start, end, host)

    def resolve_check(self, info, port, host):
        return Wazowski.is_port_free(port, host)

    def resolve_next(self, info, port, start, end, host):
        return Wazowski.next_free_port(port, start, end, host)

    def resolve_previous(self, info, port, start, end, host):
        return Wazowski.previous_free_port(port, start, end, host)

    def resolve_random(self, info, start, end, host):
        return Wazowski.random_free_port(start, end, host)


schema = Schema(query=Query)
