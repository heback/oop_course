class File:
    def read(self):
        return "Reading from a file"


class NetworkStream:
    def read(self):
        return "Reading from a network stream"


def process_data(source):
    data = source.read()
    print(data)


file = File()
stream = NetworkStream()

process_data(file)    # Output: Reading from a file
process_data(stream)  # Output: Reading from a network stream

