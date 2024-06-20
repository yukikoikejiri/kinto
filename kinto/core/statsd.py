import types
from urllib.parse import urlparse

from pyramid.exceptions import ConfigurationError

from kinto.core import utils


try:
    import statsd as statsd_module
except ImportError:  # pragma: no cover
    statsd_module = None
#BRANCH ID
coverage_data_count = {
    "branch 21": 0, "branch 22": 0
    }
total_branches= len(coverage_data_count)

coverage_data_statsd_count = {
    "branch 31": 0, "branch 32": 0
    }
total_branches_statsd_count= len(coverage_data_statsd_count)

class Client:
    def __init__(self, host, port, prefix):
        self._client = statsd_module.StatsClient(host, port, prefix=prefix)

    def watch_execution_time(self, obj, prefix="", classname=None):
        classname = classname or utils.classname(obj)
        members = dir(obj)
        for name in members:
            value = getattr(obj, name)
            is_method = isinstance(value, types.MethodType)
            if not name.startswith("_") and is_method:
                statsd_key = f"{prefix}.{classname}.{name}"
                decorated_method = self.timer(statsd_key)(value)
                setattr(obj, name, decorated_method)

    def timer(self, key):
        return self._client.timer(key)
        
    #FUNCTION TO BE INSTRUMENTED
    def count(self, key, count=1, unique=None):
        print(f"count method called with key={key}, count={count}, unique={unique}")  # Debugging print statement
        if unique is None:
            coverage_data_count["branch 21"] +=1
            return self._client.incr(key, count=count)
        else:
            coverage_data_count["branch 22"] +=1
            return self._client.set(key, unique)


# Function to print coverage data for count
def print_coverage_data_count():
    print("Branch Coverage Report for function count:")
    print(f"Number of Branches: {total_branches}")
    total_executed = sum(1 for count in coverage_data_count.values() if count > 0)
    for branch, count in coverage_data_count.items():
        print(f"{branch.replace('_', ' ').capitalize()}: executed {count} time(s)")
    coverage_percentage = (total_executed / total_branches) * 100
    print(f"Total Coverage: {coverage_percentage:.2f}%")

# Added a call to print coverage data at the end of the program
atexit.register(print_coverage_data_count)


#SECOND FUNCTION TO BE INSTRUMENTED
def statsd_count(request, count_key):
    statsd = request.registry.statsd
    if statsd:
        coverage_data_statsd_count["branch 31"] +=1
        statsd.count(count_key)
    else:
        coverage_data_statsd_count["branch 32"] +=1

# Function to print coverage data for statsd_count
def print_coverage_data_statsd_count():
    print("Branch Coverage Report for function statsd_count:")
    print(f"Number of Branches: {total_branches_statsd_count}")
    total_executed = sum(1 for count in coverage_data_statsd_count.values() if count > 0)
    for branch, count in coverage_data_statsd_count.items():
        print(f"{branch.replace('_', ' ').capitalize()}: executed {count} time(s)")
    coverage_percentage = (total_executed / total_branches_statsd_count) * 100
    print(f"Total Coverage: {coverage_percentage:.2f}%")

atexit.register(print_coverage_data_statsd_count)


def load_from_config(config):
    # If this is called, it means that a ``statsd_url`` was specified in settings.
    # (see ``kinto.core.initialization``)
    # Raise a proper error if the ``statsd`` module is not installed.
    if statsd_module is None:
        error_msg = "Please install Kinto with monitoring dependencies (e.g. statsd package)"
        raise ConfigurationError(error_msg)

    settings = config.get_settings()
    uri = settings["statsd_url"]
    uri = urlparse(uri)

    if settings["project_name"] != "":
        prefix = settings["project_name"]
    else:
        prefix = settings["statsd_prefix"]

    return Client(uri.hostname, uri.port, prefix)
