# helloworld.py
from nameko.containers import ServiceContainer
from nameko.rpc import rpc
import time
import eventlet
import signal
import errno

class GreetingService:
    name = "greeting_service"

    @rpc
    def hello(self, name):
        print("Got a request: " + name)
        time.sleep(5)
        print("Now replying...")
        return "Hello, {}!".format(name)

print("HI")
if __name__ == "__main__":

    eventlet.monkey_patch()  # noqa (code before rest of imports)

    print("in main")
    # create a container
    config = {
        'AMQP_URI': "amqp://guest:guest@localhost"
    }

    container = ServiceContainer(GreetingService, config=config)

    # ``container.extensions`` exposes all extensions used by the service
    service_extensions = list(container.extensions)

    print("starting service")
    # start service
    container.start()

    print("service running")

    def shutdown(signum, frame):
        # signal handlers are run by the MAINLOOP and cannot use eventlet
        # primitives, so we have to call `stop` in a greenlet
        eventlet.spawn_n(container.stop)

    signal.signal(signal.SIGTERM, shutdown)

    runnlet = eventlet.spawn(container.wait)

    while True:
        try:
            runnlet.wait()
        except OSError as exc:
            if exc.errno == errno.EINTR:
                # this is the OSError(4) caused by the signalhandler.
                # ignore and go back to waiting on the runner
                continue
            raise
        except KeyboardInterrupt:
            print()  # looks nicer with the ^C e.g. bash prints in the terminal
            try:
                container.stop()
            except KeyboardInterrupt:
                print()  # as above
                container.kill()
        else:
            # runner.wait completed
            break
