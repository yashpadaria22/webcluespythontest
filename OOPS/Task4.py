class Event:
    def __init__(self, name):
        self.name = name
        self.listeners = []

    def add_listener(self, listener):
        self.listeners.append(listener)

    def notify_listeners(self, data=None):
        print(f"Event '{self.name}' occurred!")
        for listener in self.listeners:
            listener.handle_event(data)


class Listener:
    def __init__(self, name):
        self.name = name

    def handle_event(self, data=None):
        print(f"{self.name} received event with data: {data}")


# Example usage:
if __name__ == "__main__":
    # Creating events
    event1 = Event("Hello good morning")
    event2 = Event("BYE good night")

    # Creating listeners
    listener1 = Listener("yash")
    listener2 = Listener("priyank")

    # Registering listeners for specific events
    event1.add_listener(listener1)
    event2.add_listener(listener1)
    event2.add_listener(listener2)

    # Triggering events
    event1.notify_listeners({"yash": "hiii"})
    event2.notify_listeners()

