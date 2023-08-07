from trickle.utils import parseArgs
from trickle.config import get_config, set_config
from trickle.trickle import sendTrickle

    
def main():
    args = parseArgs()
    if args["endpoint"] and args["token"]:
        set_config(args["endpoint"], args["token"])

    conf = get_config()
    if not conf:
        raise Exception("config is None, first set your config by running "\
            "'trickle send -e [endpoint] -t [token]'")
    
    send_args_list = args["send"]
    send_args_list.pop(0)
    if send_args_list:
        content = send_args_list[0]
        endpoint = conf.get("endpoint")
        token = conf.get("token")
        sendTrickle(content, endpoint, token)


if __name__ == "__main__":
    main()