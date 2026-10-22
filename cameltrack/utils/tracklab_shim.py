"""Stand-ins for the tracklab names cameltrack.py needs when tracklab is not installed. Tracking only uses the
base class constructor; the module is then driven directly (preprocess / process per frame) instead of by
tracklab's engine."""


class ImageLevelModule:
    def __init__(self, batch_size):
        self.batch_size = batch_size


class TrackingDataset:
    pass
