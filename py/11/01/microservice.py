from nameko.rpc import rpc

class SimpleMicroService:
    name = "simple_ms"

    @rpc
    def hello(self, who):
        print("got a hello")
        return "Hi " + who + "!"
