from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TargetLocation")


@attr.s(auto_attribs=True)
class TargetLocation:
    """The type that defines the fields for the distance between the item location and the buyer's location.

    Attributes:
        unit_of_measure (Union[Unset, str]): This value shows the unit of measurement used to measure the distance
            between the location of the item and the buyer's location. This value is typically <code> mi</code> or <code>
            km</code>.
        value (Union[Unset, str]): This value indicates the distance (measured in the measurement unit in the <b>
            unitOfMeasure</b>  field) between the item location and the buyer's location.
    """

    unit_of_measure: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_of_measure = self.unit_of_measure
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unit_of_measure is not UNSET:
            field_dict["unitOfMeasure"] = unit_of_measure
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unit_of_measure = d.pop("unitOfMeasure", UNSET)

        value = d.pop("value", UNSET)

        target_location = cls(
            unit_of_measure=unit_of_measure,
            value=value,
        )

        target_location.additional_properties = d
        return target_location

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
