"""spacex tap class."""

from typing import List

from singer_sdk import Tap, Stream

from singer_sdk import typing as th  # JSON schema typing helpers

from tap_spacex.streams import LaunchesStream, RocketsStream, CapsulesStream, CoresStream, CrewStream, DragonsStream, LandpadsStream, LaunchpadsStream, PayloadsStream, ShipsStream, StarlinkStream

STREAM_TYPES = [
    LaunchesStream, 
    RocketsStream, 
    CapsulesStream, 
    CoresStream, 
    CrewStream, 
    DragonsStream, 
    LandpadsStream, 
    LaunchpadsStream, 
    PayloadsStream, 
    ShipsStream, 
    StarlinkStream
]

class Tapspacex(Tap):
    """spacex tap class."""

    name = "tap-spacex"

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""

        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    Tapspacex.cli()
