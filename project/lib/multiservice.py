import docker
from docker.types import EndpointSpec, ServiceMode, Mount

client = docker.from_env()

def initiate_container():
    mount_volumes = []

    mount_volumes.append(Mount(target='/rootfs', source="/", type='bind', read_only=True))
    mount_volumes.append(Mount(target='/var/run', source="/var/run", type='bind'))
    mount_volumes.append(Mount(target='/sys', source="/sys", type='bind', read_only=True))
    mount_volumes.append(Mount(target='/var/lib/docker', source="/var/lib/docker", type='bind', read_only=True))

    cadvisor = client.images.pull('google/cadvisor')
    container_cadvisor = client.containers.run(
        cadvisor.id,
        detach=True,
        mounts=mount_volumes,
        ports={'8080/tcp': 8080}
    )

    print('Container ' + container_cadvisor.id + ' running on port 8080')

def initiate_swarm():
    client.swarm.init()
    print('Swarm initiated...')

    benchmark = client.services.create(
        'nclcloudcomputing/javabenchmarkapp:latest',
        endpoint_spec=EndpointSpec(mode='vip', ports={4000: 8080}),
        mode=ServiceMode(mode='replicated', replicas=2),
        name='benchmarkapp',
    )
    print ('Benchmark service initialized with id ' + benchmark.id)

    visualizer = client.services.create(
        'dockersamples/visualizer',
        endpoint_spec=EndpointSpec(mode='vip', ports={5000: 8080}),
        mounts=['/var/run/docker.sock:/var/run/docker.sock'],
        name='visualizer',
    )
    print ('Visualizer service initialized with id ' + visualizer.id)

    mongo = client.services.create(
        'mongo',
        endpoint_spec=EndpointSpec(mode='vip', ports={27017: 27017}),
        mounts=['db:/data/db'],
        name='db',
    )
    print ('Mongo service initialized with id ' + mongo.id)
