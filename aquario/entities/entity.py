class Entity:
    def update(self, delta_time):
        raise NotImplementedError

    def draw(self, canvas):
        raise NotImplementedError