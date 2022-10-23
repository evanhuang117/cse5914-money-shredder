from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PickupOptionSummary")


@attr.s(auto_attribs=True)
class PickupOptionSummary:
    """The type that defines the fields for the local pickup options that are available for the item. It is used by the <b>
    pickupOptions</b>  container.

        Attributes:
            pickup_location_type (Union[Unset, str]): This container returns the local pickup options available to the
                buyer. Possible values are <code>ARRANGED_LOCATION</code> and <code>STORE</code>.
    """

    pickup_location_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pickup_location_type = self.pickup_location_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pickup_location_type is not UNSET:
            field_dict["pickupLocationType"] = pickup_location_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pickup_location_type = d.pop("pickupLocationType", UNSET)

        pickup_option_summary = cls(
            pickup_location_type=pickup_location_type,
        )

        pickup_option_summary.additional_properties = d
        return pickup_option_summary

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
