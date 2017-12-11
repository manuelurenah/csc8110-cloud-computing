from optparse import OptionParser

parser = OptionParser()
parser.add_option('-u', action='store', dest='url')
parser.add_option('-c', action='store', dest='concurrent_calls', type='int')
parser.add_option('-i', action='store', dest='interval', type='int')
parser.add_option('-l', action='store', dest='iterations', type='int')
parser.add_option('-s', action='store_true', dest='start_service', default=False)
parser.add_option('-g', action='store_true', dest='start_load_generator', default=False)
parser.add_option('-p', action="store_true", dest="persist_benchmarks", default=False)
parser.add_option('-n', action='store', dest='collection_name')

def parse(args):
    return parser.parse_args(args)
