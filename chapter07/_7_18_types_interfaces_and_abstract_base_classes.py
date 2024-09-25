from abc import ABC, abstractmethod


class Stream(ABC):
    @abstractmethod
    def receive(self):
        print(f"Invoked {Stream.receive.__qualname__}.")

    @abstractmethod
    def send(self, msg):
        pass

    @abstractmethod
    def close(self):
        pass


class SocketStream(Stream):
    def receive(self):
        print(f"Invoked {SocketStream.receive.__qualname__}.")
        super().receive()

    def send(self, msg):
        print(f"Invoked {SocketStream.send.__qualname__}.")

    def close(self):
        print(f"Invoked {SocketStream.close.__qualname__}.")


s = SocketStream()
s.receive()
s.send("Some value")
s.close()

print(isinstance(s, Stream))  # True
print(issubclass(SocketStream, Stream))  # True
