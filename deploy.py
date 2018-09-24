import argparse
import subprocess


def argparse_init():
    parser = argparse.ArgumentParser()
    parser.add_argument('--network', '-n', action='store_true')
    parser.add_argument('--build', '-b', nargs=1, choices=['dev'])
    return parser.parse_args()


def create_network():
    subprocess.run(['docker network create pasta_net'], shell=True)


def build_docker_container(docker_compose_filename, docker_container_name=None):
    if docker_container_name is None:
        subprocess.run(['docker-compose -f {} down -v --remove-orphans'.format(docker_compose_filename)], shell=True)
        subprocess.run(['docker-compose -f {} build --no-cache'.format(docker_compose_filename)], shell=True)
        subprocess.run(['docker-compose -f {} up -d'.format(docker_compose_filename)], shell=True)
    else:
        subprocess.run(['docker-compose -f {} stop {}'.format(docker_compose_filename, docker_container_name)], shell=True)
        subprocess.run(['docker-compose -f {} rm -f {}'.format(docker_compose_filename, docker_container_name)], shell=True)
        subprocess.run(['docker-compose -f {} build --no-cache {}'.format(docker_compose_filename, docker_container_name)], shell=True)
        subprocess.run(['docker-compose -f {} up -d {}'.format(docker_compose_filename, docker_container_name)], shell=True)


def run_build(build_type):
    if build_type == 'dev':
        create_network()
        build_docker_container('./db/docker-compose-postgres.yaml')
        build_docker_container('./app/docker-compose-python.yaml')
        build_docker_container('./client/docker-compose-frontend.yaml')


if __name__ == '__main__':
    args = argparse_init()
    if args.network:
        create_network()
    elif args.build:
        run_build(args.build[0])
