#!/usr/bin/env python3

from os import path
from urllib3.exceptions import InsecureRequestWarning

from portainer_deployer.utils.utils import update_config_dir
from .utils import *
from .config import ConfigManager
from . import VERSION, PHASE, PROG, DEFAULT_HELP_MESSAGE
from re import split as re_split
from functools import wraps
import argparse
import sys
import requests
class PortainerAPIConsumer:
    """Class to manage the Portainer API
    """    
    def __init__(self, api_config_path: str) -> None:
        PATH_TO_CONFIG = api_config_path

        # Load config
        self._portainer_config = ConfigManager(PATH_TO_CONFIG, default_section='PORTAINER')

        # Set non-ssl connection
        self.use_ssl = self._portainer_config.get_boolean_var('VERIFY_SSL')
        if not self.use_ssl and self._portainer_config.url.split('://')[0] == 'https':
            # Suppress only the single warning from urllib3 needed.
            requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

        # Set portainer connection parameters
        self.__portainer_connection_str = self._portainer_config.url
        self.__connection_headers = {'X-API-Key': self._portainer_config.token}

    def error_handler(method):
        """Decorator to use static error handler.

        Args:
            func (function): Function to be decorated.

        Returns:
            function: Decorated function.
        """
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            try:
                return method(self, *args, **kwargs) 
            
            except requests.exceptions.ConnectionError as e:
                return generate_response('Connection Error.', str(e), code=500)

            except requests.exceptions.Timeout as e:
                return generate_response('Connection timeout.', e, code=500)

            except requests.exceptions.TooManyRedirects as e:
                return generate_response('Too many redirects..', e, code=500)
            
            except requests.exceptions.HTTPError as e:
                if hasattr(e.response, 'json'):
                    res = generate_response(e.response.json().get('message'), e.response.json().get('details'), code=e.response.status_code)
                elif hasattr(e.response, 'text'):
                    res = generate_response(e.response.text, code=e.response.status_code)
                else:
                    res = generate_response(str(e), code=500)
                
                return res
            
            except requests.exceptions.RequestException as e:
                res = generate_response('Fatal error', str(e), code=e.response.status_code)
                return res
            
            except Exception as e:
                return generate_response(str(e), code=500)

        return wrapper 

    @error_handler
    def get_stack(self, name:str=None, stack_id:int=None) -> dict:
        """Get a stack from portainer

        Args:
            name (str, optional): Name of the stack in Portainer. Defaults to None.
            stack_id (int, optional): Id of the stack in Portainer. Defaults to None.

        Returns:
            dict: Dictionary with the status and detail of the operation.
        """
        spacing_str = '{0:<5} {1:<12} {2:<30} {3:30} {4:<30}'

        if stack_id:
                r = requests.get(
                    f"{self.__portainer_connection_str}/api/stacks/{stack_id}", 
                    headers=self.__connection_headers,
                    verify=self.use_ssl
                )
                
                r.raise_for_status()
                data = format_stack_info(r.json())

                print(spacing_str.format('Id', 'Endpoint Id', 'Name', 'Creation', 'Last Updated'))
                print(spacing_str.format(*data))

        elif name:
            r = requests.get(
                f"{self.__portainer_connection_str}/api/stacks", 
                headers=self.__connection_headers,
                verify=self.use_ssl
            )
            
            r.raise_for_status()
            data = format_stack_info_generator(r.json())

            print(spacing_str.format('Id', 'Endpoint Id', 'Name', 'Creation', 'Last Updated'))
            for stack in data:
                if stack[2] == name:
                    print(spacing_str.format(*stack))
                    break 
            else:
                raise Exception(f"Stack {name} not found in the database.")

        else:
            r = requests.get(
                f"{self.__portainer_connection_str}/api/stacks", 
                headers=self.__connection_headers,
                verify=self.use_ssl
            )
            
            r.raise_for_status()
            data = format_stack_info_generator(r.json())

            print(spacing_str.format('Id', 'Endpoint Id', 'Name', 'Creation', 'Last Updated'))
            for stack in data:
                print(spacing_str.format(*stack))

        return generate_response('Stack(s) pulled successfully', status=True, code=r.status_code)

    @error_handler
    def post_stack_from_str(self, stack: str, endpoint_id: int, name: str = None) -> dict:
        """Post a stack from str.

        Args:
            stack (str): String of the stack.
            endpoint_id (int): Id of the endpoint in Portainer.
            name (str): Name of the stack in Portainer.

        Returns:
            dict: Dictionary with the status and detail of the operation.
        """
        if not validate_yaml(data=stack):
            raise Exception('Invalid stack', 'Stack is not in a valid yaml format.')

        name = name if name else generate_random_hash()

        params = {
            "type": 2,
            "endpointId": endpoint_id,
            "method": "string"
        }

        r = requests.post(
            f"{self.__portainer_connection_str}/api/stacks", 
            headers=self.__connection_headers,
            params=params,
            json={
                "name": name,
                "stackFileContent": stack},
            verify=self.use_ssl
        )
        
        r.raise_for_status()
        logging.getLogger('stdout').info(f"Stack {name} created successfully!!!")
        return generate_response('Stack(s) pushed successfully', status=True, code=r.status_code)

    @error_handler
    def post_stack_from_file(self, path: str, endpoint_id: int, name: str = None) -> dict:
        """Post a stack from a file.

        Args:
            path (str): Path to the file.
            endpoint_id (int): Id of the endpoint in Portainer.
            name (str): Name of the stack in Portainer.

        Returns:
            dict: Dictionary with the status and detail of the operation.
        """        
        name = name if name else generate_random_hash()
        
        if not validate_yaml(path=path):
            raise Exception('Invalid stack', 'Stack is not in a valid yaml format.')
        
        # Open file
        with open(path, 'r') as f:
            params = {
                "type": 2,
                "endpointId": endpoint_id,
                "method": "file"
            }
            
            response = requests.post(self.__portainer_connection_str + '/api/stacks',
                data={ "Name": name}, 
                params=params,
                files={'file': f},
                headers=self.__connection_headers, 
                verify=self.use_ssl
            )
            response.raise_for_status()

            logging.getLogger('stdout').info(f"Stack {name} created successfully!!!")
            return generate_response(f'Stack {name} from {path} posted successfully under the endpoint {endpoint_id}.', status=True, code=response.status_code)

    @error_handler
    def delete_stack_by_id(self, stack_id: int, endpoint_id) -> dict:
        params = {
            "endpointId": endpoint_id,
            "external": False
        }
        r = requests.delete(
            f"{self.__portainer_connection_str}/api/stacks/{stack_id}", 
            headers=self.__connection_headers,
            verify=self.use_ssl,
            params=params
        )
        
        r.raise_for_status()
        logging.getLogger('stdout').info("Deleted successfully!!!")
        return generate_response('Stack(s) deleted successfully', status=True, code=r.status_code)

    @error_handler
    def delete_stack_by_name(self, name: str, endpoint_id: int) -> dict:

        r = requests.get(
            f"{self.__portainer_connection_str}/api/stacks", 
            headers=self.__connection_headers,
            verify=self.use_ssl,
        )
        
        r.raise_for_status()
        data = format_stack_info_generator(r.json())
        
        stack_id = None

        for stack in data:
            if stack[2] == name:
                stack_id = stack[0]
                break 
        else:
            raise Exception(f"Stack {name} not found in the database.")

        logging.getLogger('stdout').debug(f"Deleting stack {name}...")
        return self.delete_stack_by_id(stack_id, endpoint_id)

    @error_handler
    def delete_stack(self, endpoint_id: int, stack_name: str=None, stack_id: int=None) -> dict:
        """Delete a stack.

        Args:
            endpoint_id (int): Id of the endpoint in Portainer.
            stack_name (str): Name of the stack in Portainer.
            stack_id (int): Id of the stack in Portainer.

        Returns:
            dict: Dictionary with the status and detail of the operation.
        """
        if not stack_name and not stack_id:
            raise Exception('Invalid stack', 'Stack name or id is required.')

        # Takes stack_name only if stack_id is not provided  
        if stack_name and not stack_id:
            r = requests.get(
                f"{self.__portainer_connection_str}/api/stacks", 
                headers=self.__connection_headers,
                verify=self.use_ssl,
            )
            r.raise_for_status()
            data = format_stack_info_generator(r.json())
            
            stack_id = None

            for stack in data:
                if stack[2] == stack_name:
                    stack_id = stack[0]
                    break 
            else:
                raise Exception(f"Stack {stack_name} not found in the database.")

        # Takes stack_id and request portainer to delete the stack
        params = {
            "endpointId": endpoint_id,
            "external": False
        }
        r = requests.delete(
            f"{self.__portainer_connection_str}/api/stacks/{stack_id}", 
            headers=self.__connection_headers,
            verify=self.use_ssl,
            params=params
        )
        
        r.raise_for_status()
        logging.getLogger('stdout').info("Deleted successfully!!!")
        return generate_response('Stack(s) deleted successfully', status=True, code=r.status_code)

class PortainerDeployer:
    """Manage Portainer's Stacks usgin its API throught Command Line.
    """
    def __init__(self) -> None:
        """Initialize the PortainerDeployer class and runs the main function.
        """        
        local_path = path.abspath(path.dirname(__file__))

        # Load .env file if it exists, otherwise create a dump path
        env_file = path.join(local_path, '.env')
        if path.exists(env_file) and path.isfile(env_file):
            env_file = ConfigManager(path.join(local_path, '.env'), default_section='CONFIG')
            self.PATH_TO_CONFIG = path.join(local_path, env_file.path_to_config)
        else:
            update_config_dir(path_to_file='/this/is/a/dummy/path/please/create/one.conf', verify=False)

        self.parser = self.__parser()
        
        
    # Create API intantiator decorator
    def use_api(method):
        """Decorator to use the API.

        Args:
            func (function): Function to be decorated.

        Returns:
            function: Decorated function.
        """
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            # Set API consummer object when not in config mode
            self.api_consumer = PortainerAPIConsumer(api_config_path=self.PATH_TO_CONFIG)
            return method(self, *args, **kwargs)
        return wrapper


    def run(self):
        """Run the main function.
        """        
        # Set arguments
        parser_args = self.parser.parse_args(args=None if len(sys.argv) > 2 else [sys.argv[1], '-h'] if len(sys.argv) == 2 else ['-h'])
        
        response = parser_args.func(parser_args)

        if response['status']:
            # Exits with success
            sys.exit(0)
        else:
            self._error_handler(response['message'], response['details'])


    def __parser(self) -> argparse.ArgumentParser:
        """Parse and handle given arguments.

        Returns:
            parser (argparse.ArgumentParser): Main parser.
        """


        parser = argparse.ArgumentParser(
            description='Manage Portainer stacks with CLI.',
            prog=PROG,
            add_help=False
        )
        
        parser.add_argument('--version', '-v', action='version', version=f'{PROG} {VERSION} ({PHASE})', help="Show program's version and exit.")
        subparsers = parser.add_subparsers(help='Sub-commands for actions', dest='subparser_name')
        
        parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help=DEFAULT_HELP_MESSAGE)
        
        # ========================== Sub-command get ==========================
        parser_get = subparsers.add_parser('get',
            description='Get stack info from Portainer.',
            add_help=False
        )
        
        parser_get.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help=DEFAULT_HELP_MESSAGE)

        # Mutually exclusive arguments for --name and --id
        mutually_exclusive_name_id = parser_get.add_mutually_exclusive_group()

        mutually_exclusive_name_id.add_argument('--id',
            action='store',
            help="Id of the stack to look for",          
            type=int
        )

        mutually_exclusive_name_id.add_argument('--name',
            '-n',
            action='store',
            help="Name of the stack to look for",   
            type=str
        )


        mutually_exclusive_name_id.add_argument('--all',
            '-a',
            action='store_true',
            help="Gets all stacks",   
        )

        parser_get.set_defaults(func=self._get_sub_command)


        # ========================== Sub-command deploy ==========================
        parser_deploy = subparsers.add_parser(
            'deploy',
            description='Deploy stacks from a local file or stdin.',
            add_help=False)

        parser_deploy.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help=DEFAULT_HELP_MESSAGE)

        parser_deploy.add_argument('stack',
            action='store',
            nargs='?',
            help="Docker Compose string for the stack.",
            default=(None if sys.stdin.isatty() else ''.join(sys.stdin.readlines())))

        
        parser_deploy.add_argument('--path',
            '-p',
            action='store',
            type=str,
            help='The path to Docker Compose file for the stack. An alternative is to pass the stack as a string.',
            required=False,
            default=None)

        parser_deploy.add_argument('--name',
            '-n',
            action='store',
            help="Name of the stack to look for.",
            type=str
        )
        
        parser_deploy.add_argument('--update-keys', 
            '-u',
            action='extend', 
            type=str,
            nargs='+',
            help="Modify the stack file by passing a list of key=value pairs, where the key is in dot notation. i.e. a.b.c=value1 d='[value2, value3]'",
            default=[]
        )

        parser_deploy.add_argument('--redeploy', 
            '-R',
            action='store_true', 
            help="Re-deply in case of stacks exists.",
        )

        parser_deploy.add_argument('-y',
            action='store_true',
            help='Accept redeploy and do not ask for confirmation before redeploying the stack.',
        )

        parser_deploy.add_argument('--endpoint', 
            '-e',
            required=True if len(sys.argv) > 2 else False,
            action='store',
            type=int,
            help='Endpoint Id to deploy the stack.'
        )

        parser_deploy.set_defaults(func=self._deploy_sub_command)


        # ========================== Sub-command remove ==========================
        parser_remove = subparsers.add_parser('remove',
            description='Remove a stack from Portainer.',
            add_help=False
        )
        
        parser_remove.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help=DEFAULT_HELP_MESSAGE)

        # Mutually exclusive arguments for --name and --id
        mutually_exclusive_name_id_rm = parser_remove.add_mutually_exclusive_group()

        mutually_exclusive_name_id_rm.add_argument('--id',
            action='store',
            help="Id of the stack remove",          
            type=int
        )

        mutually_exclusive_name_id_rm.add_argument('--name',
            '-n',
            action='store',
            help="Name of the stack to remove",   
            type=str
        )

        parser_remove.add_argument('--endpoint', 
            '-e',
            required=True if len(sys.argv) > 2 else False,
            action='store',
            type=int,
            help='Endpoint Id from the stack to remove.'
        )


        parser_remove.add_argument('-y',
            action='store_true',
            help='Accept removal action and do not ask for confirmation.',
        )

        parser_remove.set_defaults(func=self._remove_sub_command)


        # ========================== Sub-command config ==========================
        parser_config = subparsers.add_parser(
            'config', 
            description='Configure Portainer CLI.',
            add_help=False)
        
        parser_config.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
            help=DEFAULT_HELP_MESSAGE)

        mutually_exclusive_config = parser_config.add_mutually_exclusive_group() 

        mutually_exclusive_config.add_argument('--set',
            '-s',
            action='extend',
            nargs='+',
            type=str,
            help="Set a config value specifying the section, key and value. e.g. --set section.url='http://localhost:9000'")

        mutually_exclusive_config.add_argument('--get',
            '-g',
            action='store',
            type=str,
            help='Get a config value. e.g. --get section.port')


        mutually_exclusive_config.add_argument('--config-path',
            '-c',
            action='store',
            type=str,
            help='Set Portainer Deployer absulute config path. e.g. --config-path /abusolute/path/to/default.conf')

        parser_config.set_defaults(func=self._config_sub_command)
 
        return parser
        

    def _error_handler(self, error_message: str, error_detail: str) -> None: 
        """Prints an error message and exits with error code.

        Args:
            error_message (str): Error message to be printed.
            error_code (int, optional): Error code to be used. Defaults to None.
        """        
        self.parser.error(f'{error_message}\n{error_detail}')


    def _config_sub_command(self, args) -> dict:
        """Config sub-command.

        Args:
            args (argparse.Namespace): Parsed arguments.
        """

        if args.config_path:
            update = update_config_dir(args.config_path)
            if update is str:
                return generate_response(update)
            else:
                msg = f'Config path updated to: {args.config_path}' 
                logging.getLogger('stdout').info(msg)
                return generate_response(message=msg, status=True)

        config = ConfigManager(self.PATH_TO_CONFIG)
        if args.set:
            for pair in args.set:
                splited = pair.split('=')
                if len(splited) != 2:
                    return generate_response(f'Invalid config pair: {pair}')
                
                value = splited[1]
                section_key = splited[0].split('.')
                if len(section_key) != 2:
                    return generate_response(f'Invalid config pair: {pair}')
                section, key = section_key  
                config.set_var(key=key, new_value=value, section=section)

            logging.getLogger('stdout').info(f'Config updated for: {args.set}')

        elif args.get:
            pair = args.get
            splited = pair.split('.')
            if len(splited) != 2:
                    return generate_response(f'Invalid config pair: {pair}')
            
            section,key = splited
            print(config.get_var(key=key, section=section))

        else:
            return generate_response('No config action specified')

        return generate_response(f'Config operation {"get" if args.get else "set" } completed successfully', status=True)


    @use_api
    def _get_sub_command(self , args: argparse.Namespace) -> dict:
        """Get sub-command default function. Excutes get functions according given arguments.

        Args:
            args (argparse.Namespace): Parsed arguments. 
        """        

        if args.all:
            response = self.api_consumer.get_stack()
        else:
            response = self.api_consumer.get_stack(name=args.name, stack_id=args.id)

        return response
        

    @use_api
    def _deploy_sub_command(self, args: argparse.Namespace) -> dict:
        """Deploy sub-command default function. Excutes deploy functions according given arguments.

        Args:
            args (argparse.Namespace): Parsed arguments. 
        """
        
        if args.stack and args.path:
            logging.getLogger('stdout').warning('Stack stdin and Path are both set. By default the stdin is used, so that, provided path will be ignored.\n')

        if args.redeploy:
            confirmation = True
            if not args.y:
                confirmation = request_confirmation('Are you sure you want to redeploy this Stack? It will be replaced by the new one.')

            if confirmation:
                logging.getLogger('stdout').info('Redeploy is set. It will try to delete the old stack if exists.')

                delete_resp = self.api_consumer.delete_stack_by_name(name=args.name, endpoint_id=args.endpoint)
                if not delete_resp['status']:
                    logging.getLogger('stdout').debug(f'Failed to delete stack: {args.name}. {delete_resp["message"]}')
                else:
                    logging.getLogger('stdout').debug(f"Recreating stack {args.name}...")
            
            else:
                return generate_response('Redeploy was canceled', status=False)

        if args.stack:
            if args.update_keys:
                return generate_response('Invalid use of --update-keys', 'You can not use "--update-keys" argument with "stack" positional argument. It is only available for "--path" argument.')

            response = self.api_consumer.post_stack_from_str(stack=args.stack, name=args.name, endpoint_id=args.endpoint)
        
        elif args.path:
            for pair in args.update_keys:
                if validate_key_value(pair=pair):
                    keys, new_value = pair.split('=', 1)
                    new_value = re_split(', |,', new_value[1:-1]) if new_value.startswith('[') else new_value
                    edited = edit_yml_file(path=args.path, key_group=keys, new_value=new_value)
                    if edited:
                        return generate_response(edited)
                
                else:
                    return generate_response(f'Invalid key=value pair in --update-keys argument: {pair}')

            response = self.api_consumer.post_stack_from_file(path=args.path, name=args.name, endpoint_id=args.endpoint)

        else:
            response = generate_response('No stack argument specified', 'No stack specified. Please pass it as stdin or use the "--path" argument.')

        return response


    @use_api
    def _remove_sub_command(self , args: argparse.Namespace) -> dict:
        """Remove sub-command default function. Excutes removal functions according given arguments.

        Args:
            args (argparse.Namespace): Parsed arguments. 
        """        
        confirmation = True
        if not args.y:
            confirmation = request_confirmation('Are you sure you want to remove this Stack?')

        if confirmation:
            response = self.api_consumer.delete_stack(stack_name=args.name, stack_id=args.id, endpoint_id=args.endpoint)
            return response
        else:
            return generate_response('Stack removal cancelled', status=False)



def main():
    """Main function."""
    PortainerDeployer().run()

if __name__ == '__main__':
    main()
