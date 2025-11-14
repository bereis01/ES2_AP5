class CumulativeCalculator:
    def __init__(self):
        self._number = None
        self._history = []
        pass

    def history(self):
        return self._history

    def result(self):
        return self._number

    def clear(self):
        # Does nothing if history is empty
        if not self._history:
            return

        # Undos the last operation
        self._number = self._history.pop()

    def reset(self):
        # Clears all internal data structures
        self._number = None
        self._history = []

    def _update(self, result):
        self._history.append(self._number)
        self._number = result

    def sum(self, num):
        # If is first operation
        if self._number == None:
            self._number = num
            return

        result = self._number + num
        self._update(result)

    def sub(self, num):
        # If is first operation
        if self._number == None:
            self._number = -num
            return

        result = self._number - num
        self._update(result)

    def mul(self, num):
        # If is first operation
        if self._number == None:
            self._number = 1 * num
            return

        result = self._number * num
        self._update(result)

    def div(self, num):
        # If is first operation
        if self._number == None:
            self._number = 1 / num
            return

        result = self._number / num
        self._update(result)
