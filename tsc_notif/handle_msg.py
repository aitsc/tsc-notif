from .utils import push_msg, PushPlusSend


def main(
    token: str = '',
    title: str = 'supervisor',
):
    if MSG['headers'].get('eventname') in {
        'PROCESS_STATE_FATAL',
        'PROCESS_STATE_EXITED',
        'PROCESS_COMMUNICATION',
    }:
        push_msg(PushPlusSend(
            token=token,
            title=title,
            content=MSG,
            template='json',
        ))


if __name__ == '__main__':
    MSG = {
        "time": "2024-07-22T18:06:40.177068+08:00",
        "time_zone": "Asia/Shanghai",
        "headers": {
            "ver": 3.0,
            "server": "supervisor",
            "serial": 482,
            "pool": "eventlistener-process",
            "poolserial": 1,
            "eventname": "PROCESS_STATE_EXITED",
            "len": 92
        },
        "payload": {
            "processname": "eventlistener-process",
            "groupname": "eventlistener-process",
            "from_state": "STOPPED",
            "tries": 0
        },
        "data": None
    }
    CONTEXT = {}
    
    main()
    exit(0)

# main()
