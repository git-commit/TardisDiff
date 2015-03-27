from plugnplay import Plugin
from TardisUtil import TimeSubmitter


class ExamplePlugin(Plugin):
    implements = [TimeSubmitter]

    def submit_time(self, duration):
        print("Time submitted: %f" % duration)
