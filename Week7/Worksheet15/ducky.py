class ducky:
    def sum_iter_value(iterable):
        total = 0
        if not isinstance(iterable, list):
            if isinstance(iterable, str):
                iterable = iterable.strip()
                iterable = iterable.replace(' ', ',')
                iterable = iterable.split(',')
        for value in iterable:
            if isinstance(value, int) or isinstance(value, float):
                total += value
            elif isinstance(value, str):
                try:
                    total += float(value)
                except ValueError:
                    continue
        return total
