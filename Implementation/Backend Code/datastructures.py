from dataclasses import dataclass
from datetime import date

@dataclass
class Serviceman():
	surname: str
	forename: str
	age: int
	honours_awards: str
	date_of_death: date
	rank: str
	regiment: str
	unit_ship_squadron: str
	country: str
	service_number: str
	cemetary_memorial: str
	grave_reference: str
	additional_info: str