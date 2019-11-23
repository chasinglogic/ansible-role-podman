Ansible role for podman
==================================

Manage services and containers with podman

[![CircleCI](https://img.shields.io/circleci/build/github/chasinglogic/ansible-role-podman/master?style=flat-square)](https://circleci.com/gh/chasinglogic/ansible-role-podman)

Usage
-----

By default this role will simply install podman and perform any other required
setup to make the installation functional on the supported platforms. 

Additionally, it can deploy and configure podman containers as SystemD services.

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: podman
```


Automatic Service Deployment
----------------------------

Podman containers meant to run as services are relatively
homogeneous. For this reason this role provides a variable which can
be used to deploy and configure containers as SystemD services. More
complex use cases like configure multiple containers as a pod are not
yet supported. To use this feature for your host define a variable
`podman_services` which is a list of maps that have the following
structure:

```yaml
podman_services:
    ## Podman Variables
    #
    # Required: The image name to download
  - image_name: nginx
    # Optional: The tag to download. This often corresponds to
    # version, defaults to 'latest'
    image_tag: mainline
    # Optional: Description that will be added to the SystemD service file
    description: Web host
    # Optional: List of ports to publish. Takes the same form as the
    # podman CLI that is to say: host-port:container-port. This is
    # just piped directly to the '--publish' flag so binding IPs work
    # as well (ex. '127.0.0.1:8080:80'). Defaults to none.
    publish:
      - '80:80'
    # Optional: List of volumes to mount. Takes the same form as the
    # podman CLI host-directory:container-directory and as shown below
    # mount options are allowed.
    volumes:
      - '/tmp:/usr/share/nginx/html:ro'
    # Optional: Define a hostname for podman's hostname flag. Set's
    # the containers hostname, default is none.
    hostname: chasinglogic.io
    # Optional: A list of environment variables to add to the
    # container.  Default is none.
    env_vars:
      - SOME_VAR=SOME_VALUE

    ## SystemD Variables
    #
    # Optional: Define the restart policy for this service. Default is always
    restart: always
    # Optional: Define the time to wait between restarts of this service in seconds. Default is 30
    restart_sec: 30
    # Optional: Define the actual name used for the SystemD
    # service. {{ Defaults to image_name + '-podman' }}
    service_name: nginx
    # Optional: Define the targets / services this SystemD service
    # must start after. This is a YAML list not a string.
    after:
      - network.target
    # Optional: Define the timeout for starting this SystemD
    # service. For valid values see 'man systemd.service'. Defaults to
    # 5 minutes.
    timeout_start_sec: 5m
    # Optional: Define an install section for the SystemD
    # service. Currently only wanted_by is supported. See 'man
    # systemd.unit' for a description of this section. Default is none
    # and most users should not need this.
    install:
      wanted_by:
        - multi-user.target
    # Optional: define the user and group for the service
    # file. Default is omission which is equivalent to root on most
    # systems.
    user: root
    group: root
```

Development
-----------

When developing it is best to use the converge and verify stages like so:

```
make converge verify
```



License
-------

[MIT](LICENSE)
