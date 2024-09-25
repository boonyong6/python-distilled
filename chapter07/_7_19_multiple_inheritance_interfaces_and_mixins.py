# Use case of multiple inheritance: To define mixin classes.
#   A mixin class is a class that modifies or extends the functionality of
#   other classes.
# Shared commonality: noise()
class Duck:
    def noise(self):
        return "Quack"

    def waddle(self):
        return "Waddle"
    
    def __repr__(self):
        return f"{type(self).__name__}()"


class Trombonist:
    def noise(self):
        return "Blat!"

    def march(self):
        return "Clomp"
    
    def __repr__(self):
        return f"{type(self).__name__}()"


class Cyclist:
    def noise(self):
        return "On your left!"

    def pedal(self):
        return "Pedaling"
    
    def __repr__(self):
        return f"{type(self).__name__}()"


class LoudMixin:
    def noise(self):
        return super().noise().upper()  # type: ignore


class AnnoyingMixin:
    def noise(self):
        return 3 * super().noise()  # type: ignore


# a = AnnoyingMixin()
# a.noise()  # Raise AttributeError: 'super' object has no attribute 'noise'


class LoudDuck(LoudMixin, Duck):
    pass


class AnnoyingTrombonist(AnnoyingMixin, Trombonist):
    pass


# Guideline 1: It's common for mixins (AnnoyingMixin, LoudMixin) to share
#   a common parent (Cyclist) which provides a default implementation
#   of methods, such as noise().
#
# Guideline 2: All implementations of a mixin method, such as noise(),
#   should have an identical/compatible function signature.
class AnnoyingLoudCyclist(AnnoyingMixin, LoudMixin, Cyclist):
    pass


if __name__ == "__main__":
    d = LoudDuck()
    print(d.noise())

    t = AnnoyingTrombonist()
    print(t.noise())

    c = AnnoyingLoudCyclist()
    print(c.noise())

    print(AnnoyingLoudCyclist.__mro__)  # mro - method resolution order
