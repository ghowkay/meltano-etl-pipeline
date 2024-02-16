"""Stream type classes for tap-spacex."""

from __future__ import annotations

import typing as t
from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_spacex.client import spacexStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.

class CapsulesStream(spacexStream):
    name = "capsules"
    path = "/capsules"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("serial", th.StringType),
        th.Property("status", th.StringType),
        th.Property("type", th.StringType),
        th.Property("reuse_count", th.IntegerType),
        th.Property("water_landings", th.IntegerType),
        th.Property("land_landings", th.IntegerType),
        th.Property("last_update", th.StringType),
        th.Property("launches", th.ArrayType(
            th.StringType  # Assuming launches are represented by strings (IDs)
        ))
    ).to_dict()

class CoresStream(spacexStream):
    name = "cores"
    path = "/cores"  # API endpoint path
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("serial", th.StringType),
        th.Property("status", th.StringType),
        th.Property("block", th.IntegerType),
        th.Property("reuse_count", th.IntegerType),
        th.Property("rtls_attempts", th.IntegerType),
        th.Property("rtls_landings", th.IntegerType),
        th.Property("asds_attempts", th.IntegerType),
        th.Property("asds_landings", th.IntegerType),
        th.Property("last_update", th.StringType),
        th.Property("launches", th.ArrayType(
            th.StringType  # Assuming launches are represented by strings (IDs)
        ))
    ).to_dict()

    schema["required"] = ["id", "serial", "status", "reuse_count", "rtls_attempts", "rtls_landings", "asds_attempts", "asds_landings", "last_update", "launches"]

class CrewStream(spacexStream):
    name = "crew"
    path = "/crew"  # API endpoint path
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("agency", th.StringType),
        th.Property("image", th.StringType),
        th.Property("wikipedia", th.StringType),
        th.Property("launches", th.ArrayType(
            th.StringType  # Assuming launches are represented by strings (IDs)
        )),
        th.Property("status", th.StringType)
    ).to_dict()

class DragonsStream(spacexStream):
    name = "dragons"
    path = "/dragons"  # API endpoint path
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("type", th.StringType),
        th.Property("active", th.BooleanType),
        th.Property("crew_capacity", th.IntegerType),
        th.Property("sidewall_angle_deg", th.IntegerType),
        th.Property("orbit_duration_yr", th.IntegerType),
        th.Property("dry_mass_kg", th.IntegerType),
        th.Property("dry_mass_lb", th.IntegerType),
        th.Property("first_flight", th.StringType),
        th.Property("wikipedia", th.StringType),
        th.Property("description", th.StringType),
        th.Property("flickr_images", th.ArrayType(th.StringType)),
        th.Property("heat_shield", th.ObjectType(
            th.Property("material", th.StringType),
            th.Property("size_meters", th.NumberType),
            th.Property("temp_degrees", th.IntegerType),
            th.Property("dev_partner", th.StringType)
        )),
        th.Property("launch_payload_mass", th.ObjectType(
            th.Property("kg", th.IntegerType),
            th.Property("lb", th.IntegerType)
        )),
        th.Property("launch_payload_vol", th.ObjectType(
            th.Property("cubic_meters", th.IntegerType),
            th.Property("cubic_feet", th.IntegerType)
        )),
        th.Property("return_payload_mass", th.ObjectType(
            th.Property("kg", th.IntegerType),
            th.Property("lb", th.IntegerType)
        )),
        th.Property("return_payload_vol", th.ObjectType(
            th.Property("cubic_meters", th.IntegerType),
            th.Property("cubic_feet", th.IntegerType)
        )),
        th.Property("pressurized_capsule", th.ObjectType(
            th.Property("payload_volume", th.ObjectType(
                th.Property("cubic_meters", th.IntegerType),
                th.Property("cubic_feet", th.IntegerType)
            ))
        )),
        th.Property("trunk", th.ObjectType(
            th.Property("trunk_volume", th.ObjectType(
                th.Property("cubic_meters", th.IntegerType),
                th.Property("cubic_feet", th.IntegerType)
            )),
            th.Property("cargo", th.ObjectType(
                th.Property("solar_array", th.IntegerType),
                th.Property("unpressurized_cargo", th.BooleanType)
            ))
        )),
        th.Property("height_w_trunk", th.ObjectType(
            th.Property("meters", th.NumberType),
            th.Property("feet", th.NumberType)
        )),
        th.Property("diameter", th.ObjectType(
            th.Property("meters", th.NumberType),
            th.Property("feet", th.NumberType)
        )),
        th.Property("thrusters", th.ArrayType(
            th.ObjectType(
                th.Property("type", th.StringType),
                th.Property("amount", th.IntegerType),
                th.Property("pods", th.IntegerType),
                th.Property("fuel_1", th.StringType),
                th.Property("fuel_2", th.StringType),
                th.Property("isp", th.IntegerType),
                th.Property("thrust", th.ObjectType(
                    th.Property("kN", th.NumberType),
                    th.Property("lbf", th.NumberType)
                ))
            )
        ))
    ).to_dict()

class LandpadsStream(spacexStream):  # Inheriting from SpaceXStream
    name = "landpads"
    path = "/landpads"  # API endpoint path
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("full_name", th.StringType),
        th.Property("status", th.StringType),
        th.Property("type", th.StringType),
        th.Property("locality", th.StringType),
        th.Property("region", th.StringType),
        th.Property("latitude", th.NumberType),
        th.Property("longitude", th.NumberType),
        th.Property("landing_attempts", th.IntegerType),
        th.Property("landing_successes", th.IntegerType),
        th.Property("wikipedia", th.StringType),
        th.Property("details", th.StringType),
        th.Property("launches", th.ArrayType(th.StringType)),
        th.Property("images", th.ObjectType(
            th.Property("large", th.ArrayType(th.StringType))
        ))
    ).to_dict()


class LaunchesStream(spacexStream):  # Inheriting from spacexStream
    name = "launches"
    path = "/launches"  # API endpoint path
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("flight_number", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("date_utc", th.StringType),
        th.Property("date_unix", th.IntegerType),
        th.Property("date_local", th.StringType),
        th.Property("date_precision", th.StringType),
        th.Property("upcoming", th.BooleanType),
        th.Property("static_fire_date_utc", th.StringType),
        th.Property("static_fire_date_unix", th.IntegerType),
        th.Property("net", th.BooleanType),
        th.Property("window", th.IntegerType),
        th.Property("rocket", th.StringType),
        th.Property("success", th.BooleanType),
        th.Property("details", th.StringType),
        th.Property("crew", th.ArrayType(th.StringType)),
        th.Property("ships", th.ArrayType(th.StringType)),
        th.Property("capsules", th.ArrayType(th.StringType)),
        th.Property("payloads", th.ArrayType(th.StringType)),
        th.Property("launchpad", th.StringType),
        th.Property("auto_update", th.BooleanType),
        th.Property("tbd", th.BooleanType),
        th.Property("launch_library_id", th.StringType),
        th.Property("fairings", th.ObjectType(
            th.Property("reused", th.BooleanType),
            th.Property("recovery_attempt", th.BooleanType),
            th.Property("recovered", th.BooleanType),
            th.Property("ships", th.ArrayType(th.StringType))
        )),
        th.Property("links", th.ObjectType(
            th.Property("patch", th.ObjectType(
                th.Property("small", th.StringType),
                th.Property("large", th.StringType)
            )),
            th.Property("reddit", th.ObjectType(
                th.Property("campaign", th.StringType),
                th.Property("launch", th.StringType),
                th.Property("media", th.StringType),
                th.Property("recovery", th.StringType)
            )),
            th.Property("flickr", th.ObjectType(
                th.Property("small", th.ArrayType(th.StringType)),
                th.Property("original", th.ArrayType(th.StringType))
            )),
            th.Property("presskit", th.StringType),
            th.Property("webcast", th.StringType),
            th.Property("youtube_id", th.StringType),
            th.Property("article", th.StringType),
            th.Property("wikipedia", th.StringType)
        )),
        th.Property("failures", th.ArrayType(
            th.ObjectType(
                th.Property("time", th.IntegerType),
                th.Property("altitude", th.IntegerType),
                th.Property("reason", th.StringType)
            )
        )),
        th.Property("cores", th.ArrayType(
            th.ObjectType(
                th.Property("core", th.StringType),
                th.Property("flight", th.IntegerType),
                th.Property("gridfins", th.BooleanType),
                th.Property("legs", th.BooleanType),
                th.Property("reused", th.BooleanType),
                th.Property("landing_attempt", th.BooleanType),
                th.Property("landing_success", th.BooleanType),
                th.Property("landing_type", th.StringType),
                th.Property("landpad", th.StringType)
            )
        ))
    ).to_dict()


class LaunchpadsStream(spacexStream):  # Inheriting from spacexStream
    name = "launchpads"
    path = "/launchpads"  # API endpoint path
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("full_name", th.StringType),
        th.Property("locality", th.StringType),
        th.Property("region", th.StringType),
        th.Property("latitude", th.NumberType),
        th.Property("longitude", th.NumberType),
        th.Property("launch_attempts", th.IntegerType),
        th.Property("launch_successes", th.IntegerType),
        th.Property("rockets", th.ArrayType(th.StringType)),
        th.Property("timezone", th.StringType),
        th.Property("launches", th.ArrayType(th.StringType)),
        th.Property("status", th.StringType),
        th.Property("details", th.StringType),
        th.Property("images", th.ObjectType(
            th.Property("large", th.ArrayType(th.StringType))
        ))
    ).to_dict()


class PayloadsStream(spacexStream):  # Inheriting from spacexStream
    name = "payloads"
    path = "/payloads"  # API endpoint path
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("type", th.StringType),
        th.Property("reused", th.BooleanType),
        th.Property("launch", th.StringType),
        th.Property("customers", th.ArrayType(th.StringType)),
        th.Property("norad_ids", th.ArrayType(th.IntegerType)),
        th.Property("nationalities", th.ArrayType(th.StringType)),
        th.Property("manufacturers", th.ArrayType(th.StringType)),
        th.Property("mass_kg", th.NumberType),
        th.Property("mass_lbs", th.NumberType),
        th.Property("orbit", th.StringType),
        th.Property("reference_system", th.StringType),
        th.Property("regime", th.StringType),
        th.Property("longitude", th.NumberType),
        th.Property("semi_major_axis_km", th.NumberType),
        th.Property("eccentricity", th.NumberType),
        th.Property("periapsis_km", th.NumberType),
        th.Property("apoapsis_km", th.NumberType),
        th.Property("inclination_deg", th.NumberType),
        th.Property("period_min", th.NumberType),
        th.Property("lifespan_years", th.NumberType),
        th.Property("epoch", th.StringType),
        th.Property("mean_motion", th.NumberType),
        th.Property("raan", th.NumberType),
        th.Property("arg_of_pericenter", th.NumberType),
        th.Property("mean_anomaly", th.NumberType),
        th.Property("dragon", th.ObjectType(
            th.Property("capsule", th.StringType),
            th.Property("mass_returned_kg", th.NumberType),
            th.Property("mass_returned_lbs", th.NumberType),
            th.Property("flight_time_sec", th.IntegerType),
            th.Property("manifest", th.StringType),
            th.Property("water_landing", th.BooleanType),
            th.Property("land_landing", th.BooleanType)
        ))
    ).to_dict()

    
class RocketsStream(spacexStream):  # Inheriting from spacexStream
    name = "rockets"
    path = "/rockets"  # API endpoint path
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("type", th.StringType),
        th.Property("active", th.BooleanType),
        th.Property("stages", th.IntegerType),
        th.Property("boosters", th.IntegerType),
        th.Property("cost_per_launch", th.IntegerType),
        th.Property("success_rate_pct", th.IntegerType),
        th.Property("first_flight", th.StringType),
        th.Property("country", th.StringType),
        th.Property("company", th.StringType),
        th.Property("wikipedia", th.StringType),
        th.Property("description", th.StringType),
        th.Property("height", th.ObjectType(
            th.Property("meters", th.NumberType),
            th.Property("feet", th.NumberType)
        )),
        th.Property("diameter", th.ObjectType(
            th.Property("meters", th.NumberType),
            th.Property("feet", th.NumberType)
        )),
        th.Property("mass", th.ObjectType(
            th.Property("kg", th.IntegerType),
            th.Property("lb", th.IntegerType)
        )),
        th.Property("first_stage", th.ObjectType(
            th.Property("thrust_sea_level", th.ObjectType(
                th.Property("kN", th.NumberType),
                th.Property("lbf", th.NumberType)
            )),
            th.Property("thrust_vacuum", th.ObjectType(
                th.Property("kN", th.NumberType),
                th.Property("lbf", th.NumberType)
            )),
            th.Property("reusable", th.BooleanType),
            th.Property("engines", th.IntegerType),
            th.Property("fuel_amount_tons", th.NumberType),
            th.Property("burn_time_sec", th.IntegerType)
        )),
        th.Property("second_stage", th.ObjectType(
            th.Property("thrust", th.ObjectType(
                th.Property("kN", th.NumberType),
                th.Property("lbf", th.NumberType)
            )),
            th.Property("payloads", th.ObjectType(
                th.Property("composite_fairing", th.ObjectType(
                    th.Property("height", th.ObjectType(
                        th.Property("meters", th.NumberType),
                        th.Property("feet", th.NumberType)
                    )),
                    th.Property("diameter", th.ObjectType(
                        th.Property("meters", th.NumberType),
                        th.Property("feet", th.NumberType)
                    ))
                )),
                th.Property("option_1", th.StringType)
            )),
            th.Property("reusable", th.BooleanType),
            th.Property("engines", th.IntegerType),
            th.Property("fuel_amount_tons", th.NumberType),
            th.Property("burn_time_sec", th.IntegerType)
        )),
        th.Property("engines", th.ObjectType(
            th.Property("isp", th.ObjectType(
                th.Property("sea_level", th.IntegerType),
                th.Property("vacuum", th.IntegerType)
            )),
            th.Property("thrust_sea_level", th.ObjectType(
                th.Property("kN", th.NumberType),
                th.Property("lbf", th.NumberType)
            )),
            th.Property("thrust_vacuum", th.ObjectType(
                th.Property("kN", th.NumberType),
                th.Property("lbf", th.NumberType)
            )),
            th.Property("number", th.IntegerType),
            th.Property("type", th.StringType),
            th.Property("version", th.StringType),
            th.Property("layout", th.StringType),
            th.Property("engine_loss_max", th.IntegerType),
            th.Property("propellant_1", th.StringType),
            th.Property("propellant_2", th.StringType),
            th.Property("thrust_to_weight", th.NumberType)
        )),
        th.Property("landing_legs", th.ObjectType(
            th.Property("number", th.IntegerType),
            th.Property("material", th.StringType)
        )),
        th.Property("payload_weights", th.ArrayType(
            th.ObjectType(
                th.Property("id", th.StringType),
                th.Property("name", th.StringType),
                th.Property("kg", th.IntegerType),
                th.Property("lb", th.IntegerType)
            )
        )),
        th.Property("flickr_images", th.ArrayType(th.StringType))
    ).to_dict()


class ShipsStream(spacexStream):  # Inheriting from spacexStream
    name = "ships"
    path = "/ships"  # API endpoint path
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("type", th.StringType),
        th.Property("active", th.BooleanType),
        th.Property("imo", th.IntegerType),
        th.Property("mmsi", th.IntegerType),
        th.Property("abs", th.IntegerType),
        th.Property("class", th.IntegerType),
        th.Property("mass_kg", th.NumberType),
        th.Property("mass_lbs", th.NumberType),
        th.Property("year_built", th.IntegerType),
        th.Property("home_port", th.StringType),
        th.Property("status", th.StringType),
        th.Property("speed_kn", th.NumberType),
        th.Property("course_deg", th.NumberType),
        th.Property("latitude", th.NumberType),
        th.Property("longitude", th.NumberType),
        th.Property("link", th.StringType),
        th.Property("image", th.StringType),
        th.Property("last_ais_update", th.StringType),
        th.Property("legacy_id", th.StringType),
        th.Property("model", th.StringType),
        th.Property("roles", th.ArrayType(th.StringType)),
        th.Property("launches", th.ArrayType(th.StringType))
    ).to_dict()

class StarlinkStream(spacexStream):  # Inheriting from spacexStream
    name = "starlink"
    path = "/starlink"  # API endpoint path
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("launch", th.StringType),
        th.Property("version", th.StringType),
        th.Property("height_km", th.NumberType),
        th.Property("latitude", th.NumberType),
        th.Property("longitude", th.NumberType),
        th.Property("velocity_kms", th.NumberType),
        th.Property("spaceTrack", th.ObjectType(
            th.Property("CCSDS_OMM_VERS", th.StringType),
            th.Property("COMMENT", th.StringType),
            th.Property("CREATION_DATE", th.StringType),
            th.Property("ORIGINATOR", th.StringType),
            th.Property("OBJECT_NAME", th.StringType),
            th.Property("OBJECT_ID", th.StringType),
            th.Property("CENTER_NAME", th.StringType),
            th.Property("REF_FRAME", th.StringType),
            th.Property("TIME_SYSTEM", th.StringType),
            th.Property("MEAN_ELEMENT_THEORY", th.StringType),
            th.Property("EPOCH", th.StringType),
            th.Property("MEAN_MOTION", th.NumberType),
            th.Property("ECCENTRICITY", th.NumberType),
            th.Property("INCLINATION", th.NumberType),
            th.Property("RA_OF_ASC_NODE", th.NumberType),
            th.Property("ARG_OF_PERICENTER", th.NumberType),
            th.Property("MEAN_ANOMALY", th.NumberType),
            th.Property("EPHEMERIS_TYPE", th.IntegerType),
            th.Property("CLASSIFICATION_TYPE", th.StringType),
            th.Property("NORAD_CAT_ID", th.IntegerType),
            th.Property("ELEMENT_SET_NO", th.IntegerType),
            th.Property("REV_AT_EPOCH", th.IntegerType),
            th.Property("BSTAR", th.NumberType),
            th.Property("MEAN_MOTION_DOT", th.NumberType),
            th.Property("MEAN_MOTION_DDOT", th.NumberType),
            th.Property("SEMIMAJOR_AXIS", th.NumberType),
            th.Property("PERIOD", th.NumberType),
            th.Property("APOAPSIS", th.NumberType),
            th.Property("PERIAPSIS", th.NumberType),
            th.Property("OBJECT_TYPE", th.StringType),
            th.Property("RCS_SIZE", th.StringType),
            th.Property("COUNTRY_CODE", th.StringType),
            th.Property("LAUNCH_DATE", th.StringType),
            th.Property("SITE", th.StringType),
            th.Property("DECAY_DATE", th.StringType),
            th.Property("DECAYED", th.IntegerType),
            th.Property("FILE", th.IntegerType),
            th.Property("GP_ID", th.IntegerType),
            th.Property("TLE_LINE0", th.StringType),
            th.Property("TLE_LINE1", th.StringType),
            th.Property("TLE_LINE2", th.StringType)
        ))
    ).to_dict()
