class MugInvalidContentTypeError(Exception):
    pass


class MugOverflowError(Exception):
    pass


class MugNegativeContentAmountError(Exception):
    pass


class Mug:
    def __init__(self, color: str, capacity: float) -> None:
        self.color = color
        self.capacity = capacity
        self.content_amount = 0.0
        self.content_type = None

    def get_content_type(self):
        return self.content_type

    def get_content_amount(self):
        return self.content_amount

    def fill(self, content_type: str, content_amount: float):
        if content_type != self.content_type and self.content_type != None:
            raise MugInvalidContentTypeError()

        if content_amount < 0:
            raise MugNegativeContentAmountError()

        new_content_amount = self.content_amount + content_amount
        self.content_type = content_type

        if new_content_amount > self.capacity:
            self.content_amount = self.capacity
            raise MugOverflowError()

        self.content_amount = new_content_amount

    def pour_out_liquid(self, requested_amount: float) -> tuple[str, float]:
        original_amount = self.content_amount
        self.content_amount = max(self.content_amount - requested_amount, 0)

        if self.content_amount == 0:
            self.content_type = None

        return [self.content_type, float(min(requested_amount, original_amount))]


# mug = Mug(color="blue", capacity=10, content_type="tea")

# mug.fill("cola", 5)
# mug.fill("tea", -5)
# mug.fill("tea", 5)
# print(mug.pour_out_liquid(2))
# print(mug.pour_out_liquid(20))
# print(mug.pour_out_liquid(20))
