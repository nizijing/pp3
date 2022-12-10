player_creation_functions = {}


def register(role, func):
    player_creation_functions[role] = func


def unregister(role):
    player_creation_functions.pop(role, None) # None的作用，如果不存在则返回None


def create_player(args):
    the_args = args.copy()
    role = the_args['role']

    try:
        func = player_creation_functions[role]
        return func(**the_args)
    except KeyError:
        raise ValueError(f'未知的角色 {role}') from None
