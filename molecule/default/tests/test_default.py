import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_nginx_service(host):
    assert host.service("nginx-podman").is_running
    assert host.service("nginx-podman").is_enabled


def test_nginx_listening(host):
    assert host.socket("tcp://0.0.0.0:80").is_listening


def test_serve_static_page(host):
    assert host.check_output("curl http://localhost") == "Hello World"
