def receiver():
    print("Ready to receive")
    while True:
        try:
            n = yield
            print("Got", n)
        except RuntimeError:
            print("Handling runtime error...")
        except GeneratorExit:
            print("Performing cleanup...")
            return

enh_gen = receiver()

# Required for initializing the enhanced generator.
# <generator>.send(None) executes statements in the generator function and pauses at the yield expression, waiting to get the value sent by the next <generator>.send(<obj>).
enh_gen.send(None)

enh_gen.send(1)
enh_gen.send(2)
enh_gen.send("Hello")

enh_gen.throw(RuntimeError, "Dead")

enh_gen.close()  # To shut down the generator.
enh_gen.send(4)  # Raise StopIteration exception.
