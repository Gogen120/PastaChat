import os
import argparse
import subprocess
import docker

FLASK_CONTAINER = 'pasta_chat.flask'
DOCKER_NETWORK = os.environ['DOCKER_NETWORK']


def get_container_by_name(container_name):
    client = docker.from_env()
    return client.containers.get(container_name)


def create_network():
    client = docker.from_env()
    if client.networks.list(names=[DOCKER_NETWORK]):
        print(f'::: Network {DOCKER_NETWORK} already exist')
    else:
        print(f'::: Creating {DOCKER_NETWORK} network')
        client.networks.create(name=DOCKER_NETWORK)


def build_docker_container(docker_compose_filename, docker_container_name=None):
    if docker_container_name is None:
        subprocess.run([f'docker-compose -f {docker_compose_filename} down -v --remove-orphans'], shell=True)
        subprocess.run([f'docker-compose -f {docker_compose_filename} build --no-cache'], shell=True)
        subprocess.run([f'docker-compose -f {docker_compose_filename} up -d'], shell=True)
    else:
        subprocess.run([f'docker-compose -f {docker_compose_filename} stop {docker_container_name}'], shell=True)
        subprocess.run([f'docker-compose -f {docker_compose_filename} rm -f {docker_container_name}'], shell=True)
        subprocess.run([f'docker-compose -f {docker_compose_filename} build --no-cache {docker_container_name}'], shell=True)
        subprocess.run([f'docker-compose -f {docker_compose_filename} up -d {docker_container_name}'], shell=True)


def apply_migrations():
    flask_container = get_container_by_name(FLASK_CONTAINER)

    print('::: Running migrations')

    _, output = flask_container.exec_run('flask db upgrade', tty=True)

    print(output.decode('utf-8'))


def run_temp_functions():
    flask_container = get_container_by_name(FLASK_CONTAINER)

    print('::: Running temp functions')

    _, output = flask_container.exec_run('python pasta_chat/temp/__init__.py')

    print(output.decode('utf-8'))


def run_tests():
    subprocess.run([f'docker exec {FLASK_CONTAINER} pytest'], shell=True)


def run_build(build_type):
    if build_type == 'dev':
        create_network()
        build_docker_container('./db/docker-compose-postgres.yaml')
        build_docker_container('./app/docker-compose-python.yaml')
        build_docker_container('./client/docker-compose-frontend.yaml')
        apply_migrations()
        run_temp_functions()


def argparse_init():
    parser = argparse.ArgumentParser()
    parser.add_argument('--network', '-n', action='store_true')
    parser.add_argument('--build', '-b', nargs=1, choices=['dev'])
    parser.add_argument('--migrations', '-m', action='store_true')
    parser.add_argument('--temp', '-t', action='store_true')
    parser.add_argument('--action', '-a', action='store_true')
    return parser.parse_args()


if __name__ == '__main__':
    args = argparse_init()
    if args.network:
        create_network()
    elif args.build:
        run_build(args.build[0])
    elif args.migrations:
        apply_migrations()
    elif args.temp:
        run_temp_functions()
    elif args.action:
        run_tests()
