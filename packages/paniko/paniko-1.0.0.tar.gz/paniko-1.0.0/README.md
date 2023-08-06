# Paniko

Paniko is a Python wrapper for Google's [Kaniko](https://github.com/GoogleContainerTools/kaniko). Kaniko is a command line utility that enables the building of container images within environments that can't easily or securely run a Docker daemon. This includes building images within a Kubernetes Pod or serverless infrastructure such as AWS's Fargate. 

It includes the most updated Kaniko commands and streaming of Kaniko's outputs.  

This package builds off of Timofey's pykaniko package. 

---

## Install
For installation kaniko add in your Dockerfile the next lines

```bash
pip install git+https://github.com/wfclark5/paniko.git
```


```
#Dockerfile
FROM gcr.io/kaniko-project/executor:v0.12.0 AS kaniko

FROM <your docker repo>

ENV DOCKER_CONFIG /kaniko/.docker

COPY --from=kaniko /kaniko /kaniko
...
```

## Usage


```python
from paniko import Kaniko, KanikoSnapshotMode

kaniko = Kaniko()
build_logs = kaniko.build(
    docker_registry_uri='https://index.docker.io/v1/',
    registry_username='username',
    registry_password='password',
    destination='path-to-repo:tag',
    dockerfile='/path/to/Dockerfile',
    force=True,
    snapshot_mode=KanikoSnapshotMode.full,
)
```