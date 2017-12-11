import sys
from lib import multiservice, options, loadgenerator, apiconsumer

if __name__ == '__main__':
    opts, args = options.parse(sys.argv[1:])

    if opts.start_service:
        multiservice.initiate_container()
        multiservice.initiate_swarm()

    if opts.start_load_generator:
        loadgenerator.load_server(
            opts.url,
            opts.concurrent_calls,
            opts.interval,
            opts.iterations
        )

    if opts.persist_benchmarks:
        data = apiconsumer.fetch_benchmarks(opts.url)

        apiconsumer.insert(data, opts.collection_name)
