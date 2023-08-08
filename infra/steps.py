from difido.report_manager import Report


class Step(object):

    def __init__(self, description):
        self.description = description
        self.__report = Report()

    def __enter__(self):
        self.__report.start_level(f"{type(self).__name__} {self.description}")

    def __exit__(self, ex_type, value, traceback):
        self.__report.stop_level()


class And(Step):
    pass


class Given(Step):
    pass


class When(Step):
    pass


class Then(Step):
    pass
