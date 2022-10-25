from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeDuration")


@attr.s(auto_attribs=True)
class TimeDuration:
    """The type that defines the fields for a period of time in the time-measurement units supplied.

    Attributes:
        unit (Union[Unset, str]): An enumeration value that indicates the units (such as hours) of the time span. The
            enumeration value in this field defines the period of time being used to measure the duration. <br><br><b> Valid
            Values: </b> YEAR, MONTH, DAY, HOUR, CALENDAR_DAY, BUSINESS_DAY, MINUTE, SECOND, or MILLISECOND <br /><br />Code
            so that your app gracefully handles any future changes to this list. For implementation help, refer to <a
            href='https://developer.ebay.com/api-docs/buy/browse/types/ba:TimeDurationUnitEnum'>eBay API documentation</a>
        value (Union[Unset, int]): Retrieves the duration of the time span (no units).The value in this field indicates
            the number of years, months, days, hours, or minutes in the defined period.
    """

    unit: Union[Unset, str] = UNSET
    value: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit = self.unit
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unit is not UNSET:
            field_dict["unit"] = unit
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unit = d.pop("unit", UNSET)

        value = d.pop("value", UNSET)

        time_duration = cls(
            unit=unit,
            value=value,
        )

        time_duration.additional_properties = d
        return time_duration

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
